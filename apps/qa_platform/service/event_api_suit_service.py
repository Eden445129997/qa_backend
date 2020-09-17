#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apps.common.utils.decorator import (
    print_clazz, print_func, print_model_and_data
)

# 模型
from apps.qa_platform.models import domain
from apps.qa_platform.models import dto

# 自定义序列化方法
from apps.common.serializers import query_set_list_serializers
from apps.common.base_obj import BaseHandler
# pydantic错误校验
from pydantic import ValidationError
import logging, copy

# 日志
runner_log = logging.getLogger('event')

@print_clazz
class _CaseApiModelHandler(BaseHandler):
    """
    接口用例模型处理(获取模型、补全模型)
    """

    @print_func
    def handle(self, case_id):
        # 模型数据列表
        case_api_model = []
        # 模型表数据列表
        api_case_model_list = query_set_list_serializers(
            domain.ApiCaseModel.objects.filter(
                case_id=case_id, is_status=1, is_delete=0
            ).order_by('-sort').order_by('id')
        )
        for i in range(len(api_case_model_list)):
            model_node = api_case_model_list[i]
            # 补全接口信息
            api_info = domain.Api.objects.values(
                'api_name', 'method', 'path', 'content_type'
            ).get(
                id=model_node.get('api_id'), is_status=1, is_delete=0
            )
            # 创建校验点列表
            model_node['assert_list'] = []
            # 执行测试用例套件时，参数化处理器需要使用该字段
            model_node['sort'] = i

            # 补全模型需要关联的数据
            case_api_model.append(
                {**api_info, **model_node}
            )

        return self.successor.handle(case_api_model)

@print_clazz
class _DataPrepareHandler(BaseHandler):
    """
    数据准备（数据注入到模型中，生成ModelAndData）
    """

    def __init__(self):
        self.case_api_group = []

    @print_func
    def handle(self, case_api_model: list):
        # 如果这个用例下模型为空则直接返回，防止下方代码出错
        if not case_api_model:
            return self.case_api_group

        # 模型中节点id顺序
        model_order = [model_node.get("id") for model_node in case_api_model]

        # 拷贝模型列表 并替换拷贝后的列表 装进测试套件中
        for case_data in domain.ApiCaseData.objects \
                .values("id") \
                .filter(
            case_id=case_api_model[0].get('case_id'), is_status=1, is_delete=0
        ):
            # 数据id
            data_id = case_data.get('id')
            # 深拷贝
            model_and_data = copy.deepcopy(case_api_model)
            for node in model_and_data:
                node['data_id'] = data_id

            # 数据节点与模型节点替换
            for case_data_node in query_set_list_serializers(
                domain.ApiCaseDataNode.objects
                    .filter(data_id=data_id, is_status=1, is_delete=0)
            ):
                # 模型执行顺序的id列表，找到要替换的index
                data_node_index = model_order.index(
                    case_data_node.get("model_id")
                )
                # 将模型对应节点替换成数据
                model_and_data[data_node_index] = {**model_and_data[data_node_index], **case_data_node}

            # 补全断言, 校验点到指定模型节点添加数断言
            for assert_node in domain.ApiAssert.objects.values(
                'data_id', 'model_id', 'assert_method', 'assert_obj', 'assert_val'
            ).filter(
                data_id=data_id, is_status=1, is_delete=0
            ):
                assert_node_index = model_order.index(
                    assert_node.get('model_id')
                )
                model_and_data[assert_node_index].get('assert_list').append(assert_node)

            self.case_api_group.append(model_and_data)
        return self.successor.handle(self.case_api_group)

@print_clazz
class _CaseApiValidateHandler(BaseHandler):
    """
    用例校验（每个用例下都是）
    """

    @print_model_and_data
    def handle(self, case_api_group: list):
        for model_and_data in case_api_group:
            for i in range(len(model_and_data)):
                try:
                    model_and_data[i] = dto.CaseApiNode(**model_and_data[i])
                except ValidationError as e:
                    runner_log.error(e.json())
                    return False
        return case_api_group

@print_clazz
class ApiSuitChainOfResponsibility(object):
    """
    测试套件责任链
    建立模型 --> 注入数据 --> 校验
        只要有一个校验失败返回False
    :returns : 1：测试套件 --> deque([case_group1[case[api_node1,api_node2],case2[api_node1,api_node2]],case_group2[])
               2：None
    业务逻辑
    目的：获取列表的测试套件（执行任务根据套件顺序执行）
    用例模型 关系与概念：
        一个业务流程存在多个接口，并且接口之间有执行顺序与参数依赖关系
        数据驱动设计：
            用例 = 模型 + 数据
            模型：定义了接口之间的执行顺序与配置，由多个接口节点构成
            数据：数据会注入到模型之中，对对应模型的节点进行替换操作，从而完成类似数据驱动的思想
            总结：一个用例一个模型，但可以拥有多组数据
    1、根据用例id，获取用例模型（多个节点）
    2、循环每个模型节点，进行数据补全
    3、拷贝模型，数据节点根据关联关系找到对应模型节点的索引 替换节点
    4、校验每个用例的数据，校验失败返回None
    5、校验成功，将 用例对象 装进测试套件
    """

    def __init__(self):
        self.test_suit = dto.TestSuitForDeque()
        self.case_api_model_obj = _CaseApiModelHandler()
        self.data_prepare_obj = _DataPrepareHandler()
        self.case_api_suit_validate = _CaseApiValidateHandler()
        # 设置链
        self.case_api_model_obj.set_successor(self.data_prepare_obj)
        self.data_prepare_obj.set_successor(self.case_api_suit_validate)

    def main(self, case_id_list: list):
        case_id_iter = case_id_list.__iter__()
        while True:
            try:
                case_api_group = self.case_api_model_obj.handle(
                    case_id_iter.__next__()
                )
                # 为了防止有不合格的数据
                if case_api_group is False:
                    return None
                self.test_suit.append(case_api_group)
            # 跳出用例的迭代
            except StopIteration:
                break
        return self.test_suit

def case_id_list_by_plan_id(plan_id: int):
    """
    1、根据测试计划获取测试用例id列表
    2、根据测试用例id列表获取测试套件
    :param plan_id:
    :return: 测试套件列表 or 数据异常为None
    """
    # 根据测试计划获取测试用例列表
    return [
        id.get("id")
        # 循环queryset字典列表
        for id in domain.QaCase.objects
            .values("id")
            .filter(id=plan_id, is_status=1, is_delete=0)
            .order_by('-sort').order_by('id')
    ]

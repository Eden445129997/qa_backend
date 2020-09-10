#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
runner_log = logging.getLogger('runner_log')


def print_model_and_data(func):
    """打印入参列表数据 装饰器"""

    def outter_wrapper(*args, **kwargs):
        print("*" * 200)
        suit: list or tuple = args[1]
        for case_group in suit:
            print("* 场景分组  ：", case_group)
            print("* 数据类型  ：", type(case_group))
            for i in range(len(case_group)):
                print("* 数据内容 %s:" % i, case_group[i])
            print("*" * 200)
        return func(*args, **kwargs)

    return outter_wrapper


class _CaseApiModelHandler(BaseHandler):
    """
    接口用例模型处理(获取模型、补全模型)
    """

    def handle(self, case_id):
        # 模型
        case_api_model = []
        # 补全模型节点
        for model_node in query_set_list_serializers(
            domain.ApiCaseModel.objects
                .filter(case_id=case_id, is_status=1, is_delete=0)
                .order_by('-sort').order_by('id')
        ):
            # 补全接口信息
            api_info = domain.Api.objects.values(
                'api_name', 'method', 'path', 'content_type'
            ).get(
                id=model_node.get('api_id'), is_status=1, is_delete=0
            )

            # 补全校验点
            model_node['assert_list'] = list(
                domain.ApiAssert.objects.values(
                    'api_model_id', 'assert_object', 'assert_method', 'assert_value'
                ).filter(
                    api_model_id=model_node.get('id'), is_status=1, is_delete=0
                )
            )
            # 补全模型需要关联的数据
            case_api_model.append(
                {**api_info, **model_node}
            )

        return self.successor.handle(case_api_model)


class _DataPrepareHandler(BaseHandler):
    """
    数据准备（数据注入到模型中，生成ModelAndData）
    """

    def __init__(self):
        self.case_api_group = []

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
                serch_index = model_order.index(
                    case_data_node.get("model_id")
                )
                # 将模型对应节点替换成数据
                model_and_data[serch_index] = {**model_and_data[serch_index], **case_data_node}
            self.case_api_group.append(model_and_data)
        return self.successor.handle(self.case_api_group)


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


class ApiSuitChainOfResponsibility(object):
    """
    测试套件责任链
    建立模型 --> 注入数据 --> 校验
        只要有一个校验失败返回False
    :returns : 1：测试套件 --> deque([case_group1[case[api_node1,api_node2],case2[api_node1,api_node2]],case_group2[])
               2：None
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


def get_test_suit_by_plan_id(plan_id: int):
    """
    1、根据测试计划获取测试用例id列表
    2、根据测试用例id列表获取测试套件
    :param plan_id:
    :return: 测试套件列表 or 数据异常为None
    """
    # 根据测试计划获取测试用例列表
    case_id_list = [
        id.get("id")
        # 循环queryset字典列表
        for id in domain.QaCase.objects
            .values("id")
            .filter(id=plan_id, is_status=1, is_delete=0)
            .order_by('-sort').order_by('id')
    ]
    return _get_test_suit_by_case_id_list(case_id_list)


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


def get_test_suit_by_case_id(case_id: int):
    """
    根据测试用例id列表获取测试套件
    :param case_id:
    :return: 测试套件列表 or 数据异常为None
    """
    return _get_test_suit_by_case_id_list(
        [case_id]
    )


def _get_test_suit_by_case_id_list(case_id_list: list):
    """
    根据用例id的列表获取测试套件
    :return: 测试套件列表 or 数据异常为None
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
    # 测试套件：deque
    test_suit = dto.TestSuitForDeque()

    for case_id in case_id_list:
        # 这个是临时的list，为了方便数据注入替换对应的
        case_model = []
        # 这个是节点的id列表，为了让数据替换对应的index
        test_case_order_list = [
            query_set_dict_list.get("id")
            for query_set_dict_list in domain.ApiCaseModel.objects
                .values("id")
                .filter(case_id=case_id, is_status=1, is_delete=0)
                .order_by('-sort').order_by('id')
        ]

        # 补全模型节点的数据
        # 将模型节点按顺序添加进入列表，成为一个临时存储的完全模型
        for test_case_node in query_set_list_serializers(
            domain.ApiCaseModel.objects
                .filter(case_id=case_id, is_status=1, is_delete=0)
                .order_by('-sort').order_by('id')
        ):
            # 补全模型需要关联的数据
            case_model.append(
                _make_case_node_to_complete(test_case_node)
            )

        # 获取用例数据列表
        # 拷贝模型列表 并替换拷贝后的列表 装进测试套件中
        for case_data in domain.ApiCaseData.objects \
            .values("id") \
            .filter(
            case_id=case_id, is_status=1, is_delete=0
        ):
            # 深拷贝
            case_model_with_data = copy.deepcopy(case_model)

            # 数据节点与模型节点替
            for case_data_node in query_set_list_serializers(
                domain.ApiCaseDataNode.objects
                    .filter(data_id=case_data.get("id"), is_status=1, is_delete=0)
            ):
                # 模型执行顺序的id列表，找到要替换的index
                serch_index = test_case_order_list.index(
                    case_data_node.get("model_id")
                )
                # 将模型对应节点替换成数据
                case_model_with_data[serch_index] = {**case_model_with_data[serch_index], **case_data_node}
            # 校验所有用例节点
            if _case_validate(case_model_with_data) is False:
                return None
            test_suit.append(case_model_with_data)
    return test_suit


def _make_case_node_to_complete(test_case_node: dict):
    """
    补全用例模型中的节点
    :return: TestSuitNode or None
    """
    # 补全接口信息
    api_info = domain.Api.objects.values(
        'api_name', 'method', 'path', 'content_type'
    ).get(
        id=test_case_node.get('api_id'), is_status=1, is_delete=0
    )

    # 补全校验点
    test_case_node['assert_list'] = list(
        domain.ApiAssert.objects.values(
            'api_model_id', 'assert_object', 'assert_method', 'assert_value'
        ).filter(
            api_model_id=test_case_node.get('id'), is_status=1, is_delete=0
        )
    )
    return {**api_info, **test_case_node}


def _case_validate(case_model_with_data: list):
    """
    校验模型每一个节点
    :param case_model_with_data:
    :return:
    """

    for i in range(len(case_model_with_data)):
        try:
            case_model_with_data[i] = dto.CaseApiNode(**case_model_with_data[i])
        except ValidationError as e:
            runner_log.error(e.json())
            return False
    return case_model_with_data

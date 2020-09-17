#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import threading
import sys
import datetime

from apps.common.utils.decorator import (
    print_clazz, print_func
)

from apps.qa_platform.models.domain import EventApiResult
from apps.qa_platform.models.dto import (
    Context, TestSuitForDeque, CaseApiNode
)
from apps.qa_platform.enumeration import EventApiStatus
from apps.qa_platform.service.event_api_suit_service import (
    ApiSuitChainOfResponsibility, case_id_list_by_plan_id
)
from apps.qa_platform.service.event_api_record_service import ApiRunChainOfResponsibility

# 日志
event_log = logging.getLogger('event')

@print_clazz
class EventApiResultThread(threading.Thread):

    log = event_log

    def __init__(
            self,
            context : Context
    ):
        super().__init__()
        self.context = context
        # 接口测试结果
        self.result_obj = self.mk_event_api_result()
        self.suit_chain = ApiSuitChainOfResponsibility()
        self.run_chain = ApiRunChainOfResponsibility()
        self.err_record = []

    @print_func
    def handle_context(self):
        """处理context数据"""
        if not self.context.plan_id and not self.context.case_id:
            raise ValueError('缺少必填参数：plan_id or case_id')
        elif self.context.plan_id and self.context.case_id:
            raise ValueError('plan_id和case_id其中只能有一个，请检查context')
        elif self.context.plan_id:
            self.context.case_id_list = case_id_list_by_plan_id(self.context.plan_id)
        else:
            self.context.case_id_list = [self.context.case_id]

    @print_func
    def mk_event_api_result(self):
        """创建事件对象，并计入等待"""
        result_obj = EventApiResult(
            host=self.context.host,
            current_status=EventApiStatus.WAIT.value
        )
        result_obj.save()
        return result_obj

    @print_func
    def start_event_api(self):
        """开始事件"""
        print("event_api_result:",EventApiStatus.EXECUTION.value)
        self.result_obj.current_status = EventApiStatus.EXECUTION.value
        self.result_obj.total = len(self.suit)
        self.result_obj.is_prepared = True
        self.result_obj.save()
        return datetime.datetime.now()

    @print_func
    def stop_event_api(self, start_time : datetime):
        """结束事件"""
        self.result_obj.current_status = EventApiStatus.FINISH.value
        self.result_obj.time_taken = datetime.datetime.now() - start_time
        self.result_obj.save()

    @print_func
    def fail_event_api(self):
        """结束事件"""
        self.result_obj.current_status = EventApiStatus.FAILSE.value
        self.result_obj.err_record = self.err_record
        self.result_obj.save()

    @print_func
    def run(self):
        try:
            # 处理context信息
            self.handle_context()
            # 测试套件 链子
            self.suit: TestSuitForDeque = self.suit_chain.main(self.context.case_id_list)
            # 执行测试套件 执行链对象
            start_time = self.start_event_api()
            # 责任链模式：执行测试套件
            for case_api_group in self.suit:
                # 接口模型测试点（笛卡尔积:迭代次数=模型*数据）
                group_iter = case_api_group.__iter__()
                while True:
                    try:
                        # 接口点下具体测试用例（迭代次数=模型关联的可用数据次数）
                        model_and_data_iter = group_iter.__next__().__iter__()
                        while True:
                            try:
                                case_api_node: CaseApiNode = model_and_data_iter.__next__()
                                case_api_node.result_id = self.result_obj.id
                                case_api_node.path = "%s%s" % (self.context.host, case_api_node.path)
                                event_log.info(case_api_node)
                                # 失败跳过该数据
                                if not self.run_chain.main(case_api_node):
                                    self.err_record.append(
                                        'case_id:%s,data_id:%s' % (
                                            case_api_node.case_id, case_api_node.data_id
                                        )
                                    )
                                    break
                            except StopIteration:
                                break
                    # 跳出用例的迭代
                    except StopIteration:
                        break
            # 如果有失败记录则标记失败
            if self.err_record:
                self.fail_event_api()
            self.stop_event_api(start_time)
        except ValueError as e:
            event_log.error(e)
            self.err_record.append(e)
            self.fail_event_api()
        except Exception as e:
            event_log.error(e)
            self.err_record.append(e)
            self.fail_event_api()
        finally:
            sys.exit()

    # 方案1：使用生成器维护这四种状态，使用迭代器处理每一个用例节点
    # 生成器：使用while循环执行四种状态的return
    # 迭代器（两层迭代器）：使用while循环处理迭代器返回的每个用例与每个用例节点
    # 责任链模式：用例节点执行 — 数据准备（序列化逻辑）、参数化逻辑、mock与请求逻辑、校验点逻辑-
    #
    # 创建测试报告 执行状态：等待中（枚举）入餐：测试套件，计算总数
    # 执行状态：执行中（枚举）入餐：测试套件，处理套件中的每一个
    #                    入餐：使用迭代器，每次执行返回对应的节点数据
    # 执行状态：完成任务（枚举）
    # 执行状态：失败任务（枚举）
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import threading
import sys
import datetime

from apps.common.utils.decorator import (
    print_clazz, print_func
)

from apps.qa_platform.models.domain.event_api_result import EventApiResult
from apps.qa_platform.models.dto import (
    Context, TestSuitForDeque, CaseApiNode
)
from apps.qa_platform.enumeration import EventApiStatus

from apps.qa_platform.service.event_api_suit_service import (
    ApiSuitChainOfResponsibility, query_case_id_list_by_plan_id
)

from apps.qa_platform.service.event_api_record_service import ApiRunChainOfResponsibility

# 日志
event_log = logging.getLogger('event')


# @print_func
# def handle_context(context : Context):
#     """处理context数据"""
#     if not context.plan_id and not context.case_id:
#         raise ValueError('缺少必填参数：plan_id or case_id')
#     elif context.plan_id and context.case_id:
#         raise ValueError('plan_id和case_id其中只能有一个，请检查context')
#     elif context.plan_id:
#         context.case_id_list = query_case_id_list_by_plan_id(context.plan_id)
#     else:
#         context.case_id_list = [context.case_id]
#         runner = EventApiResultThread(context)
#         runner.run()

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
        self.headers = context.headers
        self.err_record = []

    @print_func
    def handle_context(self):
        """处理context数据"""
        if not self.context.plan_id and not self.context.case_id:
            raise ValueError('缺少必填参数：plan_id or case_id')
        elif self.context.plan_id and self.context.case_id:
            raise ValueError('plan_id和case_id其中只能有一个，请检查context')
        elif self.context.plan_id:
            self.context.case_id_list = query_case_id_list_by_plan_id(self.context.plan_id)
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
        self.result_obj.current_status = EventApiStatus.FALSE.value
        self.result_obj.err_record = self.err_record
        self.result_obj.save()

    @print_func
    def run(self):
        """
        业务逻辑：
            1、接收context，根据context执行api的事件逻辑
            2、result四种状态
                等待状态
                    获取测试套件责任链
                        未完成获取测试套件：is_prepared = 0
                        完成获取测试套件：is_prepared = 1
                运行状态（已完成获取测试套件进入该阶段）
                    接口请求事件责任链
                        请求失败：跳出该这个测试点下的某个用例，但仍然执行该测试点其他用例
                        并标记result状态为失败
                完成状态
                    当运行完测试套件，并没有错误则标记
                失败状态
                    1、获取测试套件失败
                    2、执行测试用例失败
                    3、未知异常标记失败
        迭代器（两层迭代器）：使用while循环处理迭代器返回的每个用例与每个用例节点
        责任链模式：用例节点执行 — 数据准备（序列化逻辑）、参数化逻辑、mock与请求逻辑、校验点逻辑-
        """
        try:
            # 处理context信息
            self.handle_context()
            # 测试套件 链子
            self.suit: TestSuitForDeque = self.suit_chain.main(self.context.case_id_list)
            if self.suit is None:
                raise ValueError('测试套件获取失败，测试套件存在脏数据')
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
                                case_api_node.headers = {**case_api_node.headers, **self.headers}
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
            else:
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, logging, datetime, threading  # ,collections, sys, time
from apps.test_platform.api_framework.http import HttpBuilder
from apps.test_platform.api_framework.parameters import ParametersBuilder
from apps.test_platform.api_framework.report import ReportBuilder
from apps.test_platform.api_framework.checkpoint import CheckpointBuilder

# 序列化
# from apps.common.serializers import query_set_list_serializers

# 枚举
from apps.test_platform.enumeration import TaskStatus

# 日志
runner_log = logging.getLogger('runner_log')

"""
todo：
任务顺序
1、计划前置
2、用例前置
3、用例后置
4、计划后置

是否支持sql？
    1、将表变成接口的方式呈现
    2、允许人员手写sql
正则获取
断言

mock如何处理？
方案1（已临时解决）：
    添加字段，当mock的时候，取mock值

步骤
1、根据id查询这次运行的测试计划或者用例所需要的数据（前置，后置，入参出参）
2、创建一个线程运行该次任务（这里需要一个表存储任务数据，失败需要补偿）
3、执行任务（正则、断言。后期优化做同步或者异步）
4、数据写入到测试报告中
"""


class TaskDirector(threading.Thread):
    """执行任务对象：
        创建对象：
            1、host：http://0.0.0.0:9998/
            2、headers(非必填)：{'cookie': 'xxx' }
        执行任务：
            1、任务列表：数据格式[{get},{post},{put},{delete}]
        mock逻辑：
            判断mock_status，启用则跳过，并且将mock_response当作response
        status启用逻辑:
            问题：当不启用时，如何处理校验点逻辑
            解决方案1：更新不启用时，判断断言，如果有则不允许更新
            暂时还没完全想好
    """

    log = runner_log

    def __init__(self, suit, host, headers=None):

        super().__init__()

        self.http_builder = HttpBuilder()
        self.parameters_builder = ParametersBuilder()
        self.report_builder = ReportBuilder()
        self.checkpoint_builder = CheckpointBuilder()
        # self.data_factory = factory.DataFactory()

        self.suit = suit
        self.host = host if host else 'http://localhost'
        self.headers = {}

        if headers:
            self.headers = headers

    def run(self):
        """指挥测试任务"""
        # todo：
        #  1、参数化（完成）
        #  2、检查点
        #  3、异步处理，加入mq等中间件（生产者负责生产任务，指挥者负责消费任务）
        #  4、任务存储走缓存
        #  5、任务死锁异常处理—定时任务（补偿处理）
        total = len(self.suit)

        # 创建报告
        report_id = self.report_builder.wait_build_test_report(executor="Eden", host=self.host, total=total)
        self.report_builder.start_buil_test_report(report_id)

        # 计算测试计划执行时间
        task_start_time = datetime.datetime.now()

        # print(self.test_task)
        # print(report_id)

        # print(self.suit)

        # 执行任务
        for case in self.suit:
            # print(case)
            # 基础接口信息
            api_name = case.get('api_name', '')
            method = case.get('method', '')
            path = case.get('path', '')

            # 请求配置信息
            case_id = case.get('case_id', '')
            # interface_id = test_task.get('interface_id','')
            reconnection_times = case.get('reconnection_times', 3)
            wait_time = case.get('wait_time', 10)
            sort = case.get('sort', 0)

            # 请求参数
            headers = case.get('headers', '{}')
            data = case.get('data', '{}')

            # 参数化逻辑字段
            expression_status = case.get('expression_status', False)

            # mock逻辑
            mock_status = case.get('mock_status', False)

            # 校验点
            checkpoint_list = case.get('checkpoint_list', [])

            # 拼接成具体请求的url
            url = '%s%s' % (self.host, path)

            fail_times = 0
            error_list = []

            # 进入参数化逻辑代码
            if expression_status:
                parameters_dict = self.parameters_builder.build(data, report_id)
                data = parameters_dict.get('response')
                error_list.extend(parameters_dict.get('error_list'))

            # 序列化请求头
            headers = json.loads(headers.replace('\'', '"'))
            # 合并请求头，顺序不能变
            headers = {**headers, **self.headers}

            # 序列化成python可操作数据类型
            try:
                # headers = json.loads(headers.replace('\'', '"'))
                data = json.loads(data.replace('\'', '"'))
            except Exception as e:
                self.log.error('json序列化失败:\n请求头：{}\n请求参数{}\n错误：{}'.format(headers, data, e))
                error_list.append(e)
                # break
                # raise KeyboardInterrupt

            # 开始计时
            case_start_time = datetime.datetime.now()

            # 如果mock=true，则跳过发送请求，否则发送
            if mock_status:
                response = case.get('mock_response', '{}')
            # 发送http请求
            else:
                # 构造http请求
                self.http_builder.build_http(
                    method=method, url=url, headers=headers, data=data,
                    reconnection_times=reconnection_times, timeout=wait_time
                )
                # 发送http请求
                http = self.http_builder.send_http()
                # 重置http
                self.http_builder.reset_http()

                # 覆盖默认失败次数
                fail_times = http.get('fail_times', 0)
                response = http.get('response', None)
                error_list.extend(http.get('error_list', []))

                # 校验点
                error_list.extend(self.checkpoint_builder.build(checkpoint_list, response).get('error_list'))

            # 结束计时
            case_stop_time = datetime.datetime.now()
            case_time_taken = case_stop_time - case_start_time

            # 执行完这次请求后，生成对应的测试细节信息数据
            self.report_builder.running_buil_test_report_detail(
                case_id=case_id, report_id=report_id,
                api_name=api_name,
                url=url,
                header=headers,
                data=data,
                response=response,
                error_record=error_list,
                fail_times=fail_times,
                is_mock=mock_status,
                sort=sort,
                start_time=case_start_time,
                stop_time=case_stop_time,
                time_taken=case_time_taken
            )
            # 假如有报错信息，标记失败，跳出循环，不再执行
            if error_list:
                self.report_builder.failse_buil_test_report(report_id)
                break

        # 计时
        task_stop_time = datetime.datetime.now()
        task_time_taken = task_stop_time - task_start_time

        # 正常的报告
        if self.report_builder.task_status != TaskStatus.FAILSE.value:
            self.report_builder.stop_buil_test_report(report_id=report_id, time_taken=task_time_taken)
        self.log.info('report_id:%s\ntask_status:%s\ntest_task:%s\ntime_taken:%s'
                      % (report_id, self.report_builder.task_status, self.suit, task_time_taken))

        # 线程中断代码，主动停止，用户抛出异常
        # raise KeyboardInterrupt

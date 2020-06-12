#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json, logging, datetime, threading  # ,collections, sys, time
# from functools import wraps

# 工厂
from apps.test_platform import factory
# 模型
from apps.test_platform import models
# 序列化
# from apps.common.serializers import query_set_list_serializers

# 枚举
from apps.test_platform.enumeration import TaskStatus

# https警告解除
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

# 尽量别用这种方式，闭包的方式会慢很多
# 3.2901763916015625e-05
# 8.344650268554688e-06
# def timeTaken(func):
#     """计算执行时间"""
#     startTime = time.time()
#
#     @wraps(func)
#     def inner_wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     stopTime = time.time()
#     timeTaken = stopTime - startTime
#     runner_log.info("方法:%s" % func)
#     runner_log.info("执行时长:%s" % timeTaken)
#     return inner_wrapper

def _get(url, data, headers, timeout=10):
    return requests.request(method='GET', url=url, params=data, headers=headers, verify=False, timeout=timeout)


def _post(url, data, headers, timeout=10):
    return requests.request(method='POST', url=url, json=data, headers=headers, verify=False, timeout=timeout)


def _put(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="PUT", url=url, data=data, headers=headers, verify=False, timeout=timeout)


def _delete(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="DELETE", url=url, headers=headers, verify=False, timeout=timeout)


# 选择请求方式
choice = {
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}


class HttpBuilder(object):
    """
    http建造者
    """

    log = runner_log

    def __init__(self):
        self.result = {
            'response': None,
            'fail_times': 0,
            'error': []
        }

        self._url = None
        self._data = None
        self._headers = None
        self._reconnection_times = None
        self._rest_reconnection_times = None
        self._timeout = None
        self._fail_times = None

    def build_http(self, method, url, data, headers, reconnection_times=3, timeout=10):
        self._method = method
        self._url = url
        self._headers = headers if isinstance(headers, dict) else {}
        self._data = data if isinstance(data, dict) else {}
        self._reconnection_times = reconnection_times
        self._rest_reconnection_times = reconnection_times
        self._timeout = timeout
        # print(self._url)

    def send_http(self):
        """发送http请求"""
        # 发送请求，失败则递归重复发送
        try:
            # print(self._url)
            response = choice.get(self._method)(url=self._url, data=self._data, headers=self._headers,
                                                timeout=self._timeout)
            # 二进制字符集编码设置
            # response = response.content.decode("unicode_escape")
            response = response.text
            response = json.loads(response)
            self.result['response'] = response
            # 失败次数 = 重连次数 - 剩余重连次数
            self.result['fail_times'] = self._reconnection_times - self._rest_reconnection_times

        except Exception as e:
            self.log.error(e)
            self.result.get('error', []).append(e)
            # 剩余重连次数
            self._rest_reconnection_times = self._rest_reconnection_times - 1
            # 剩余重连次数 > 0，则递归
            if self._rest_reconnection_times:
                self.send_http()

        return self.result


class ReportBuilder(object):
    """
    测试报告建造者
    """

    def __init__(self):
        self.data_factory = factory.DataFactory()
        self.task_status = None

    def build(self):
        pass

    def wait_build_test_report(self, executor, host, total):
        """
        创建测试报告
        执行状态：等待中（枚举）
        :return:
        """
        try:
            api_test_report = models.ApiTestReport(executor=executor, host=host, total=total,
                                                   task_status=TaskStatus.WAIT.value)
            api_test_report.save()
            self.task_status = TaskStatus.WAIT.value
            return api_test_report.id
        except Exception as e:
            runner_log.error(e)

    def start_buil_test_report(self, report_id):
        """
        开始执行，更新执行状态为执行中
        执行状态：执行中（枚举）
        :return:
        """
        try:
            api_test_report = models.ApiTestReport.objects.get(id=report_id)
            api_test_report.task_status = TaskStatus.EXECUTION.value
            api_test_report.save()
        except Exception as e:
            runner_log.error(e)

    def running_buil_test_report_detail(self,
                                        case_id, report_id, url, api_name, header, data, response,
                                        error_record, fail_times, is_mock, sort,
                                        start_time, stop_time, time_taken
                                        ):
        """
        添加测试用例细节数据
        :return:
        """
        try:
            apiTest_report_detail = models.ApiTestReportDetail(
                case_id=case_id, report_id=report_id,
                api_name=api_name,
                url=url,
                header=header,
                data=data,
                response=response,
                error_record=error_record, fail_times=fail_times, is_mock=is_mock, sort=sort, start_time=start_time,
                stop_time=stop_time, time_taken=time_taken
            )
            apiTest_report_detail.save()
        except Exception as e:
            runner_log.error(e)

    def stop_buil_test_report(self, report_id):
        """
        结束状态
        执行状态：结束任务（枚举）
        :return:
        """
        try:
            api_test_report = models.ApiTestReport.objects.get(id=report_id)
            api_test_report.task_status = TaskStatus.FINISH.value
            api_test_report.save()
            self.task_status = TaskStatus.FINISH.value
        except Exception as e:
            runner_log.error(e)


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

    def __init__(self, test_task, host, headers=None):

        super().__init__()

        self.http_builder = HttpBuilder()
        self.report_builder = ReportBuilder()

        self.test_task = test_task
        self.host = host if host else 'http://localhost'
        self.headers = {}

        if headers:
            self.headers = headers

    def run(self):
        """指挥测试任务"""
        # todo：
        #  1、参数化（
        #  判断parameters_status
        #  获取对应节点的response判断数据类型
        #  使用parameters,jsonpath解析后判断为真
        #  根据parameters_index获取之并处理异常outofindex
        #     解决方案1：case_detail加字段，用户控制是否正则解析表达式
        #     解决方案2：所有入参默认解析，只要用户写了正则匹配，根据写的正则匹配进行匹配
        #  2、检查点
        #  3、异步处理，加入mq等中间件（生产者负责生产任务，指挥者负责消费任务）
        #  4、任务存储走缓存
        #  5、任务死锁异常处理—定时任务（补偿处理）
        total = len(self.test_task)

        # 创建报告
        report_id = self.report_builder.wait_build_test_report(executor="Eden", host=self.host, total=total)
        self.report_builder.start_buil_test_report(report_id)

        # 计算测试计划执行时间
        task_start_time = datetime.datetime.now()

        # print(self.test_task)
        # print(report_id)

        # 执行任务
        for info in self.test_task:
            api_name = info.get('api_name', '')
            method = info.get('method', '')
            path = info.get('path', '')
            case_id = info.get('case_id', '')
            # interface_id = test_task.get('interface_id','')
            reconnection_times = info.get('reconnection_times', 3)
            wait_time = info.get('wait_time', 10)
            header = info.get('header', '{}')
            data = info.get('data', '{}')
            # checkpoint = info.get('checkpoint', '{}')
            sort = info.get('sort', 0)

            # 拼接成具体请求的url
            url = '%s%s' % (self.host, path)
            # 序列化
            header = json.loads(header)
            data = json.loads(data)
            print(type(header))
            # 合并请求头，顺序不能变
            headers = {**header, **self.headers}

            # mock逻辑
            mock_status = info.get('mock_status', False)

            # 开始计时
            case_start_time = datetime.datetime.now()
            fail_times = 0
            error_list = []

            # 如果mock=true，则跳过发送请求，否则发送
            if mock_status:
                response = info.get('mock_response', '{}')
            else:
                self.http_builder.build_http(
                    method=method, url=url, headers=headers, data=data,
                    reconnection_times=reconnection_times, timeout=wait_time
                )
                http = self.http_builder.send_http()
                # todo:校验点和正则在发送请求后进行json解析处理
                # 覆盖默认失败次数
                fail_times = http.get('fail_times', 0)
                response = http.get('response', {})
                error_list = http.get('error', [])
            # 结束计时
            case_stop_time = datetime.datetime.now()
            case_time_taken = case_stop_time - case_start_time
            # 失败次 = 重试次数 - 剩余重试，获取不到则默认减成0

            # 执行完这次请求后，生成对应的测试细节信息数据
            self.report_builder.running_buil_test_report_detail(
                case_id=case_id, report_id=report_id,
                api_name=api_name,
                url=url,
                header=header,
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

        # 计时
        task_stop_time = datetime.datetime.now()
        task_time_taken = task_stop_time - task_start_time

        # 报告状态
        self.report_builder.stop_buil_test_report(report_id=report_id)
        self.log.info('report_id:%s\ntask_status:%s\ntest_task:%s\ntime_taken:%s'
                      % (report_id,self.report_builder.task_status,self.test_task,task_time_taken))

        # print(task_time_taken)


if __name__ == '__main__':
    headers = {
        'CONTENT_TYPE': 'text/plain'
    }
    data = {
        'id': 1
    }
    try:
        print(choice.get("GET")('http://localhost:9998/platform/ProjectViews/', data, headers).text)
    except ConnectionError:
        pass

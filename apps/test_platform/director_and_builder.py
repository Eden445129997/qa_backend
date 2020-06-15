#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json, logging, datetime, threading, re, jsonpath  # ,collections, sys, time
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
            'error_list': []
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
            self.result.get('error_list', []).append(e)
            # 剩余重连次数
            self._rest_reconnection_times = self._rest_reconnection_times - 1
            # 剩余重连次数 > 0，则递归
            if self._rest_reconnection_times:
                self.send_http()

        return self.result


class ParametersBuilder(object):
    """
    参数化建造者
    """

    log = runner_log

    def __init__(self):
        self.data_factory = factory.DataFactory()
        self.result = {
            'response': None,
            'error_list': []
        }

    def _regular_catch(self, regular, be_catch_object):
        """
        正则表达式捕捉数据
        :param regular:
        :param be_catch_object:
        :return: ['str'，'str']
        """
        return re.findall(regular, be_catch_object)

    def _error_record(self, *error_info):
        """
        异常流
        :param report_id:
        :param error_info:
        :return:
        """
        self.log.error('error_info：%s' % str(error_info))
        for error in error_info:
            self.result.get('error_list',[]).append(error)

    def build(self, data, report_id):
        """
        参数化
        成功则返回参数化之后的数据
        失败则返回参数化失败之后的数据
        异常流，停止执行代码
        :param data:
        :param report_id:
        :return:
        """

        self.result['response'] = data
        self.report_id = report_id

        # 参数化
        # {'a': '$..&011#','b': '渣男$多人运动&1#','c': '孤儿$亚索&2#'}
        # ['$..&011#', '$多人运动&1#', '$亚索&2#']
        catch_list = self._regular_catch("\$.*?&\d+?#", data)

        # 如果有符合正则规则的数据则进入参数化
        if catch_list:
            for i in range(len(catch_list)):
                try:
                    # 获取要查询的节点
                    # "$多人运动&1#"
                    # "1"
                    catch_index = int((self._regular_catch('&\d+?#', catch_list[i])[0][1:-1]))
                except ValueError as e:
                    self._error_record('非法的表达式%s' % catch_list[i], e)
                else:
                    try:
                        # 找到要捕捉的用例节点
                        catch_index_response = self.data_factory.get_report_detail_response_by_report_id_and_sort(
                            report_id=self.report_id, sort=catch_index)
                        # print(catch_index_response)
                    except Exception as e:
                        self._error_record('不存在该表达式节点%s' % catch_list[i],e)
                    else:
                        # 节点存在数据，jsonpath捕捉数据
                        if catch_index_response:
                            # jsonpath的查询参数
                            # "$多人运动&1#"
                            # "$多人运动"
                            catch_data = self._regular_catch('\$.*?&', catch_list[i])[0][:-1]
                            catch_result_list = jsonpath.jsonpath(catch_index_response, catch_data)
                            # 如果抓不到数据
                            if catch_result_list:
                                # 选择list中需要替换的参数
                                try:
                                    # 选择并替换'➡️"
                                    catch_result = str(catch_result_list[0]).replace('\'', '"')
                                    # print(catch_result)
                                except IndexError as e:
                                    self._error_record('索引越界：\n%s' % e)
                                except Exception as e:
                                    self._error_record('未知错误：\n%s' % e)
                                else:
                                    # 替换参数
                                    self.result['response'] = data.replace(catch_list[i], catch_result)
                            else:
                                self._error_record('jsonpath表达式捕捉为空%s' % catch_result_list)
                        else:
                            self._error_record('节点不存在数据%s' % catch_index_response)
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
            self.task_status = TaskStatus.EXECUTION.value
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
        状态
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

    def failse_buil_test_report(self, report_id):
        """
        状态
        执行状态：失败任务（枚举）
        :return:
        """
        try:
            api_test_report = models.ApiTestReport.objects.get(id=report_id)
            api_test_report.task_status = TaskStatus.FAILSE.value
            api_test_report.save()
            self.task_status = TaskStatus.FAILSE.value
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

    def __init__(self, suit, host, headers=None):

        super().__init__()

        self.http_builder = HttpBuilder()
        self.report_builder = ReportBuilder()
        self.parameters_builder = ParametersBuilder()
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

        # 执行任务
        for case in self.suit:
            # print(test_task)
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

            # todo：校验点逻辑字段
            # checkpoint = test_task.get('checkpoint', '{}')

            # 参数化逻辑字段
            parameters_status = case.get('parameters_status', False)

            # mock逻辑
            mock_status = case.get('mock_status', False)

            # 拼接成具体请求的url
            url = '%s%s' % (self.host, path)

            # 开始计时
            case_start_time = datetime.datetime.now()
            fail_times = 0
            error_list = []

            # 进入参数化逻辑代码
            if parameters_status:
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
                self.report_builder.stop_buil_test_report(report_id)
                self.log.error('json序列化失败:\n{}\n{}\n{}'.format(headers, data, e))
                error_list.append(e)
                # break
                # raise KeyboardInterrupt

            # 如果mock=true，则跳过发送请求，否则发送
            if mock_status:
                response = case.get('mock_response', '{}')
            # 发送http请求
            else:
                self.http_builder.build_http(
                    method=method, url=url, headers=headers, data=data,
                    reconnection_times=reconnection_times, timeout=wait_time
                )
                http = self.http_builder.send_http()
                # todo:校验点
                # 覆盖默认失败次数
                fail_times = http.get('fail_times', 0)
                response = http.get('response', {})
                error_list.extend(http.get('error_list', []))

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
            # 假如有报错信息，跳出循环，不再执行
            if error_list:
                break

        # 计时
        task_stop_time = datetime.datetime.now()
        task_time_taken = task_stop_time - task_start_time

        # 失败的报告
        if self.report_builder.task_status == TaskStatus.FINISH.value:
            self.report_builder.failse_buil_test_report(report_id=report_id)
        # 无异常的报告
        else:
            self.report_builder.stop_buil_test_report(report_id=report_id)
        self.log.info('report_id:%s\ntask_status:%s\ntest_task:%s\ntime_taken:%s'
                      % (report_id, self.report_builder.task_status, self.suit, task_time_taken))

        # 线程中断代码，主动停止，用户抛出异常
        # raise KeyboardInterrupt


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

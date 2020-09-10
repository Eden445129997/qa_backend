#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.common.base_obj import BaseHandler

from apps.qa_platform.models.dto import CaseApiNode
from apps.qa_platform.models.domain import EventApiRecord

import urllib3

import requests

import time

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from apps.common.http_utils import choice


def print_clazz(clazz):
    def outter_wrapper(*args, **kwargs):
        print("进入clazz：",clazz)
        return clazz(*args, **kwargs)
    return outter_wrapper

def print_func(func):
    def outter_wrapper(*args, **kwargs):
        print("进入func：",func)
        return func(*args, **kwargs)
    return outter_wrapper

@print_clazz
class _SetUpHandler(BaseHandler):

    @print_func
    def handle(self, case_node : CaseApiNode):
        return self.successor.handle(case_node)

@print_clazz
class _TearDownHandler(BaseHandler):

    @print_func
    def handle(self, case_node : CaseApiNode):
        if case_node.err_record:
            return False
        return True

@print_clazz
class _ExpressionHandler(BaseHandler):
    """
    表达式处理对象
    1、参数化表达式
    2、日期表达式
    """

    @print_func
    def handle(self, case_node):
        pass

@print_clazz
class _HttpPrepareHandler(BaseHandler):
    """数据准备对象（暂时无用，目前数据在suit一开始就注入好了）"""

    @print_func
    def handle(self, case_node):
        pass

@print_clazz
class _HttpHandler(BaseHandler):
    """
    http请求处理对象
    """

    @property
    def _method_tuple(self):
        return ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')

    @property
    def _method_dict(self):
        return {
            'GET': '_get',
            'POST': '_post',
            'PUT': '_put',
            'DELETE': '_delete',
        }

    def _default(
            self,
            method: str,
            url: str,
            params: dict,
            body: dict,
            headers: dict,
            timeout: int = 10
    ):
        """所有请求都引用该方法"""
        if method.upper() not in self._method_tuple:
            raise RuntimeError('不支持的请求方法')
        if headers and 'application/json' in headers.get('Content-Type'):
            return requests.request(method=method, url=url, params=params, json=body, headers=headers, verify=False,
                                    timeout=timeout)
        return requests.request(method=method, url=url, params=params, data=body, headers=headers, verify=False,
                                timeout=timeout)

    def _get(
            self, url: str,
            params: dict,
            body: dict,
            headers: dict,
            timeout: int = 10
    ):
        return self._default(method='GET', url=url, params=params, body=body, headers=headers, timeout=timeout)

    def _post(
            self, url: str,
            params: dict,
            body: dict,
            headers: dict,
            timeout: int = 10
    ):
        return self._default(method='POST', url=url, params=params, body=body, headers=headers, timeout=timeout)

    def _put(
            self, url: str,
            params: dict,
            body: dict,
            headers: dict,
            timeout: int = 10
    ):
        return self._default(method='PUT', url=url, params=params, body=body, headers=headers, timeout=timeout)

    def _delete(
            self, url: str,
            params: dict,
            body: dict,
            headers: dict,
            timeout: int = 10
    ):
        return self._default(method='DELETE', url=url, params=params, body=body, headers=headers, timeout=timeout)

    def _get_func(self, key: str):
        """获取请求方法"""
        func = self._method_dict.get(key)
        if func is None:
            return func
        if isinstance(func, str):
            func = getattr(self, func)
        return func

    def _handle_context(self, case_node: CaseApiNode):
        self._reconnection_times = case_node.reconnection_times
        self._rest_reconnection_times = case_node.reconnection_times

    def _send(self, case_node: CaseApiNode):
        request_func = self._get_func(case_node.method)
        try:
            response = request_func(
                url=case_node.path,
                params=case_node.query,
                body=case_node.body,
                headers=case_node.headers,
                timeout=case_node.timeout
            )
            # 二进制字符集编码设置
            # response = response.content.encode('utf-8')
            response = response.text
            # response = json.loads(response)
            case_node.response = response
            # 失败次数 = 重连次数 - 剩余重连次数
            case_node.fail_times = self._reconnection_times - self._rest_reconnection_times

        except requests.Timeout:
            print("进入timeout")
            # 剩余重连次数
            self._rest_reconnection_times = self._rest_reconnection_times - 1
            # 剩余重连次数 > 0，则递归
            if self._rest_reconnection_times:
                time.sleep(1)
                self._send(case_node)

        except Exception as e:
            print("进入exception")
            case_node.err_record.append(e)

    @print_func
    def handle(self, case_node: CaseApiNode):
        """责任链入口"""
        if case_node.is_mock:
            case_node.response = case_node.mock_response
            return self.successor.handle(case_node)
        self._handle_context(case_node)
        self._send(case_node)
        return self.successor.handle(case_node)

@print_clazz
class _AssertHandler(BaseHandler):
    """
    断言处理对象
    """

    @print_func
    def handle(self, case_node):
        pass

@print_clazz
class _ApiRecordHandler(BaseHandler):
    """
    请求结果处理对象
    """

    @print_func
    def handle(self, case_node : CaseApiNode):
        record_obj = EventApiRecord(
            result_id = case_node.result_id,
            case_id = case_node.case_id,
            data_id = case_node.data_id,
            api_name = case_node.api_name,
            url = case_node.path,
            headers = case_node.headers,
            params = case_node.query,
            body = case_node.body,
            response = case_node.response,
            err_record = case_node.err_record,
            fail_times = case_node.fail_times,
            is_mock = case_node.is_mock,
            sort = case_node.sort
        )
        record_obj.save()
        return self.successor.handle(case_node)

@print_clazz
class ApiRunChainOfResponsibility:
    """
    接口测试执行器责任链
    """

    def __init__(self):
        self.set_up_handler = _SetUpHandler()
        self.http_handler = _HttpHandler()
        self.api_record_handler = _ApiRecordHandler()
        self.tear_down_handler = _TearDownHandler()

        self.set_up_handler.set_successor(self.http_handler)
        self.http_handler.set_successor(self.api_record_handler)
        self.api_record_handler.set_successor(self.tear_down_handler)

    @print_func
    def main(self, case_node : CaseApiNode):
        return self.set_up_handler.handle(case_node)


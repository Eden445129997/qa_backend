#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.common.base_obj import BaseHandler
from apps.common.utils.decorator import (
    print_clazz, print_func
)

from apps.qa_platform.models.dto import CaseApiNode
from apps.qa_platform.models.domain.event_api_record import EventApiRecord
from apps.qa_platform.enumeration import AssertMethod

import urllib3

import time

import json
from json.decoder import JSONDecodeError

import re

import requests

from pydantic import Json

import jsonpath

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

    # 先找到字符串："{{ $.. ｜ 0 }}"
    # 将{{}}字符串去掉
    # 字符串从 ｜ 分割
    # 分割后的数组，索引0字符串前后去空格，索引1直接正则获取数字
    # 索引1找到对应节点，索引0捕捉元素

    # todo: 字典转字符串之后，出现异常未转回字典(已修复的异常，找个时间优化以更好的解决方式处理掉)
    """

    def replace_from_expression(self, replace_json_or_dict : Json):
        """
        1、找到所有表达式
            获取：${ $.. | 0 }
            ['${ $.. | 0 }', '${ $.. | 1 }' , '${ $.. | 2 }', '${ $.. | 3 }']
        2、循环表达式
        3、切割表达式
            ['"${ $.. ', ' 0 }"']
                正则获取指定的节点，表达式有问题则报表达式err
        4、找到指定节点
            1、不存在节点报err
            2、对应节点json反序列化
        5、指定节点找到对应参数
        6、替换
        """
        replace_json_or_dict = json.dumps(replace_json_or_dict)
        # 获取到${ $.. | 0 }
        # ['${ $.. | 0 }', '${ $.. | 1 }' , '${ $.. | 2 }', '${ $.. | 3 }']
        expression_with_index_list = re.findall('"\$\{.*?\}"', replace_json_or_dict.replace('\'','"'))

        if not expression_with_index_list:
            return json.loads(replace_json_or_dict)
        for i in range(len(expression_with_index_list)):
            # 分割成['"${ $.. ', ' 0 }"']
            expression_split_list = expression_with_index_list[i].split('|')
            if len(expression_split_list) < 2:
                self.case_node.err_record.append('表达式异常:%s'%expression_with_index_list[i])
                return json.loads(replace_json_or_dict)
            # 去掉最外层表达式并去空格
            # '"${ $.. '
            # '$..'
            expression = expression_split_list[0][3:].strip()
            # 只匹配数字，并且匹配1-2个字符
            # ' 0 }"'
            # '0'
            index_list = re.findall(r'(?![a-zA-Z])(\d{1,2})', expression_split_list[1])
            # 无匹配与多匹配则报错，比如 1111，则会匹配['11'，'11']
            if not index_list or len(index_list) > 1:
                self.case_node.err_record.append('表达式异常:%s'%expression_with_index_list[i])
                return json.loads(replace_json_or_dict)
            index = int(index_list[0])
            # 找到之前运行过的节点，这里的sort和排序规则和用例执行展示的排序规则不一样，生成测试套件时特地修改了sort
            try:
                response = EventApiRecord.objects.values(
                    'response'
                ).get(
                    result_id=self.case_node.result_id,
                    case_id=self.case_node.case_id,
                    data_id = self.case_node.data_id,
                    sort=index,
                    is_status=1, is_delete=0
                ).get('response')
            except EventApiRecord.DoesNotExist as e:
                self.case_node.err_record.append(
                    '表达式异常，查询不到response，result_id：%s，case_id：%s，data_id：%s，sort：%s，err：%s' % (
                        self.case_node.result_id, self.case_node.case_id,self.case_node.data_id, index ,e
                    )
                )
                return json.loads(replace_json_or_dict)
            else:
                try:
                    response_dict = json.loads(response.replace('\'', '"'))
                except JSONDecodeError as e:
                    self.case_node.err_record.append((self.__class__, e, '对应执行记录response非标准json，不支持参数化'))
                    return json.loads(replace_json_or_dict)
                else:
                    # 指定节点获取到对应需要替换的参数列表，只替换0
                    replace_new_data_list = jsonpath.jsonpath(response_dict, expression)
                    if not replace_new_data_list:
                        self.case_node.err_record.append('表达式异常，节点response的上没有\'参数化\'的数据')
                        return json.loads(replace_json_or_dict)
                    # 我的参数，对应表达式与对应节点的数据进行替换
                    # 场景：假如出现两个表达式获取的同一个节点的某个数据，第二次替换不到实际上无所谓，因为对应节点数据是一致的
                    # 字符串替换并将字符串转回字典
                    replace_json_or_dict = json.loads(
                        replace_json_or_dict.replace(
                            expression_with_index_list[i],
                            # 字典转json
                            json.dumps(replace_new_data_list[0], ensure_ascii=False)
                        )
                    )
        return replace_json_or_dict

    @print_func
    def handle(self, case_node : CaseApiNode):
        # 如果需要参数化则进入该判断
        if case_node.is_expression:
            self.case_node = case_node
            case_node.headers = self.replace_from_expression(self.case_node.headers)
            case_node.query = self.replace_from_expression(self.case_node.query)
            case_node.body = self.replace_from_expression(self.case_node.body)
        return self.successor.handle(case_node)

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

    @print_func
    def _get_func(self, key: str):
        """获取请求方法"""
        func = self._method_dict.get(key)
        if func is None:
            return func
        if isinstance(func, str):
            func = getattr(self, func)
        return func

    @print_func
    def _handle_context(self, case_node: CaseApiNode):
        case_node.headers['Content-Type'] = case_node.content_type
        self._reconnection_times = case_node.reconnection_times
        self._rest_reconnection_times = case_node.reconnection_times

    @print_func
    def _send(self, case_node : CaseApiNode):
        request_func = self._get_func(case_node.method)
        try:
            print(
                type(case_node.path),
                'url:%s'%case_node.path,
                type(case_node.query),
                'query:%s'%case_node.query,
                type(case_node.body),
                'body:%s'%case_node.body,
                type(case_node.headers),
                'headers:%s'%case_node.headers,
            )
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
            print(response)
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
            print(e)
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
    1、断言列表有数据，则断言，没有则跳过
    2、断言时要求必须的得能够反序列化json，否则报fails，添加到err_record
    场景：
        1、json响应
        2、非json响应（支持非json响应的数据，所以dto使用str存储）
    """

    @property
    def _assert_dict(self):
        return {
            AssertMethod.ASSERT_EQUAL.value: "_assert_equal",
            AssertMethod.ASSERT_NOT_EQUAL.value: '_assert_not_equal',
            AssertMethod.ASSERT_IN.value: '_assert_in',
            AssertMethod.ASSERT_NOT_IN.value: '_assert_not_in'
        }

    @print_func
    def _assert(self, func : str, first, second):
        # 根据设置的枚举选择并获取方法
        assert_func = self._get_assert_func(func)
        # 返回true或者false
        return assert_func(
            # 校验的对象转成字符串
            ('%s' % first).strip().replace('\'','"'),
            ('%s' % second).strip().replace('\'','"')
        )

    @print_func
    def _get_assert_func(self, func):
        """根据字典获取对应的方法"""
        asserter = self._assert_dict.get(func)
        if asserter is not None:
            if isinstance(asserter, str):
                asserter = getattr(self, asserter)
            return asserter
        # 不是统一数据类型返回默认验证方法
        return self._base_assert

    def _base_assert(self, first, second):
        """默认校验方法"""
        return False

    @print_func
    def _assert_equal(self, first : str, second : str):
        """判断值相等"""
        return first == second

    def _assert_not_equal(self, first : str, second : str):
        """判断值不想等"""
        return first != second

    def _assert_in(self, first : str, second : str):
        """判断包含"""
        return second in first

    def _assert_not_in(self, first : str, second : str):
        """判断不包含"""
        return second not in first

    @print_func
    def handle(self, case_node : CaseApiNode):
        # 如果没有校验点，则跳过
        if not case_node.assert_list:
            return self.successor.handle(case_node)
        try:
            response = json.loads(case_node.response)
        except JSONDecodeError as e:
            case_node.err_record.append((self.__class__, e))
            return self.successor.handle(case_node)
        except TypeError as e:
            case_node.err_record.append((self.__class__, e))
            return self.successor.handle(case_node)
        except Exception as e:
            case_node.err_record.append((self.__class__, e))
            return self.successor.handle(case_node)
        assert_iter = case_node.assert_list.__iter__()
        while True:
            try:
                assert_info : dict = assert_iter.__next__()
                assert_method = assert_info.get('assert_method')
                assert_obj = assert_info.get('assert_obj')
                assert_val = assert_info.get('assert_val')
                catch_list = jsonpath.jsonpath(
                    response, assert_obj
                )
                if not catch_list:
                    case_node.err_record.append('断言异常，未找到断言对象，表达式：%s'%assert_obj)
                    continue
                # todo：修改断言表达式，多个断言对象需要指定哪一个
                # 断言失败添加到报错中
                if not self._assert(assert_method, catch_list[0], assert_val):
                    case_node.err_record.append(
                        {
                            'assert_method': assert_method, 'assert_obj': catch_list[0], 'assert_val': assert_val
                        }
                    )

            except StopIteration:
                break
        return self.successor.handle(case_node)

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
        self.expression_handler = _ExpressionHandler()
        self.api_record_handler = _ApiRecordHandler()
        self.assert_handler = _AssertHandler()
        self.tear_down_handler = _TearDownHandler()

        self.set_up_handler.set_successor(self.expression_handler)
        self.expression_handler.set_successor(self.http_handler)
        self.http_handler.set_successor(self.assert_handler)
        self.assert_handler.set_successor(self.api_record_handler)
        self.api_record_handler.set_successor(self.tear_down_handler)

    @print_func
    def main(self, case_node : CaseApiNode):
        return self.set_up_handler.handle(case_node)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging, re, json, jsonpath

from apps.qa_platform.enumeration import CheckMethod

# 日志
runner_log = logging.getLogger('runner_log')


class CheckpointBuilder(object):
    """
    校验点建造者
    """

    log = runner_log

    def __init__(self):
        self.result = {
            'error_list': []
        }
        # 方法字典
        self._funcs_dict = {
            CheckMethod.ASSERT_EQUAL.value: "_assert_equal",
            CheckMethod.ASSERT_NOT_EQUAL.value: '_assert_not_equal',
            CheckMethod.ASSERT_IN.value: '_assert_in',
            CheckMethod.ASSERT_NOT_IN.value: '_assert_not_in'
        }

    def _error_record(self, *error_info):
        """
        异常流
        :param report_id:
        :param error_info:
        :return:
        """
        self.log.error('error_info：%s' % str(error_info))
        self.result.get('error_list', []).extend(error_info)

    def build(self, checkpoint_list, response):

        # 不存在校验点则不进入校验点逻辑
        if not checkpoint_list:
            return self.result

        # 非json数据不支持
        if not isinstance(response, dict):
            self._error_record('校验的响应参数不支持非json数据：%s' % response)
            return self.result

        # 处理response数据，字典转成json字符串
        try:
            response = json.dumps(response, ensure_ascii=False)
        except Exception as e:
            self._error_record('json序列化失败:响应参：{} & 错误：{}'.format(response, e))
            return self.result

        # 循环校验
        for check_info in checkpoint_list:
            jsonpath_expression = check_info.get('check_object')
            check_method = check_info.get('check_method')
            check_value = check_info.get('check_value')

            # todo：jsonpath_expression/check_method/check_value获取不到数据的

            catch_list = jsonpath.jsonpath(response, jsonpath_expression)
            # list为空则添加error
            if not catch_list:
                self._error_record('jsonpath表达式捕捉为空:表达式：{} & 捕捉结果：{}'.format(jsonpath_expression, catch_list))
            else:
                # 校验
                check_result = self._to_check(check_method, catch_list[0], check_value)
                # print(check_result)
                # 校验失败进入判断
                if not check_result:
                    self._error_record(
                        {'check_object': catch_list[0], 'check_method': check_method, 'check_value': check_value}
                    )
        return self.result

    def _to_check(self, func, first, second):
        # 根据设置的枚举选择并获取方法
        assertion_func = self._get_assert_func(func)
        # 校验的对象都转成字符串
        first, second = str(first).replace(' ', ''), str(second).replace(' ', '')
        # 返回true或者false
        return assertion_func(first, second)

    def _get_assert_func(self, func):
        """根据字典获取对应的方法"""
        asserter = self._funcs_dict.get(func)
        if asserter is not None:
            if isinstance(asserter, str):
                asserter = getattr(self, asserter)
            return asserter
        # 不是统一数据类型返回默认验证方法
        return self._base_assert_equal

    def _base_assert_equal(self, first, second):
        """默认校验方法"""
        if not first == second:
            self.result.get('error_list', []).append(self._base_assert_equal)

    def _assert_equal(self, first, second):
        """判断值相等"""
        return first == second

    def _assert_not_equal(self, first, second):
        """判断值不想等"""
        return first != second

    def _assert_in(self, first, second):
        """判断包含"""
        return second in first

    def _assert_not_in(self, first, second):
        """判断不包含"""
        return second not in first

# if __name__ == '__main__':
# check = CheckpointBuilder()

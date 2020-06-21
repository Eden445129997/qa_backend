#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging, re, jsonpath
from apps.test_platform.api_framework import factory

# 日志
runner_log = logging.getLogger('runner_log')


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
        self.result.get('error_list', []).extend(error_info)

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
                        self._error_record('不存在该表达式节点%s' % catch_list[i], e)
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

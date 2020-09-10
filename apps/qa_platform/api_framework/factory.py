#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform import models
# 序列化
from apps.common.serializers import query_set_list_serializers


class DataFactory(object):
    """
    测试用例数据工厂
    """

    def __init__(self):
        pass

    def get_query_set_case_list_by_plan_id(self, plan_id):
        """
        需求：新创建的在最后，支持排序
        创建默认sort为0
        倒序排序
        相同则用id升序
        :param plan_id:
        :return: query_set:[{case3},{case2},{case1},{case0},{case0}]
        """
        return models.TestCase.objects.filter(plan_id=plan_id).order_by('-sort').order_by('id')

    def get_case_detail_list_by_case_id(self, case_id):
        """
        需求：新创建的在最后，支持排序
        创建默认sort为0
        倒序排序
        相同则用id升序
        :param case_id:
        :return: query_set:[{case_detail3},{case_detail2},{case_detail1},{case_detail0},{case_detail0}]
        """
        query_set_case_detail_list = models.TestCaseModel.objects.filter(case_id=case_id).order_by('-sort').order_by('id')
        return query_set_list_serializers(query_set_case_detail_list)

    def get_interface_by_interface_id(self, interface_id):
        """
        根据interface_id获取interface的数据
        :param case_detail_id:
        :return: {interface}
        """
        return models.Interface.objects.values('api_name', 'method', 'path').get(id=interface_id)

    def get_report_detail_response_by_report_id_and_sort(self, report_id, sort):
        """
        根据报告id和排序id获取response（参数化业务）
        :param report_id:
        :param sort:
        :return:
        """
        # 模型获取出response的字典，再获取response键的值
        return models.ApiTestReportDetail.objects.values('response').get(report_id=report_id, sort=sort).get('response')

    def get_check_point_by_case_detail_id(self, case_detail_id):
        """
        根据用例节点id查询检查点
        :param case_detail_id:
        :return:
        """
        check_point_list = [checkpoint for checkpoint in models.CheckPoint.objects.values('case_detail_id','check_object','check_method','check_value').filter(case_detail_id=str(case_detail_id), status=1)]
        return check_point_list

class SuitFactory(object):
    """
    测试套件工厂
    """

    def __init__(self):
        # 测试套件
        self.test_suit = models.Suit()
        # 数据工厂对象
        self.data_factory = DataFactory()

    def get_suit_by_plan_id(self, plan_id):
        """
        根据计划id生成测试套件
        1、循环用例
        2、根据每个用例检索出对应节点，节点反查url，并且放入映射对象
        :param plan_id:
        :return: {'api_name': '查看个人/他人基本信息', 'method': 'POST', 'path': '/app-http/v104/user/getAppUserBasicInfo', 'case_id': '1', 'path_id': '156', 'reconnection_times': 3, 'wait_time': 10, 'input_header': '{}', 'input_parameter': '{}', 'mock_status': False, 'mock_response': '{}', 'text': None, 'checkpoint': '{}', 'case_sort': 0, 'status': True, 'create_time': '2020-06-03', 'update_time': datetime.datetime(2020, 6, 3, 1, 11, 53, tzinfo=<UTC>)}
        """

        # 获取case列表（query_set对象）
        query_set_case_list = self.data_factory.get_query_set_case_list_by_plan_id(plan_id)

        # 根据计划检索测试用例
        for case_id in query_set_case_list:
            # print(case_id)
            # 检索用例节点
            test_case_detail_list = self.data_factory.get_case_detail_list_by_case_id(case_id)
            # 补充接口数据和校验点数据
            for test_case_detail in test_case_detail_list:
                # print(test_case_detail)

                # 补充节点对应的接口数据
                interface_id = test_case_detail.get('interface_id')
                api_info = self.data_factory.get_interface_by_interface_id(interface_id)

                # 补充节点下的校验点
                id = test_case_detail.get('id')
                checkpoint_list = self.data_factory.get_check_point_by_case_detail_id(id)
                test_case_detail['checkpoint_list'] = checkpoint_list

                # print(api_info)
                # print(checkpoint_list)

                # 将接口数据，用例数据并在一起
                test_task = {**api_info, **test_case_detail}
                # print(test_task)
                self.test_suit.append(test_task)
        # print(self.test_suit)
        # print(type(self.test_suit[0]))
        return self.test_suit

    def get_suit_by_case_id(self, case_id):
        """
        根据用例id生产测试套件
        :param case_id:
        :return:
        """
        # 检索用例节点
        test_case_detail_list = self.data_factory.get_case_detail_list_by_case_id(case_id)
        # 补充接口数据和校验点数据
        for test_case_detail in test_case_detail_list:
            interface_id = test_case_detail.get('interface_id')
            # 反查接口数据
            api_info = self.data_factory.get_interface_by_interface_id(interface_id)

            # 补充节点下的校验点
            id = test_case_detail.get('id')
            checkpoint_list = self.data_factory.get_check_point_by_case_detail_id(id)
            test_case_detail['checkpoint_list'] = checkpoint_list

            # 将接口数据，用例数据并在一起
            test_task = {**api_info, **test_case_detail}
            self.test_suit.append(test_task)
        return self.test_suit

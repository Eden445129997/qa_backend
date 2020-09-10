#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from apps.qa_platform.api_framework import factory
from apps.qa_platform.enumeration import EventStatus
from apps.qa_platform import models

# 日志
runner_log = logging.getLogger('runner_log')


class ReportBuilder(object):
    """
    测试报告建造者
    """

    def __init__(self):
        self.data_factory = factory.DataFactory()
        self.task_status = None

    def build(self):
        pass

    def _set_status(self, status):
        self.task_status = status

    def wait_build_test_report(self, executor, host, total):
        """
        创建测试报告
        执行状态：等待中（枚举）
        :return:
        """
        try:
            api_test_report = models.EventStatus(executor=executor, host=host, total=total,
                                                   task_status=EventStatus.WAIT.value)
            api_test_report.save()
            self._set_status(EventStatus.WAIT.value)
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
            api_test_report.task_status = EventStatus.EXECUTION.value
            api_test_report.save()
            self._set_status(EventStatus.EXECUTION.value)

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

    def stop_buil_test_report(self, report_id, time_taken):
        """
        状态
        执行状态：完成任务（枚举）
        :return:
        """
        try:
            api_test_report = models.ApiTestReport.objects.get(id=report_id)
            api_test_report.task_status = EventStatus.FINISH.value
            api_test_report.time_taken = time_taken
            api_test_report.save()
            self._set_status(EventStatus.FINISH.value)

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
            api_test_report.task_status = EventStatus.FAILSE.value
            api_test_report.save()
            self._set_status(EventStatus.FAILSE.value)

        except Exception as e:
            runner_log.error(e)

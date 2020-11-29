#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)

from .qa_case import QaCase
from .api_case_data import ApiCaseData
from .event_api_result import EventApiResult

class EventApiRecord(BaseDoMain):
    """
    接口测试事件结果记录
    """
    # 外键关联报告id
    result = models.ForeignKey(
        EventApiResult, verbose_name="接口事件结果", db_column='result_id', on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    # 关联用例表
    case = models.ForeignKey(
        QaCase, verbose_name="测试用例", db_column='case_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )
    # 关联的tb_api_case_data : id
    data = models.ForeignKey(
        ApiCaseData, verbose_name="接口数据", on_delete=models.DO_NOTHING, db_column='data_id',
        related_name='+', db_constraint=False, default=1
    )
    # 接口别名
    api_name = models.CharField(verbose_name="接口名称", null=True, max_length=32)
    # 请求的url
    url = models.CharField(verbose_name="请求地址", null=True, max_length=128)
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    query = models.TextField(verbose_name="请求行入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # 响应参数
    response = models.TextField(verbose_name="响应参数", blank=True, null=True)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)
    # 失败次数
    fail_times = models.IntegerField(verbose_name="请求失败次数", null=True)
    # 是否mock，该历史记录是否使用mock
    is_mock = models.BooleanField(verbose_name="是否mock", default=False)
    # 排序顺序
    sort = models.IntegerField(verbose_name="用例排序顺序", default=0)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event_api_record"
        # django的admin界面的后台展示的数据
        verbose_name = "接口事件细节记录"
        verbose_name_plural = verbose_name


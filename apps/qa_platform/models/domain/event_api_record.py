#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class EventApiRecord(models.Model):
    """
    接口测试事件结果记录
    """
    id = models.AutoField(primary_key=True)
    # 外键关联报告id
    result_id = models.IntegerField(verbose_name='所属报告id')
    # 外键关联用例id
    case_id = models.IntegerField(verbose_name='所属用例id', blank=True, null=True)
    # 绑定的数据id
    data_id = models.IntegerField(verbose_name='所属数据id', blank=True, null=True)
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
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event_api_record"
        # django的admin界面的后台展示的数据
        verbose_name = "接口事件细节记录"
        verbose_name_plural = verbose_name
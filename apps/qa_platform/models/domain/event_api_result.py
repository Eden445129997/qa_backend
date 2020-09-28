#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class EventApiResult(models.Model):
    """
    接口测试事件结果
    """
    id = models.AutoField(primary_key=True)
    # 执行的域名
    host = models.CharField(verbose_name="执行的域名", max_length=64, null=True)
    # 执行用例总数
    total = models.IntegerField(verbose_name="用例执行总数", blank=True, null=True)
    # 接口测试结果
    current_status = models.CharField(verbose_name="接口测试结果", choices=EVENT_API_STUTAS, max_length=8)
    # 所用时间(s为单位)
    time_taken = models.CharField(verbose_name="执行使用时间", max_length=16, blank=True, null=True)
    # 测试套件的数据准备是否成功
    is_prepared = models.BooleanField(verbose_name="套件准备：0未准备 1已准备", default=False)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)
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
        db_table = "tb_event_api_result"
        verbose_name = "接口事件结果"
        verbose_name_plural = verbose_name
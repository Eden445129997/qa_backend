#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

class Event(BaseDoMain):
    """
    事件工单
    """
    id = models.AutoField(primary_key=True)
    # 业务开关（00000）类似二进制处理方式，0未处理，1已处理
    switch = models.CharField(verbose_name="业务字段（0为需要执行，1不需要处理）", max_length=16, null=True)
    # 事件数据（json存储）
    context = models.TextField(verbose_name="事件数据",default= "{}")
    # 当前执行次数
    current_times = models.IntegerField(verbose_name="最大执行次数", default=0)
    # 最大执行次数
    max_times = models.IntegerField(verbose_name="最大执行次数", default=3)
    # 事件描述
    text = models.CharField(verbose_name="事件备注", max_length=64, blank=True, null=True)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event"
        verbose_name = "事件表"
        verbose_name_plural = verbose_name
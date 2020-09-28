#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class Host(models.Model):
    """
    域名表
    """
    # 域名id
    id = models.AutoField(primary_key=True)
    # 外键—关联工程表
    project_id = models.IntegerField(verbose_name='所属项目id')
    # 环境名
    nickname = models.CharField(verbose_name='域名昵称', max_length=32)
    # host地址
    host = models.CharField(verbose_name='Host域名', max_length=64)
    # 环境描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)
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
        db_table = "tb_host"
        # django的admin界面的后台展示的数据
        verbose_name = "环境"
        verbose_name_plural = verbose_name
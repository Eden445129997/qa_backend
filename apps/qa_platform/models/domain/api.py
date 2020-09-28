#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class Api(models.Model):
    """
    接口表
    """
    # 接口id
    id = models.AutoField(primary_key=True)
    # 工程id
    project_id = models.IntegerField(verbose_name='所属项目id', blank=True, null=True)
    # 接口名称
    api_name = models.CharField(verbose_name="接口名称", max_length=32)
    # 解析方式
    content_type = models.CharField(verbose_name="http报文body序列化类型content_type", choices=HTTP_CONTENT_TYPE,
                                    max_length=128)
    # 请求方式—1、get2、post3、put4、delete
    method = models.CharField(verbose_name="请求方式", choices=REQUEST_METHOD, max_length=255)
    # 资源路径
    path = models.CharField(verbose_name="资源路径", max_length=128)
    # 接口描述
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
        db_table = "tb_api"
        # django的admin界面的后台展示的数据
        verbose_name = "接口"
        verbose_name_plural = verbose_name

    @classmethod
    def query_api_by_id(cls, api_id: int):
        """根据id获取api"""
        return cls.objects.values(
            'project_id', 'api_name', 'method', 'path', 'content_type'
        ).get(
            id=api_id, is_status=1, is_delete=0
        )
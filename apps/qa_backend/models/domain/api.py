#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals


from . import (
    models, BaseDoMain
)

from .project import (
    Project
)


from apps.qa_backend.enumeration import (
    HTTP_METHOD_TUPLE, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)


class Api(BaseDoMain):
    """
    接口表
    """
    # 工程id
    project = models.ForeignKey(
        to=Project, verbose_name="项目", db_column='project_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False, blank=True, null=True
    )
    # 接口名称
    api_name = models.CharField(verbose_name="接口名称", max_length=32)
    # 解析方式
    content_type = models.CharField(
        verbose_name="Content-type", choices=HTTP_CONTENT_TYPE,
        max_length=128
    )
    # 请求方式—1、get2、post3、put4、delete
    method = models.CharField(
        verbose_name="请求方式",
        choices=HTTP_METHOD_TUPLE,
        max_length=255)
    # 资源路径
    path = models.CharField(verbose_name="资源路径", max_length=128)

    objects = models.Manager()

    def __str__(self):
        return '%s: %s'%(self.api_name, self.path)

    class Meta:
        db_table = "tb_api"
        # django的admin界面的后台展示的数据
        verbose_name = "接口配置"
        verbose_name_plural = verbose_name

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

from .project import Project

class Host(BaseDoMain):
    """
    域名表
    """
    # 工程id
    project = models.ForeignKey(
        Project, db_column='project_id', on_delete=models.DO_NOTHING,
        db_constraint=False, blank=True, null=True
    )
    # 环境名
    nickname = models.CharField(verbose_name='域名昵称', max_length=32)
    # host地址
    host = models.CharField(verbose_name='Host域名', max_length=64)
    # 环境描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_host"
        # django的admin界面的后台展示的数据
        verbose_name = "环境"
        verbose_name_plural = verbose_name
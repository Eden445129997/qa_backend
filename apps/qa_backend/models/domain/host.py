#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)

from .project import Project


class Host(BaseDoMain):
    """
    域名表
    """
    # 工程id
    project = models.ForeignKey(
        Project, verbose_name="项目", db_column='project_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False, blank=True, null=True
    )
    # 环境名
    nickname = models.CharField(verbose_name='域名昵称', max_length=32)
    # host地址
    host = models.CharField(verbose_name='Host域名', max_length=64)

    objects = models.Manager()

    def __str__(self):
        return '%s: %s'%(self.nickname, self.host)

    class Meta:
        db_table = "tb_host"
        # django的admin界面的后台展示的数据
        verbose_name = "HOST配置"
        verbose_name_plural = verbose_name

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)


class Project(BaseDoMain):
    """
    工程表
    """
    # 工程名
    project_name = models.CharField(verbose_name="项目名", max_length=64)
    # 项目负责人
    project_leader = models.CharField("负责人", max_length=64)

    objects = models.Manager()

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = "tb_project"
        # django的admin界面的后台展示的数据
        verbose_name = "项目"
        verbose_name_plural = verbose_name


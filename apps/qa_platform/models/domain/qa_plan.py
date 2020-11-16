#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

from .project import Project

class QaPlan(BaseDoMain):
    """
    测试计划表
    """
    # 工程id
    project = models.ForeignKey(
        Project, db_column='project_id', on_delete=models.DO_NOTHING,
        db_constraint=False, blank=True, null=True
    )
    # 计划名称
    plan_name = models.CharField(verbose_name="测试计划", max_length=32)
    # 计划描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_qa_plan"
        # django的admin界面的后台展示的数据
        verbose_name = "测试计划"
        verbose_name_plural = verbose_name
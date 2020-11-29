#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)


from .project import Project

class QaPlan(BaseDoMain):
    """
    测试计划表
    """
    # 工程id
    project = models.ForeignKey(
        Project, verbose_name="项目", db_column='project_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False, blank=True, null=True
    )
    # 计划名称
    plan_name = models.CharField(verbose_name="测试计划", max_length=32)

    objects = models.Manager()

    def __str__(self):
        return self.plan_name

    class Meta:
        db_table = "tb_qa_plan"
        # django的admin界面的后台展示的数据
        verbose_name = "测试计划"
        verbose_name_plural = verbose_name

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models


from .qa_plan import QaPlan

# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

class QaCase(BaseDoMain):
    """
    测试用例表
    """
    # 用例id
    id = models.AutoField(primary_key=True)
    # 外键—关联计划表
    plan = models.ForeignKey(
        QaPlan, on_delete=models.DO_NOTHING, db_column='plan_id',
        db_constraint=False
    )
    # 用例名称
    case_name = models.CharField(verbose_name="用例名称", max_length=32)
    # 排序
    sort = models.IntegerField(verbose_name="排序", default=0)
    # 用例描述
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
        db_table = "tb_qa_case"
        # django的admin界面的后台展示的数据
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name

    @classmethod
    def query_qa_case_list(cls, plan_id: int):
        return cls.to_serialize(
            cls.objects
                .filter(
                plan_id=plan_id,
                is_status=1,
                is_delete=0
            )
                .order_by('-sort')
                .order_by('id')
        )
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class ApiAssert(models.Model):
    """
    断言
    """
    id = models.AutoField(primary_key=True)
    # 关联的tb_api_case_data : id
    data_id = models.IntegerField(verbose_name='所属数据id')
    # 关联的tb_api_case_model : id
    model_id = models.IntegerField(verbose_name='关联模型id')
    # 检查关系
    assert_method = models.CharField(verbose_name='校验方法', max_length=16, choices=CHECK_METHOD)
    # 检查对象（仅仅支持json校验）
    assert_obj = models.CharField(verbose_name='检查对象，jsonpath表达式', max_length=64)
    # 检查值
    assert_val = models.TextField(verbose_name="校验的比对值")
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
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
        db_table = "tb_api_assert"
        # django的admin界面的后台展示的数据
        verbose_name = "断言"
        verbose_name_plural = verbose_name

    @classmethod
    def get_api_assert_list_by_data_id(cls, data_id : int):
        return cls.objects.values(
            'data_id', 'model_id', 'assert_method', 'assert_obj', 'assert_val'
        ).filter(
            data_id=data_id,
            is_status=1,
            is_delete=0
        )
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

from .api_case_model import ApiCaseModel
from .api_case_data import ApiCaseData

from apps.qa_platform.enumeration import (
    CHECK_METHOD
)

class ApiAssert(BaseDoMain):
    """
    断言
    """
    id = models.AutoField(primary_key=True)
    # 关联的tb_api_case_model : id
    model = models.ForeignKey(
        ApiCaseModel, on_delete=models.DO_NOTHING, db_column='model_id',
        db_constraint=False
    )
    # 关联的tb_api_case_data : id
    data = models.ForeignKey(
        ApiCaseData, on_delete=models.DO_NOTHING, db_column='data_id',
        db_constraint=False
    )
    # 检查关系
    assert_method = models.CharField(verbose_name='校验方法', max_length=16, choices=CHECK_METHOD)
    # 检查对象（仅仅支持json校验）
    assert_obj = models.CharField(verbose_name='检查对象，jsonpath表达式', max_length=64)
    # 检查值
    assert_val = models.TextField(verbose_name="校验的比对值")
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_assert"
        # django的admin界面的后台展示的数据
        verbose_name = "断言"
        verbose_name_plural = verbose_name

    @classmethod
    def query_api_assert_list(cls, data_id : int) -> list:
        return cls.to_serialize(
            cls.objects.filter(
                data_id=data_id,
                is_status=1,
                is_delete=0
            )
        )
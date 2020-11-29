#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)

from .api_case_model import ApiCaseModel
from .api_case_data import ApiCaseData

from apps.qa_backend.enumeration import (
    CHECK_METHOD
)

class ApiAssert(BaseDoMain):
    """
    断言
    """
    id = models.AutoField(primary_key=True)
    # 关联的tb_api_case_model : id
    model = models.ForeignKey(
        ApiCaseModel, verbose_name="接口模型", on_delete=models.DO_NOTHING, db_column='model_id',
        related_name='+', db_constraint=False
    )
    # 关联的tb_api_case_data : id
    data = models.ForeignKey(
        ApiCaseData, verbose_name="接口数据", on_delete=models.DO_NOTHING, db_column='data_id',
        related_name='+', db_constraint=False
    )
    # 断言方法
    assert_method = models.CharField(verbose_name='断言', max_length=16, choices=CHECK_METHOD)
    # 断言对象（仅仅支持json校验）
    assert_obj = models.CharField(verbose_name='断言对象表达式', max_length=64)
    # 断言值
    assert_val = models.TextField(verbose_name="断言值")

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_assert"
        # django的admin界面的后台展示的数据
        verbose_name = "接口断言"
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

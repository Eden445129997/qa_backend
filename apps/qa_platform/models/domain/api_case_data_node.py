#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

class ApiCaseDataNode(BaseDoMain):
    # 用例模型id
    model = models.ForeignKey(
        verbose_name='关联模型id', to="ApiCaseModel", db_column='model_id', on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    # 关联用例数据表
    data = models.ForeignKey(
        verbose_name='所属数据id', to="ApiCaseData",  db_column='data_id', on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    query = models.TextField(verbose_name="请求行入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # mock状态（0 不启用mock，1启用mock）
    is_mock = models.BooleanField(verbose_name="mock状态（0 不启用mock，1启用mock）", default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock的返回值", default="{}")
    # 表达式状态
    is_expression = models.BooleanField(verbose_name="表达式状态：0 不启用jsonpath捕捉参数化\n 1 启用jsonpath捕捉参数化", default=False)
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_data_node"
        # django的admin界面的后台展示的数据
        verbose_name = "用例参数"
        verbose_name_plural = verbose_name

    @classmethod
    def query_case_api_data_node_list(cls,data_id: int) -> list:
        return cls.to_serialize(
            cls.objects.filter(
                data_id=data_id,
                is_status=1,
                is_delete=0
            )
        )
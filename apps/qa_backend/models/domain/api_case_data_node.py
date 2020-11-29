#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, HttpDoMain
)

from .api_case_model import ApiCaseModel
from .api_case_data import ApiCaseData

class ApiCaseDataNode(HttpDoMain):
    # 用例模型id
    model = models.ForeignKey(
        to=ApiCaseModel, verbose_name='接口模型', db_column='model_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )
    # 关联用例数据表
    data = models.ForeignKey(
        to=ApiCaseData, verbose_name='接口数据',  db_column='data_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_data_node"
        # django的admin界面的后台展示的数据
        verbose_name = "接口数据节点"
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


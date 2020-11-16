#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from apps.common.base_obj import BaseDoMain
from django.db import models

from .qa_case import QaCase
from .api import Api


from apps.common.serializers import query_set_list_serializers

class ApiCaseModel(BaseDoMain):
    """
    测试模型表(测试节点表)
    比如用例ABCDE，如果c启用mock，则写入mock返回值，c校验直接为True，并直接取mock里面的值
    """

    # 关联用例表
    case = models.ForeignKey(
        QaCase, db_column='case_id', on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    # 请求的path
    api = models.ForeignKey(
        Api, db_column='api_id', on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    # 重连次数
    reconnection_times = models.IntegerField(verbose_name="重连次数", default=3)
    # 超时设置
    timeout = models.IntegerField(verbose_name="最长等待时长", default=10)
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    query = models.TextField(verbose_name="请求头入参", default="{}")
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
    # 排序顺序
    sort = models.IntegerField(verbose_name="用例排序顺序", default=0)

    class Meta:
        db_table = "tb_api_case_model"
        # django的admin界面的后台展示的数据
        verbose_name = "用例模型"
        verbose_name_plural = verbose_name

    @classmethod
    def query_set_by_case_id(cls, case_id: int):
        """根据用例id获取接口用例模型列表"""
        return cls.objects.filter(
                case_id=case_id, is_status=1, is_delete=0
            ).order_by('-sort').order_by('id')


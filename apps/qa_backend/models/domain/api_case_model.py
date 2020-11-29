#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, HttpDoMain
)

from .qa_case import QaCase
from .api import Api


class ApiCaseModel(HttpDoMain):
    """
    测试模型表(测试节点表)
    比如用例ABCDE，如果c启用mock，则写入mock返回值，c校验直接为True，并直接取mock里面的值
    """

    # 关联用例表
    case = models.ForeignKey(
        QaCase, verbose_name="测试用例", db_column='case_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )
    # 请求的path
    api = models.ForeignKey(
        Api, verbose_name="接口", db_column='api_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )
    # 重连次数
    reconnection_times = models.IntegerField(verbose_name="重连次数", default=3)
    # 超时设置
    timeout = models.IntegerField(verbose_name="最长等待时长", default=10)
    # 排序顺序
    sort = models.IntegerField(verbose_name="模型排序顺序", default=0)

    def __str__(self):
        return '%s - %s'%(self.case, self.api)

    class Meta:
        db_table = "tb_api_case_model"
        # django的admin界面的后台展示的数据
        verbose_name = "接口模型"
        verbose_name_plural = verbose_name

    @classmethod
    def query_set_by_case_id(cls, case_id: int):
        """根据用例id获取接口用例模型列表"""
        return cls.objects.filter(
                case_id=case_id, is_status=1, is_delete=0
            ).order_by('-sort', 'id')



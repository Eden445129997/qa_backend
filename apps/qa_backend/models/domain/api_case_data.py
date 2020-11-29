#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from . import (
    models, BaseDoMain
)

from .qa_case import QaCase

class ApiCaseData(BaseDoMain):
    # 关联用例表
    case = models.ForeignKey(
        QaCase, verbose_name="测试用例", db_column='case_id', on_delete=models.DO_NOTHING,
        related_name='+', db_constraint=False
    )

    objects = models.Manager()

    def __str__(self):
        return '%s: %s'%(self.case, self.text)

    class Meta:
        db_table = "tb_api_case_data"
        # django的admin界面的后台展示的数据
        verbose_name = "接口数据"
        verbose_name_plural = verbose_name

    @classmethod
    def query_api_case_data_list(cls, case_id: int) -> list:
        return cls.to_serialize(
            cls.objects.filter(
                case_id=case_id,
                is_status=1,
                is_delete=0
            )
        )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from collections import Iterable

class BaseDoMain(models.Model):
    """数据库表模型基类"""
    id = models.AutoField(primary_key=True)
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
        abstract=True
        # 索引
        # indexes = []
        # 联合索引
        # index_together
        # 联合唯一索引
        # unique_together

    @classmethod
    def to_serialize(cls, query_set: object or models.Model) -> list:
        serializer_list = []
        # 当 query_set 为 model
        if not isinstance(query_set, Iterable):
            query_set = [query_set]
        # query_set 为 query_set的时候
        for model in query_set:
            model_dict = model.__dict__
            del model_dict['_state']
            serializer_list.append(model_dict)
        # from django.core import serializers
        # serialize_obj = serializers.serialize("python", query_set)
        return serializer_list


class BaseHandler(object):
    """责任链模式基类"""
    def set_successor(self, successor):
        self.successor = successor
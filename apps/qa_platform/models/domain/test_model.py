#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models
# 自定义模型视图
from apps.common.views import CustomModelViewSet

from rest_framework import serializers


class A(models.Model):
    """
    接口表
    """
    # 接口id
    id = models.AutoField(primary_key=True)
    # 接口名称
    name = models.CharField(verbose_name="接口名称", max_length=32)

    objects = models.Manager()

    class Meta:
        db_table = "tb_A"

class B(models.Model):
    """
    接口表
    """
    # 接口id
    id = models.AutoField(primary_key=True)
    a = models.ForeignKey("A", on_delete=models.DO_NOTHING, db_column='test', db_constraint=False)

    objects = models.Manager()

    class Meta:
        db_table = "tb_B"

class ASerializer(serializers.ModelSerializer):
    """工程表"""
    class Meta:
        model = A
        fields = "__all__"

class BSerializer(serializers.ModelSerializer):
    """工程表"""
    class Meta:
        model = B
        fields = "__all__"

class AViews(CustomModelViewSet):
    """测试用例"""
    queryset = A.objects.all()
    serializer_class = ASerializer

class BViews(CustomModelViewSet):
    """测试用例"""
    queryset = A.objects.all()
    serializer_class = BSerializer

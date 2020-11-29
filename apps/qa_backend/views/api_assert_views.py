#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import api_assert
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class ApiAssertViews(BaseModelViewSet):
    """接口校验点表"""
    queryset = api_assert.ApiAssert.objects.all()
    serializer_class = serializers.ApiAssertSerializer

    # 精确匹配
    # assert_method、model_id、data_id
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import api_case_model
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class ApiCaseModelViews(CustomModelViewSet):
    """测试模型表"""
    queryset = api_case_model.ApiCaseModel.objects.all()
    serializer_class = serializers.ApiCaseModelSerializer

    # 排序
    ordering = ('-sort', 'id')

    # 精确匹配
    # model_id、data_id
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import api_case_data
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class ApiCaseDataViews(CustomModelViewSet):
    """接口数据表"""
    queryset = api_case_data.ApiCaseData.objects.all()
    serializer_class = serializers.ApiCaseDataSerializer

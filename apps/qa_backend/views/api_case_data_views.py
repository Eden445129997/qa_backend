#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import api_case_data
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class ApiCaseDataViews(BaseModelViewSet):
    """接口数据表"""
    queryset = api_case_data.ApiCaseData.objects.all()
    serializer_class = serializers.ApiCaseDataSerializer

    # 精确匹配
    # case_id、is_status
    search_fields = ('text',)
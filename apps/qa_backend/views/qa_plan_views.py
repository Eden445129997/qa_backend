#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status

# 模型
from apps.qa_backend.models.domain import qa_plan
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

# 序列化
from apps.common.response import JsonResponse


class QaPlanViews(BaseModelViewSet):
    """测试计划表"""
    queryset = qa_plan.QaPlan.objects.all()
    serializer_class = serializers.QaPlanSerializer

    # 精确匹配
    # project_id,is_status
    # 模糊查询字段
    search_fields = ('plan_name',)

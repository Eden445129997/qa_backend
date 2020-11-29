#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status
# 过滤器(字段过滤)
from django_filters.rest_framework import DjangoFilterBackend
# drf SearchFilter模糊查询、OrderingFilter排序过滤器
from rest_framework.filters import (
    SearchFilter, OrderingFilter
)

# 模型
from apps.qa_backend.models.domain import project
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

from apps.common.response import JsonResponse
# http请求的类
from django.http.request import HttpRequest


class ProjectViews(BaseModelViewSet):
    """工程表"""
    queryset = project.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter,]
    # 自定义精确查询字段
    filter_fields = '__all__'
    # 模糊查询字段
    search_fields = ('project_name',)
    # 默认排序
    ordering = ('-create_time', 'id')
    # 自定义排序字段
    ordering_fields = '__all__'


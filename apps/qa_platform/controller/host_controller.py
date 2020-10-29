#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import host
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class HostViews(CustomModelViewSet):
    """域名表"""
    queryset = host.Host.objects.all()
    serializer_class = serializers.HostSerializer

    # 精确匹配
    # project_id
    # 模糊匹配
    search_fields = ('nickname', 'host',)
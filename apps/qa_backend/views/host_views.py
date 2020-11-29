#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import host
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class HostViews(BaseModelViewSet):
    """域名表"""
    queryset = host.Host.objects.all()
    serializer_class = serializers.HostSerializer

    # 精确匹配
    # project_id
    # 模糊匹配
    search_fields = ('nickname', 'host',)
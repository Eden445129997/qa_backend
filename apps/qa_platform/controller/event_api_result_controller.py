#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class EventApiResultViews(CustomModelViewSet):
    """接口事件结果"""
    queryset = domain.EventApiResult.objects.all()
    serializer_class = serializers.EventApiResultSerializer

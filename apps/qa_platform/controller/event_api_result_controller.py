#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import event_api_result
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class EventApiResultViews(CustomModelViewSet):
    """接口事件结果"""
    queryset = event_api_result.EventApiResult.objects.all()
    serializer_class = serializers.EventApiResultSerializer

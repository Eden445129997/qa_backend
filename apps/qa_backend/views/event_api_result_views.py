#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import event_api_result
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class EventApiResultViews(BaseModelViewSet):
    """接口事件结果"""
    queryset = event_api_result.EventApiResult.objects.all()
    serializer_class = serializers.EventApiResultSerializer

    # 精确匹配
    # is_status、is_prepared、current_status
    search_fields = ('host',)
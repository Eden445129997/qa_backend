#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import event_api_record
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class EventApiRecordViews(BaseModelViewSet):
    """接口事件记录"""
    queryset = event_api_record.EventApiRecord.objects.all()
    serializer_class = serializers.EventApiRecordSerializer

    # 精确匹配
    # result_id、case_id、data_id
    search_fields = ('url',)
    ordering = ('sort')
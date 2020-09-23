#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def query_api_by_id(api_id : int):
    """根据id获取api"""
    return domain.Api.objects.values(
        'project_id','api_name', 'method', 'path', 'content_type'
    ).get(
        id=api_id, is_status=1, is_delete=0
    )
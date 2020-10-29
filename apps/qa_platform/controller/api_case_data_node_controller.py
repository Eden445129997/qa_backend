#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import api_case_data_node
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class ApiCaseDataNodeViews(CustomModelViewSet):
    """接口数据节点表"""
    queryset = api_case_data_node.ApiCaseDataNode.objects.all()
    serializer_class = serializers.ApiCaseDataNodeSerializer

    # 排序
    ordering = ('-sort', 'id')

    # 精确匹配
    # model_id、data_id
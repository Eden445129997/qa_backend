#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_backend.models.domain import api_case_data_node
# 自定义模型视图
from apps.common.base_obj import BaseModelViewSet
# 序列化
from apps.qa_backend import serializers

class ApiCaseDataNodeViews(BaseModelViewSet):
    """接口数据节点表"""
    queryset = api_case_data_node.ApiCaseDataNode.objects.all()
    serializer_class = serializers.ApiCaseDataNodeSerializer

    # 排序
    ordering = ('-sort', 'id')

    # 精确匹配
    # model_id、data_id
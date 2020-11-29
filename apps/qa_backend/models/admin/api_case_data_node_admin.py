#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.api_case_data_node import (
     ApiCaseDataNode
)

@register(ApiCaseDataNode)
class ApiCaseDataNodeAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'id',
        'model',
        'data',
        'headers',
        'query',
        'body',
        'is_mock',
        'mock_response',
        'is_expression',
    ] + BaseAdmin.list_display
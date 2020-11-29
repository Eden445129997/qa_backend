#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.api_case_model import (
     ApiCaseModel
)

@register(ApiCaseModel)
class ApiCaseModelAdmin(BaseAdmin):
    list_filter = BaseAdmin.list_filter
    date_hierarchy = 'create_time'
    # 展示列表
    list_display = [
        'id',
        'case',
        'api',
        'headers',
        'query',
        'body',
        'is_mock',
        'mock_response',
        'is_expression',
        'sort',
        'reconnection_times',
        'timeout',
    ] + BaseAdmin.list_display

    # 编辑页中的只读字段
    readonly_fields = ['sort'] + BaseAdmin.readonly_fields
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.api_case_data import (
     ApiCaseData
)

@register(ApiCaseData)
class ApiCaseDataAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'id',
        'case',
        'text'
    ] + BaseAdmin.list_display
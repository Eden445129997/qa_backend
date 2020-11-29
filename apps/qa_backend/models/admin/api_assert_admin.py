#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.api_assert import (
     ApiAssert
)

@register(ApiAssert)
class ApiAssertAdmin(BaseAdmin):
    """展示列表"""
    list_display = [
        'id',
        'model',
        'data',
        'assert_method',
        'assert_obj',
        'assert_val'
    ] + BaseAdmin.list_display
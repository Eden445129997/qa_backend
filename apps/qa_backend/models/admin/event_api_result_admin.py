#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.event_api_result import (
     EventApiResult
)

@register(EventApiResult)
class EventApiResultAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'id',
        'host',
        'current_status',
        'total',
        'time_taken',
        'is_prepared',
        'err_record',
    ] + BaseAdmin.list_display
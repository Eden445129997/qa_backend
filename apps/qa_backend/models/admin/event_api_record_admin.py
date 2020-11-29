#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.event_api_record import (
     EventApiRecord
)

@register(EventApiRecord)
class EventApiRecordAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'result',
        'case',
        'data',
        'api_name',
        'url',
        'headers',
        'query',
        'body',
        'response',
        'err_record',
        'fail_times',
        'is_mock',
        'sort',
    ] + BaseAdmin.list_display
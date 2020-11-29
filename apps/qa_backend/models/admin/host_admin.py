#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.host import (
     Host
)

@register(Host)
class HostAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'id', 'project', 'nickname', 'host'
    ] + BaseAdmin.list_display
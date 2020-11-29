#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.qa_plan import (
     QaPlan
)

@register(QaPlan)
class QaPlanAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'project',
        'plan_name'
    ] + BaseAdmin.list_display
    pass

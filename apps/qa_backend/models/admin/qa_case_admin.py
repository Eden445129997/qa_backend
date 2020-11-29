#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包

# 跨包导入
from ..domain.qa_case import (
     QaCase
)

@register(QaCase)
class QaCaseAdmin(BaseAdmin):
    # 展示列表
    list_display = [
        'id',
        'plan',
        'case_name',
        'sort'
    ] + BaseAdmin.list_display
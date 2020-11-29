#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)
# 从当前子包
from .api_admin import ApiInline

# 跨包导入
from ..domain.project import (
     Project
)

class ProjectInline(BaseStackedInline):
    model = Project


@register(Project)
class ProjectAdmin(BaseAdmin):

    inlines = [ ApiInline, ]

    # 不展示的字段
    exclude = []
    # 展示列表
    list_display = [
        'id', 'project_name', 'project_leader'
    ] + BaseAdmin.list_display

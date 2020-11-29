#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从当前父包
from . import (
    BaseAdmin, BaseTabularInline, BaseStackedInline, register
)

# 跨包
from ..domain.api import (
    Api
)


class ApiInline(BaseStackedInline):
    model = Api
    extra = 0
    can_delete = False

@register(Api)
class ApiAdmin(BaseAdmin):

    # 关联模型
    # inlines = [ ProjectInline, ]

    # 多个字段、模糊查询(pk为主键)
    search_fields = ('api_name', 'path')
    # 精确检索
    list_filter = BaseAdmin.list_filter + ['method', 'project', 'content_type', 'create_time', 'update_time']
    # 指定外键的查询（当model存在多个外键的时候，会每个数据的多个外键进行查询，非常消耗系统资源）
    list_select_related = ('project',)
    # exclude = ['project', 'project_id'] + BaseAdmin.exclude
    # 展示列表
    # list_display = BaseAdmin.get_list_display_from_model(Api, exclude)
    list_display = [
        'id',
        'api_name',
        'project',
        'method',
        'content_type',
        'path',
    ] + BaseAdmin.list_display
    # 修改外键编辑样式字段
    # raw_id_fields = ("project",)

    actions = ['to_link']

    def to_link(self, request, queryset):
        print(111)
        pass
    #     for i in queryset:
    #         print(i.__dict__)
    #     from django.utils.html import format_html
    #     from django.utils.html import mark_safe

    # def get_action(self, action):

    to_link.short_description = '操作'

    # 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    to_link.action_type = 1
    to_link.action_url = 'http://www.baidu.com'

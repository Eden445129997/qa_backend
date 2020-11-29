#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from collections import Iterable

from django.db import models
from django.contrib import admin
from rest_framework import serializers

# 视图类相关
from rest_framework import viewsets  # , views
# 过滤器(字段过滤)
from django_filters.rest_framework import DjangoFilterBackend
# drf SearchFilter模糊查询、OrderingFilter排序过滤器
from rest_framework.filters import (
    SearchFilter, OrderingFilter
)

ID = 'id'
TEXT = 'text'
IS_STATUS = 'is_status'
IS_DELETE = 'is_delete'
CREATE_TIME = 'create_time'
UPDATE_TIME = 'update_time'

class BaseDoMain(models.Model):
    """数据库表模型基类"""
    id = models.AutoField(verbose_name="ID", db_column=ID.upper(), primary_key=True)
    # 描述
    text = models.CharField(verbose_name="描述", db_column=TEXT, blank=True, default='', max_length=64)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态", db_column=IS_STATUS, default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除", db_column=IS_DELETE, default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', db_column=CREATE_TIME, auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', db_column=UPDATE_TIME, auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True
        # 索引
        # indexes = []
        # 联合索引
        # index_together
        # 联合唯一索引
        # unique_together

    @classmethod
    def to_serialize(cls, query_set: object or models.Model) -> list:
        serializer_list = []
        # 当 query_set 为 model
        if not isinstance(query_set, Iterable):
            query_set = [query_set]
        # query_set 为 query_set的时候
        for model in query_set:
            model_dict = model.__dict__
            del model_dict['_state']
            serializer_list.append(model_dict)
        return serializer_list

class HttpDoMain(BaseDoMain):
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    query = models.TextField(verbose_name="查询字符串", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体", default="{}")
    # mock状态（0 不启用mock，1启用mock）
    is_mock = models.BooleanField(verbose_name="是否mock", default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock响应", default="{}")
    # 表达式状态
    is_expression = models.BooleanField(verbose_name="是否使用参数化", default=False)

    class Meta:
        abstract = True


class ListPageConf(admin.ModelAdmin):
    """django后台管理的列表页配置类"""

    """列表页等功能按钮"""
    # 可搜索字段(pk为主键, 模糊查询)
    # search_fields = (ID,)
    # 精确搜索
    list_filter = [ID,]
    # 详细时间分层筛选
    date_hierarchy = 'create_time'

    """列表相关"""
    # 是否展示count所有数据(一定要False)
    show_full_result_count = False
    # 列表展示的字段
    list_display = [IS_STATUS, CREATE_TIME, 'edit_model']
    # 可跳转对应页面的链接
    list_display_links = ['edit_model']
    # 外键的查询
    # list_select_related = ()
    # 操作按钮
    # actions = []
    # 排除字段(不在列表和表单页展示字段)
    exclude = [IS_DELETE, UPDATE_TIME,]
    # 列表页可编辑字段
    # list_editable = []
    # 分页，每页显示条数
    list_per_page = 10
    # 分页,显示全部,真是数据小于该值时才会显示全部
    list_max_show_all = 10
    # 排序
    ordering = ('-%s'%CREATE_TIME, ID)
    # 默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态。将preserve_filters设为False后，则会返回未过滤状态。
    preserve_filters = True

    def edit_model(self, model):
        """给列表页新增操作字段"""
        return '编辑'

    edit_model.short_description = '操作'


class EditPageConf(admin.ModelAdmin):
    """django后台管理的model详情页配置类"""

    """编辑页相关"""
    # 详情页可编辑展示字段
    # fields = ()
    # 编辑页中的只读字段
    readonly_fields = [CREATE_TIME, UPDATE_TIME]
    # 修改外键编辑样式字段
    # raw_id_fields = (,)
    # 保存后仍然在新的编辑页中
    # save_as = True
    # True点击保存并新增按钮会跳转编辑页，False跳转到列表页面（只针对sava_as=True时生效）
    # save_as_continue = False

    def view_on_site(self, model):
        """编辑页右上角的跳转按钮"""
        # print(model._meta.app_label)
        # return 'http://www.baidu.com'
        # return '/admin/qa_backend/api/2/change/'
        return '/admin/{}/'.format(model._meta.app_label)


class BaseAdmin(ListPageConf, EditPageConf):
    """django后台管理的基类"""

    # 定制保存操作
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(BaseAdmin, self).save_model(request, obj, form, change)

    # 定制加载列表
    def get_queryset(self, request):
        """列表页 逻辑删除 权限判断"""
        # todo：用户权限判断
        queryset = super().get_queryset(request).filter(is_delete=False)
        # 权限判断
        # if request.user.is_superuser:
        #     return queryset
        # return queryset.filter(author=request.user)
        return queryset

    # 定制搜索功能
    # def get_search_results(self, request, queryset, search_term):
    #     pass

    def delete_model(self, request, model):
        """详情页 逻辑删除"""
        model.is_delete = True
        model.save()

    def delete_queryset(self, request, queryset):
        """列表页 定制逻辑删除"""
        # queryset.delete()
        queryset.update(is_delete=True)

    # 定制actions操作（列表页的功能按钮）
    # def get_actions(self, request):
    #     """重写action"""
    #     actions = super(BaseAdmin, self).get_actions(request)
    #     if ...:
    #         # 如果满足一定条件，则删除某个响应或者添加某个响应
    #         del actions['action name']
    #         actions.add('another action')
    #     # 返回经过处理的actions
    #     return actions

    @classmethod
    def get_list_display_from_model(
            cls,
            model: object,
            exclude: list = False
    ) -> list:
        """获取模型的所有的字段列表"""
        if not exclude:
            exclude = []
        return [
            str(field)
            for field in model._meta._forward_fields_map.keys()
            if field not in exclude
        ]

def batch_enable(modeladmin, request, queryset) -> None:
    """批量启用"""
    count = queryset.count()
    queryset.update(is_status=True)
    modeladmin.message_user(request, '成功 - 启用 {} 条数据'.format(count))

def batch_disable(modeladmin, request, queryset) -> None:
    """批量不启用"""
    count = queryset.count()
    queryset.update(is_status=False)
    modeladmin.message_user(request, '成功 - 不启用 {} 条数据'.format(count))

batch_enable.short_description = '启用'
batch_disable.short_description = '禁用'
# icon
# batch_enable.icon = batch_disable.icon = 'fas fa-audio-description'
# 底色
# batch_enable.type = batch_disable.type = 'danger'
# 字体类型
# batch_enable.style = batch_disable.style = 'color:black;'
admin.site.add_action(batch_enable, 'enable')
admin.site.add_action(batch_disable, 'disable')

class BaseInline():
    """django admin自定义拓展内联基类"""
    # 展示标题
    # verbose_name = ('接口配置')
    # verbose_name_plural = ('接口配置')

    # 定义展示的字段和顺序（默认不写按照admin展示）
    # fields = (  )
    # 只读字段
    readonly_fields = (CREATE_TIME, UPDATE_TIME)
    # 删除
    can_delete = False

    # def has_add_permission(self, request, obj=None):
    #     """ 不允许这个inline类增加记录 (当然也增加不了，readonly_fileds中定义的字段，在增加时无法输入内容) """
    #     return False

    # def get_queryset(self, request):
    #     """ 重写这个方法 不显示任何的Note模型的记录，这个类就只允许添加相关的数据，不是用来展示数据的 """
    #     queryset = super().get_queryset(request)
    #     return queryset.none()


class BaseTabularInline(BaseInline, admin.TabularInline):
    """横的内联"""
    extra = 0
    pass


class BaseStackedInline(BaseInline, admin.StackedInline):
    """竖的内联"""
    pass


class BaseSerializer(serializers.ModelSerializer):
    """序列化基类"""
    create_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    # 1.外键值显示对应的全部值
    # depth = 1  # 显示关系表层数(1表示显示到2层),外键值显示对应的全部值
    # 2.外键值只显示部份值,可序列化也可返序列化,在models.py中用方法重写字段.
    depth = 2


class BaseModelViewSet(viewsets.ModelViewSet):
    """
    自定义viewSet类
        1、配置组件
        2、统一响应格式（暂无法解决）

    这里面查看需要重写的属性与方法
    from rest_framework import generics

    get_queryset(): 从类属性queryset中获取model的queryset数据
    get_object(): 从类属性queryset中获取model的queryset数据, 在通过有名分组pk确定唯一对象
    get_serializer(): 从类属性serializer_class中获取的serializer的序列化类
    """

    # 配置过滤器类
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    # 自定义精确查询字段
    filter_fields = '__all__'
    # 自定义排序字段
    ordering_fields = '__all__'
    # 模糊查询字段
    #     lookup_prefixes = {
    #          ^以指定内容开头
    #         '^': 'istartswith',
    #          =完全匹配
    #         '=': 'iexact',
    #          @全文搜索(目前只支持django数据存放在mysql)
    #         '@': 'search',
    #          $正则匹配
    #         '$': 'iregex',
    #     }
    # search_fields = ('case_name', 'id')
    # 默认排序
    ordering = ('-%s'%CREATE_TIME, ID)


class BaseHandler(object):
    """责任链模式基类"""

    def set_successor(self, successor):
        self.successor = successor


# def admin_url(model):
#     app_label = model._meta.app_label
#     model_name = model._meta.__name__lower

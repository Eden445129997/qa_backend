#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import viewsets, views
# 过滤器(字段过滤)
from django_filters.rest_framework import DjangoFilterBackend
# drf SearchFilter模糊查询、OrderingFilter排序过滤器
from rest_framework.filters import (
    SearchFilter, OrderingFilter
)

# 这里面查看需要重写的属性与方法
# from rest_framework import generics

class CustomModelViewSet(viewsets.ModelViewSet):
    """
    自定义viewSet类
        1、配置组件
        2、统一响应格式（暂无法解决）
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
    ordering = ('-create_time', 'id')


'''

from rest_framework import status
from apps.common.response import JsonResponse
# http请求的类
from django.http.request import HttpRequest

    def create(self, request : HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(data=serializer.data, msg="success", code=status.HTTP_201_CREATED)

    def list(self, request : HttpRequest, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, msg="success")

    def retrieve(self, request : HttpRequest, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, msg="success")

    def update(self, request : HttpRequest, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return JsonResponse(data=serializer.data, msg="success", code=status.HTTP_200_OK)

    def destroy(self, request : HttpRequest, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse(data=[], code=status.HTTP_200_OK, msg="delete resource success")
'''
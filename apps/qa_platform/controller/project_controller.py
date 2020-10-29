#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status
# 过滤器(字段过滤)
from django_filters.rest_framework import DjangoFilterBackend
# drf SearchFilter模糊查询、OrderingFilter排序过滤器
from rest_framework.filters import (
    SearchFilter, OrderingFilter
)

# 模型
from apps.qa_platform.models.domain import project
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.response import JsonResponse
# http请求的类
from django.http.request import HttpRequest


class ProjectViews(CustomModelViewSet):
    """工程表"""
    queryset = project.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter,]
    # 自定义精确查询字段
    filter_fields = '__all__'
    # 模糊查询字段
    search_fields = ('project_name',)
    # 默认排序
    ordering = ('-create_time', 'id')
    # 自定义排序字段
    ordering_fields = '__all__'

class QueryProjectByName(APIView):
    """根据项目名获取数据，返回数组"""

    def get(self, request : HttpRequest, *args, **kwargs):
        keyword_key = 'keyword'

        # 判空
        if keyword_key in request.GET.dict():
            keyword = str(request.GET['keyword'])
            # print(keyword)
            project_list = project.Project.objects.filter(project_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(data=project_list, msg="success",
                                code=status.HTTP_200_OK)
        else:
            return JsonResponse(data=[], msg="success",
                                code=status.HTTP_400_BAD_REQUEST)

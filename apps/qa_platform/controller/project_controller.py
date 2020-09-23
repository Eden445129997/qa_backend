#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status

# 模型
from apps.qa_platform.models import domain
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
    queryset = domain.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class QueryProjectByName(APIView):
    """根据项目名获取数据，返回数组"""

    def get(self, request : HttpRequest, *args, **kwargs):
        keyword_key = 'keyword'

        # 判空
        if keyword_key in request.GET.dict():
            keyword = str(request.GET['keyword'])
            # print(keyword)
            project_list = domain.Project.objects.filter(project_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(data=project_list, msg="success",
                                code=status.HTTP_200_OK)
        else:
            return JsonResponse(data=[], msg="success",
                                code=status.HTTP_400_BAD_REQUEST)

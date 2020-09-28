#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status

# 模型
from apps.qa_platform.models.domain import qa_plan
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.response import JsonResponse


class QaPlanViews(CustomModelViewSet):
    """测试计划表"""
    queryset = qa_plan.QaPlan.objects.all()
    serializer_class = serializers.QaPlanSerializer


class QueryQaPlanByName(APIView):
    """根据计划名获取数据，返回数组"""

    def get(self, request, *args, **kwargs):
        keywordKey = 'keyword'

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = qa_plan.QaPlan.objects.filter(plan_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(data=project_list, msg="success",
                                code=status.HTTP_200_OK)
        else:
            return JsonResponse(data=[], msg="success",
                                code=status.HTTP_400_BAD_REQUEST)

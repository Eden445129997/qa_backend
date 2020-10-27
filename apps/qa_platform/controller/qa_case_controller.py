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
# from apps.qa_platform.models.domain.qa_case import QaCase
# from apps.qa_platform.models.domain.api_case_model import QaCase
# from apps.qa_platform.models.domain.api_case_data import QaCase

from apps.qa_platform.models.domain import (
    qa_case, api_case_model, api_case_data
)
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.response import JsonResponse


class QaCaseViews(CustomModelViewSet):
    """测试用例"""
    queryset = qa_case.QaCase.objects.all()
    serializer_class = serializers.QaCaseSerializer

    # 模糊查询字段
    search_fields = ('case_name', 'id')
    # 排序
    ordering = ('-sort', 'id')

class QueryQaCaseByName(APIView):
    """根据测试用例名称获取数据，返回数组"""

    def get(self, request, *args, **kwargs):
        keywordKey = 'keyword'

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = qa_case.QaCase.objects.filter(case_name__icontains=keyword).order_by('-create_time').order_by('id')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(data=project_list, msg="success",
                                code=status.HTTP_200_OK)
        else:
            return JsonResponse(data=[], msg="参数错误",
                                code=status.HTTP_400_BAD_REQUEST)

class CaseApiAutoAdd(APIView):
    """自动添加测试用例"""
    def post(self, request, *args, **kwargs):
        body = request.META.get('BODY')
        plan_id = body.get('plan_id')
        api_order = body.get('api_order')
        is_prepare = body.get('is_prepare')
        print(body)
        if not isinstance(api_order ,list) or not plan_id:
            return JsonResponse(data={}, msg="参数错误",
                                code=status.HTTP_400_BAD_REQUEST)
        for i in api_order:
            if not isinstance(i, int):
                return JsonResponse(data={}, msg="参数错误",
                                    code=status.HTTP_400_BAD_REQUEST)
        if not is_prepare:
            is_prepare = 0

        model_list = []

        case = qa_case.QaCase(
            plan_id = plan_id,
            case_name = '自动添加用例'
        )
        case.save()
        if is_prepare:
            model = api_case_model.ApiCaseModel(
                case_id=case.id,
                api_id=1,
                is_mock=True,
                text='自动添加模型：数据准备节点'
            )
            model.save()
            model_list.append(model.id)
        for api_id in api_order:
            model = api_case_model.ApiCaseModel(
                case_id=case.id,
                api_id=api_id
            )
            model.save()
            model_list.append(model.id)
        case_data = api_case_data.ApiCaseData(
            case_id=case.id
        )
        case_data.save()
        return JsonResponse(data={
            "case_id": case.id,
            "model_list": model_list,
            "data_id": case_data.id
        }, msg="success",code=status.HTTP_200_OK)
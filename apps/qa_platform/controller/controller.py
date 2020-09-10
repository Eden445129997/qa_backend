#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# django原生自带的View类
from django.views import View
# django原生前后端分离，返回Json
from django.http import JsonResponse  # ,HttpResponse
# django原生sql
# from django.db import connection
# drf状态码
from rest_framework import status
from pydantic import ValidationError

# 模型
from apps.qa_platform.service.event_api_suit_service import *
from apps.qa_platform.service.event_api_result_service import *
from apps.qa_platform.models import domain
# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.views import CustomModelViewSet
from apps.common.single import db

import json

# import collections

# 数据库的单例连接
conner = db()

# drf框架的视图类（viewsets.Model类似基于restful风格的视图集—get/post/put/delete）
# from rest_framework import viewsets
from apps.qa_platform import serializers


class ProjectViews(CustomModelViewSet):
    """工程表"""
    queryset = domain.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class HostViews(CustomModelViewSet):
    """域名表"""
    queryset = domain.Host.objects.all()
    serializer_class = serializers.HostSerializer


class ApiViews(CustomModelViewSet):
    """接口表"""
    queryset = domain.Api.objects.all()
    serializer_class = serializers.ApiSerializer


class QaPlanViews(CustomModelViewSet):
    """测试计划表"""
    queryset = domain.QaPlan.objects.all()
    serializer_class = serializers.QaPlanSerializer


class QaCaseViews(CustomModelViewSet):
    """测试用例"""
    queryset = domain.QaCase.objects.all()
    serializer_class = serializers.QaCaseSerializer


class ApiCaseModelViews(CustomModelViewSet):
    """测试模型表"""
    queryset = domain.ApiCaseModel.objects.all()
    serializer_class = serializers.ApiCaseModelSerializer


class ApiCaseDataViews(CustomModelViewSet):
    """测试数据表"""
    queryset = domain.ApiCaseData.objects.all()
    serializer_class = serializers.ApiCaseDataSerializer


class ApiCaseDataNodeViews(CustomModelViewSet):
    """测试数据节点表"""
    queryset = domain.ApiCaseDataNode.objects.all()
    serializer_class = serializers.ApiCaseDataNodeSerializer


class ApiAssertViews(CustomModelViewSet):
    """测试数据节点表"""
    queryset = domain.ApiAssert.objects.all()
    serializer_class = serializers.ApiAssertSerializer


class EventViews(CustomModelViewSet):
    """接口测试任务报告"""
    queryset = domain.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventApiRecordViews(CustomModelViewSet):
    """接口测试报告细节"""
    queryset = domain.EventApiRecord.objects.all()
    serializer_class = serializers.EventApiRecordSerializer


class Test(View):
    def post(self, request, *args, **kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        # print("aaaa")
        return JsonResponse({"code": 200, "data": "success,this is django CBV post request"}, safe=False)


class Login(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"token": "Django token", "routers": ["*"]}, status=status.HTTP_200_OK)


class Logout(View):
    def post(self, request, *args, **kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        return JsonResponse({"code": 200, "data": {"token": "Django token", "routers": ["*"]}}, safe=False)


class RunTestPlanById(View):
    def post(self, request, *args, **kwargs):
        """
        :param request: {id,host,headers}
        :return:
        """
        request_body = bytes.decode(request.body)
        # print(request_body)
        plan_dict = json.loads(request_body)

        try:
            context = Context(**plan_dict)
            # test_model = domain.ApiCaseDataNode.objects.all()
            # print(test_model.query)
            task_runner = EventApiResultThread(context)
            task_runner.start()
            return JsonResponse(context.dict(), safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        except ValidationError:
            return JsonResponse(plan_dict, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)

class GetProjectByName(View):
    """根据项目名获取数据，返回数组"""

    def get(self, request, *args, **kwargs):
        keyword_key = 'keyword'
        # print(request.META)
        # print(request.META.get('PATH_INFO'))
        # print(request.META.get('REQUEST_METHOD'))
        # print(request.META.get('QUERY_STRING'))
        # print(request.META.get('CONTENT_TYPE'))

        # 判空
        if keyword_key in request.GET.dict():
            keyword = str(request.GET['keyword'])
            # print(keyword)
            project_list = domain.Project.objects.filter(project_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)


class GetTestPlanByName(View):
    """根据计划名获取数据，返回数组"""

    def get(self, request, *args, **kwargs):
        keywordKey = 'keyword'
        # print(request.META)
        # print(request.GET.dict())

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = domain.TestPlan.objects.filter(plan_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)


class GetTestCaseByName(View):
    """根据测试用例名称获取数据，返回数组"""

    def get(self, request, *args, **kwargs):
        keywordKey = 'keyword'
        # print(request.META)
        # print(request.GET.dict())

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = domain.TestCase.objects.filter(case_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)

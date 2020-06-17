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

# 模型
from apps.test_platform import models
from apps.test_platform.api_framework.factory import SuitFactory
from apps.test_platform.api_framework.director import TaskDirector

# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.single import db

import json
# import collections

# 数据库的单例连接
conner = db()

# drf框架的视图类（viewsets.ModelViewSet类似基于restful风格的视图集—get/post/put/delete）
from rest_framework import viewsets
# from apps.common.views import viewsets.ModelViewSet
from apps.test_platform import serializers


class ProjectViews(viewsets.ModelViewSet):
    """工程表"""
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class HostViews(viewsets.ModelViewSet):
    """域名表"""
    queryset = models.Host.objects.all()
    serializer_class = serializers.HostSerializer


class BusiModelViews(viewsets.ModelViewSet):
    """业务划分成模块表"""
    queryset = models.BusiModel.objects.all()
    serializer_class = serializers.BusiModelSerializer


class InterfaceViews(viewsets.ModelViewSet):
    """接口表"""
    queryset = models.Interface.objects.all()
    serializer_class = serializers.InterfaceSerializer


class TestPlanViews(viewsets.ModelViewSet):
    """测试计划表"""
    queryset = models.Interface.objects.all()
    serializer_class = serializers.TestPlanSerializer


class TestCaseViews(viewsets.ModelViewSet):
    """测试用例"""
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer


class TestCaseDetailViews(viewsets.ModelViewSet):
    """测试细节表(测试参数表)"""
    queryset = models.TestCaseDetail.objects.all()
    serializer_class = serializers.TestCaseDetailSerializer


class ApiTestReportViews(viewsets.ModelViewSet):
    """接口测试任务报告"""
    queryset = models.ApiTestReport.objects.all()
    serializer_class = serializers.ApiTestReportSerializer


class ApiTestReportDetailViews(viewsets.ModelViewSet):
    """接口测试报告细节"""
    queryset = models.ApiTestReportDetail.objects.all()
    serializer_class = serializers.ApiTestReportDetailSerializer


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
        plan_dict = json.loads(request_body)

        plan_id = plan_dict.get('id', None)
        host = plan_dict.get('host', None)
        headers = plan_dict.get('headers', {})

        if plan_id:
            # 测试套件工厂，根据生产测试套件
            suit_factory = SuitFactory()
            suit = suit_factory.get_suit_by_plan_id(plan_id)
            # print(test_suit)
            # 指挥者，执行任务(多线程)
            task_director = TaskDirector(suit=suit, host=host, headers=headers)
            task_director.start()
            return JsonResponse(plan_dict, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({}, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)


class RunTestCaseById(View):
    def post(self, request, *args, **kwargs):

        request_body = bytes.decode(request.body)
        case_dict = json.loads(request_body)

        case_id = case_dict.get('id', None)
        host = case_dict.get('host', None)
        headers = case_dict.get('headers', {})

        if case_id:
            # 测试套件工厂，根据生产测试套件
            suit_factory = SuitFactory()
            suit = suit_factory.get_suit_by_case_id(case_id)
            # 指挥者，执行任务(多线程)
            task_director = TaskDirector(suit=suit, host=host, headers=headers)
            task_director.start()
            return JsonResponse(case_dict, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({}, safe=False, json_dumps_params={'ensure_ascii': False},
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
            project_list = models.TestPlan.objects.filter(plan_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False},
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
            project_list = models.Project.objects.filter(project_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_list_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False},
                                status=status.HTTP_400_BAD_REQUEST)

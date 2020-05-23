# from django.shortcuts import render

# 模板对象
from apps.test_platform import models

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


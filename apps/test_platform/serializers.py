from rest_framework import serializers
from apps.test_platform import models


class ProjectSerializer(serializers.ModelSerializer):
    """工程表"""
    class Meta:
        model = models.Project
        fields = "__all__"

class HostSerializer(serializers.ModelSerializer):
    """域名表"""
    class Meta:
        model = models.Host
        fields = "__all__"

class BusiModelSerializer(serializers.ModelSerializer):
    """业务划分成模块表"""
    class Meta:
        model = models.BusiModel
        fields = "__all__"

class InterfaceSerializer(serializers.ModelSerializer):
    """接口表"""
    class Meta:
        model = models.Interface
        fields = "__all__"

class TestPlanSerializer(serializers.ModelSerializer):
    """测试计划表"""
    class Meta:
        model = models.TestPlan
        fields = "__all__"

class TestCaseSerializer(serializers.ModelSerializer):
    """测试用例表"""
    class Meta:
        model = models.TestCase
        fields = "__all__"

class TestCaseDetailSerializer(serializers.ModelSerializer):
    """测试细节表(测试参数表)"""
    class Meta:
        model = models.TestCaseDetail
        fields = "__all__"

class ApiTestReportSerializer(serializers.ModelSerializer):
    """接口测试任务报告"""
    class Meta:
        model = models.ApiTestReport
        fields = "__all__"

class ApiTestReportDetailSerializer(serializers.ModelSerializer):
    """接口测试报告细节"""
    class Meta:
        model = models.ApiTestReport
        fields = "__all__"


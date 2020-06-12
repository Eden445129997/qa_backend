from django.urls import path
# from django.http import HttpResponse
from .controller import drf_controller,d_controller

# 使用viewset时使用的路由
from rest_framework.routers import DefaultRouter

# 将rest_framework实现的viewset也添加django的路由中
urlpatterns = [
    path('login/',d_controller.Login.as_view(),name='登录demo，获取token'),
    path('logout/',d_controller.Logout.as_view(),name='退出登录demo，清除token'),
    path('test/',d_controller.Test.as_view(),name='测试回调'),
    path('getProjectByName/',d_controller.GetProjectByName.as_view(),name='根据project_name获取project'),
    path('getTestPlanByName/', d_controller.GetTestPlanByName.as_view(), name='根据plan_name获取project'),
    path('runTestPlanById/', d_controller.RunTestPlanById.as_view(), name='根据测试计划id执行测试'),
    path('runTestCaseById/', d_controller.RunTestCaseById.as_view(), name='根据测试用例id执行测试')
]

# Viewset视图集
router = DefaultRouter()
router.register("ProjectViews", drf_controller.ProjectViews, basename="ProjectViews")
router.register("HostViews", drf_controller.HostViews, basename="HostViews")
router.register("BusiModelViews", drf_controller.BusiModelViews, basename="BusiModelViews")
router.register("InterfaceViews", drf_controller.InterfaceViews, basename="InterfaceViews")
router.register("TestPlanViews", drf_controller.TestPlanViews, basename="TestPlanViews")
router.register("TestCaseViews", drf_controller.TestCaseViews, basename="TestCaseViews")
router.register("TestCaseDetailViews", drf_controller.TestCaseDetailViews, basename="TestCaseDetailViews")
router.register("ApiTestReportViews", drf_controller.ApiTestReportViews, basename="ApiTestReportViews")
router.register("ApiTestReportDetailViews", drf_controller.ApiTestReportDetailViews, basename="ApiTestReportDetailViews")

# 视图集导入到url路由dict中
urlpatterns += router.urls

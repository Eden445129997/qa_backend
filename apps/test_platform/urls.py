from django.urls import path
# from django.http import HttpResponse
from . import controller

# 使用viewset时使用的路由
from rest_framework.routers import DefaultRouter

# 将rest_framework实现的viewset也添加django的路由中
urlpatterns = [
    path('login/', controller.Login.as_view(), name='登录demo，获取token'),
    path('logout/', controller.Logout.as_view(), name='退出登录demo，清除token'),
    path('test/', controller.Test.as_view(), name='测试回调'),
    path('getProjectByName/', controller.GetProjectByName.as_view(), name='根据project_name获取project'),
    path('getTestPlanByName/', controller.GetTestPlanByName.as_view(), name='根据plan_name获取plan'),
    path('getTestCaseByName/', controller.GetTestCaseByName.as_view(), name='根据case_name获取case'),
    path('runTestPlanById/', controller.RunTestPlanById.as_view(), name='根据测试计划id执行测试'),
    path('runTestCaseById/', controller.RunTestCaseById.as_view(), name='根据测试用例id执行测试')
]

# Viewset视图集
router = DefaultRouter()
router.register("project", controller.ProjectViews, basename="project")
router.register("host", controller.HostViews, basename="host")
router.register("busiModel", controller.BusiModelViews, basename="busiModel")
router.register("interface", controller.InterfaceViews, basename="interface")
router.register("testPlan", controller.TestPlanViews, basename="testPlan")
router.register("testCase", controller.TestCaseViews, basename="testCase")
router.register("testCaseDetail", controller.TestCaseDetailViews, basename="testCaseDetail")
router.register("apiTestReport", controller.ApiTestReportViews, basename="apiTestReport")
router.register("apiTestReportDetail", controller.ApiTestReportDetailViews, basename="apiTestReportDetail")

# 视图集导入到url路由dict中
urlpatterns += router.urls

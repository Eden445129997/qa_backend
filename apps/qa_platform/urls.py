from django.urls import path
# from django.http import HttpResponse
from .controller import controller

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
]

# Viewset视图集
router = DefaultRouter()
router.register("project", controller.ProjectViews, basename="project")
router.register("host", controller.HostViews, basename="host")
router.register("api", controller.ApiViews, basename="api")
router.register("qaPlan", controller.QaPlanViews, basename="qaPlan")
router.register("qaCase", controller.QaCaseViews, basename="qaCase")
router.register("apiCaseModel", controller.ApiCaseModelViews, basename="apiCaseModel")
router.register("apiCaseData", controller.ApiCaseDataViews, basename="apiCaseData")
router.register("apiCaseDataNode", controller.ApiCaseDataNodeViews, basename="apiCaseDataNode")
router.register("apiAssert", controller.ApiAssertViews, basename="apiAssert")
router.register("event", controller.EventViews, basename="event")
router.register("eventApiRecord", controller.EventApiRecordViews, basename="eventApiRecord")

# 视图集导入到url路由list中
urlpatterns += router.urls

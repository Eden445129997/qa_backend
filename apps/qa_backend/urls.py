from django.urls import path
# from django.http import HttpResponse

# 使用viewset时使用的路由
from rest_framework.routers import DefaultRouter

from .views import (
    controller,
    project_views,
    host_views,
    qa_plan_views,
    qa_case_views,
    api_views,
    event_views,
    event_api_result_views,
    event_api_record_views,
    api_case_model_views,
    api_case_data_views,
    api_case_data_node_views,
    api_assert_views,
)
# AutoAddCaseApi
# 将rest_framework实现的viewset也添加django的路由中
urlpatterns = [
    path('login/', controller.Login.as_view(), name='登录demo，获取token'),
    path('logout/', controller.Logout.as_view(), name='退出登录demo，清除token'),
    path('event/api/run/', event_views.HandleEvent.as_view(), name='处理event'),
    path('qaCase/api/autoadd/', qa_case_views.CaseApiAutoAdd.as_view(), name='自动添加接口用例'),
]

# Viewset视图集
router = DefaultRouter()

router.register("project", project_views.ProjectViews, basename="project")
router.register("host", host_views.HostViews, basename="host")
router.register("api", api_views.ApiViews, basename="api")
router.register("qaPlan", qa_plan_views.QaPlanViews, basename="qaPlan")
router.register("qaCase", qa_case_views.QaCaseViews, basename="qaCase")
router.register("event", event_views.EventViews, basename="event")
router.register("eventApiResult", event_api_result_views.EventApiResultViews, basename="eventApiResult")
router.register("eventApiRecord", event_api_record_views.EventApiRecordViews, basename="eventApiRecord")
router.register("apiCaseModel", api_case_model_views.ApiCaseModelViews, basename="apiCaseModel")
router.register("apiCaseData", api_case_data_views.ApiCaseDataViews, basename="apiCaseData")
router.register("apiCaseDataNode", api_case_data_node_views.ApiCaseDataNodeViews, basename="apiCaseDataNode")
router.register("apiAssert", api_assert_views.ApiAssertViews, basename="apiAssert")

# 视图集导入到url路由list中
urlpatterns += router.urls

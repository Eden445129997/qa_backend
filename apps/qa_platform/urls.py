from django.urls import path
# from django.http import HttpResponse

# 使用viewset时使用的路由
from rest_framework.routers import DefaultRouter

from .models.domain.test_model import *

from .controller import (
    controller,
    project_controller,
    host_controller,
    qa_plan_controller,
    qa_case_controller,
    api_controller,
    event_controller,
    event_api_result_controller,
    event_api_record_controller,
    api_case_model_controller,
    api_case_data_controller,
    api_case_data_node_controller,
    api_assert_controller,
)
# AutoAddCaseApi
# 将rest_framework实现的viewset也添加django的路由中
urlpatterns = [
    path('login/', controller.Login.as_view(), name='登录demo，获取token'),
    path('logout/', controller.Logout.as_view(), name='退出登录demo，清除token'),
    path('queryProjectByName/', project_controller.QueryProjectByName.as_view(), name='根据project_name获取project'),
    path('queryQaPlanByName/', qa_plan_controller.QueryQaPlanByName.as_view(), name='根据plan_name获取plan'),
    path('queryQaCaseByName/', qa_case_controller.QueryQaCaseByName.as_view(), name='根据case_name获取case'),
    path('event/api/run/', event_controller.HandleEvent.as_view(), name='处理event'),
    path('qaCase/api/autoadd/', qa_case_controller.CaseApiAutoAdd.as_view(), name='自动添加接口用例'),
]

# Viewset视图集
router = DefaultRouter()
router.register("a", AViews, basename="a")
router.register("b", BViews, basename="b")

router.register("project", project_controller.ProjectViews, basename="project")
router.register("host", host_controller.HostViews, basename="host")
router.register("api", api_controller.ApiViews, basename="api")
router.register("qaPlan", qa_plan_controller.QaPlanViews, basename="qaPlan")
router.register("qaCase", qa_case_controller.QaCaseViews, basename="qaCase")
router.register("event", event_controller.EventViews, basename="event")
router.register("eventApiResult", event_api_result_controller.EventApiResultViews, basename="eventApiResult")
router.register("eventApiRecord", event_api_record_controller.EventApiRecordViews, basename="eventApiRecord")
router.register("apiCaseModel", api_case_model_controller.ApiCaseModelViews, basename="apiCaseModel")
router.register("apiCaseData", api_case_data_controller.ApiCaseDataViews, basename="apiCaseData")
router.register("apiCaseDataNode", api_case_data_node_controller.ApiCaseDataNodeViews, basename="apiCaseDataNode")
router.register("apiAssert", api_assert_controller.ApiAssertViews, basename="apiAssert")

# 视图集导入到url路由list中
urlpatterns += router.urls

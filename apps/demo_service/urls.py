from django.urls import path
# from django.http import HttpResponse
from . import views

# 使用viewset时使用的路由
from rest_framework.routers import DefaultRouter


# 将rest_framework实现的viewset也添加django的路由中
urlpatterns = [
    # 基于restful规范实现的原生django接口
    path('django/',views.DemoCBV.as_view(),name='django CBV restful API'),
    path('drf/view/',views.DrfView.as_view(),name='rest_framework CBV restful API'),
    path('relationQuery/', views.RelationQuery.as_view(), name='关联查询'),
]

# Viewset视图集
router = DefaultRouter()
router.register("drf/viewset",views.DrfViewset,basename="viewset")
urlpatterns += router.urls
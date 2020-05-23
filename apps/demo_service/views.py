# 前后端不分离，render：返回html页面
# from django.shortcuts import render

# 模板对象
from apps.demo_service import models

# django原生自带的View类
from django.views import View
# django原生前后端分离，返回Json
from django.http import JsonResponse

# 方式1：增删改查
# drf框架的视图类（viewsets类似基于restful风格的视图集—get/post/put/delete）
from rest_framework import viewsets
from .serializers import DemoSerializer

# 方式2：自定义
# drf框架的自定义视图
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

# django实现cbv（class base view）方式
class DemoCBV(View):
    def get(self,request,*args,**kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        return JsonResponse("success,this is django CBV get request",safe=False)

    def post(self,request,*args,**kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        return JsonResponse("success,this is django CBV post request",safe=False)

# 使用rest_framework实现基于restful风格的get/post/put/delete......
class DrfViewset(viewsets.ModelViewSet):
    # objects.all()方法必须得让model加入方法objects = models.Manager()
    queryset = models.DemoModel.objects.all()#
    serializer_class = DemoSerializer

# 使用rest_framwork实现基于restful风格的接口（自定义）
class DrfView(views.APIView):
    def get(self,request):
        DemoModel = models.DemoModel.objects.all()
        serializer = DemoSerializer(DemoModel, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DemoSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# django原生自带的View类
from django.views import View
# django原生前后端分离，返回Json
from django.http import JsonResponse
# django原生sql
# from django.db import connection
# drf状态码
from rest_framework import status

# 模型
from apps.test_platform import models
# 序列化
from apps.common.serializers import query_set_serializers


class Test(View):
    def post(self,request,*args,**kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        # print("aaaa")
        return JsonResponse({"code":200,"data":"success,this is django CBV post request"},safe=False)

class Login(View):
    def get(self,request,*args,**kwargs):
        return JsonResponse({"token":"Django token","routers":["*"]},status=status.HTTP_200_OK)

# class Logout(controller.APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"token":"Django token","routers":["*"]},status=status.HTTP_200_OK)
#
#     # 不被允许post请求，不知道为啥
#     def post(self,request,*args,**kwargs):
#         return Response({"token":"Django token","routers":["*"]},status=status.HTTP_200_OK)

class Logout(View):
    def post(self,request,*args,**kwargs):
        # safe参数默认为True，返回的必须是字典类型，否则报错
        return JsonResponse({"code":200,"data":{"token":"Django token","routers":["*"]}},safe=False)

class GetTestPlanByName(View):
    """根据计划名获取数据，返回数组"""
    def get(self,request,*args,**kwargs):
        keywordKey = 'keyword'
        # print(request.GET.dict())

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = models.TestPlan.objects.filter(plan_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)

class GetProjectByName(View):
    """根据项目名获取数据，返回数组"""
    def get(self,request,*args,**kwargs):
        keywordKey = 'keyword'
        # print(request.GET.dict())

        # 判空
        if keywordKey in request.GET.dict():
            keyword = str(request.GET['keyword'])
            project_list = models.Project.objects.filter(project_name__icontains=keyword).order_by('-create_time')
            # print(project_list.query)
            project_list = query_set_serializers(project_list)

            # safe参数默认为True，返回的必须是字典类型，否则报错
            return JsonResponse(project_list, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse([], safe=False, status=status.HTTP_400_BAD_REQUEST)


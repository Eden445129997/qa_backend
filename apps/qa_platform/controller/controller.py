#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# django原生前后端分离，返回Json
# from django.http import JsonResponse  # ,HttpResponse
# django原生sql
# from django.db import connection

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status
# drf响应
# from rest_framework.response import Response

# 模型
from apps.qa_platform.service.event_api_suit_service import *
from apps.qa_platform.service.event_api_result_service import *
from apps.qa_platform.models import domain
# 序列化
from apps.common.serializers import query_set_list_serializers
from apps.common.response import JsonResponse
# http请求的类
from django.http.request import HttpRequest


from apps.common.single import db

import json

# import collections

# 数据库的单例连接
conner = db()

# class Login(View):
#     def get(self, request : HttpRequest, *args, **kwargs):
#         return JsonResponse({"token": "Django token", "routers": ["*"]}, status=status.HTTP_200_OK)

class Login(APIView):
    def get(self, request : HttpRequest, *args, **kwargs):
        return JsonResponse(data={"token": "Django token", "routers": ["*"]}, msg="success", code=status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request : HttpRequest, *args, **kwargs):
        return JsonResponse(data={"token": "Django token", "routers": ["*"]}, msg="success", code=status.HTTP_200_OK)

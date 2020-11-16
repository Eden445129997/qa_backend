#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from rest_framework.serializers import ValidationError


# 模型
from apps.qa_platform.models.domain import event
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

# 模型
from apps.qa_platform.service.event_api_suit_service import *
from apps.qa_platform.service.event_api_result_service import *
from apps.qa_platform.models import domain
# 序列化
# from apps.common.response import JsonResponse
from rest_framework.response import Response

# http请求的类
from django.http.request import HttpRequest
# from django.http.response import JsonResponse


class EventViews(CustomModelViewSet):
    """事件表"""
    queryset = event.Event.objects.all()
    serializer_class = serializers.EventSerializer


class HandleEvent(APIView):
    def post(self, request : HttpRequest, *args, **kwargs):
        """
        :param request: {case_id or plan_id,host,headers}
        :return:
        """

        body = JSONParser().parse(request)
        try:
            context = Context(**body)
        except ValidationError as e:
            return Response(data=body, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            task_runner = EventApiResultThread(context)
            task_runner.start()
            return Response(data=context.dict())

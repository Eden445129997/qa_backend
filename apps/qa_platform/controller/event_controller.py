#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# drf接口继承类
from rest_framework.views import APIView
# drf状态码
from rest_framework import status
# 模型
from apps.qa_platform.models import domain
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

# 模型
from apps.qa_platform.service.event_api_suit_service import *
from apps.qa_platform.service.event_api_result_service import *
from apps.qa_platform.models import domain
# 序列化
from apps.common.response import JsonResponse

# http请求的类
from django.http.request import HttpRequest
# from django.http.response import JsonResponse


class EventViews(CustomModelViewSet):
    """事件表"""
    queryset = domain.Event.objects.all()
    serializer_class = serializers.EventSerializer


class HandleEvent(APIView):
    def post(self, request : HttpRequest, *args, **kwargs):
        """
        :param request: {case_id or plan_id,host,headers}
        :return:
        """
        body = request.META.get('BODY')

        try:
            context = Context(**body)
        except ValidationError as e:
            return JsonResponse(data=body, msg="%s"%e,
                                code=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(data=body, msg="%s"%e,
                                code=status.HTTP_400_BAD_REQUEST)
        else:
            task_runner = EventApiResultThread(context)
            task_runner.start()
            return JsonResponse(data=context.dict(), msg="success", code=status.HTTP_200_OK)

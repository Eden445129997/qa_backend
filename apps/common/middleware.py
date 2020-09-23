#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import json

import logging

from json.decoder import JSONDecodeError

# from django.urls import reverse
# deprecation.MiddlewareMixin是 Django 目前版本中用来兼容老版本代码的措施
from django.utils.deprecation import MiddlewareMixin

# http请求的类
from django.http.request import HttpRequest
from django.http.response import JsonResponse

# 日志
http_log = logging.getLogger('http')

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request : HttpRequest):
        """
        Middleware 中时进入的第1个方法
        一般做用户登录或者 HTTP 是否有认证头之类的验证
        """
        self.start_time = time.time()

        try:
            if 'application/json' in request.content_type:
                # 二进制转码
                # request_body = bytes.decode(request.body)
                request.META['BODY'] = json.loads(request.body)

        except JSONDecodeError:
            http_log.error(
                'request.META:%s\n'
                'request.path:%s\n'
                'request.method:%s\n'
                'request.content_type:%s\n'
                'request.body:%s\n'%(
                    request.META,
                    request.path,
                    request.method,
                    request.content_type,
                    request.body
                )
            )


    def process_view(self, request : HttpRequest, func, *args, **kwargs):
        """
        这个方法是在 process_request 方法之后执行的， 参数上面代码所示，其中 func 就是我们将要执行的 view 方法
        统计调用 View 所消耗的时间
        """
        # if request.path != reverse('index'):
        #     return None
        pass

    def process_exception(self,request : HttpRequest, exception):
        """
        可以在这里做 它的返回值跟 process_reques 样，是 HttpResponse 或者
        None ，其逻辑也一样 如果返回 None ，那么 django 会帮你执行 view 函数，从而得到
        最终的 response
        """
        pass

    def process_template_response(self, request : HttpRequest, response):
        """
        执行完上面的方法，并且 Django 帮我们执行 view
        拿到最终的 respons 后，如果使用了模板的 response（这是指通过 return render (request : HttpRequest, ' index. html ', con text= ｛｝）方式返回的 respons ），
        """
        return response


    def process_response(self, request : HttpRequest, response : JsonResponse):
        """
        当所有流程都处理完毕后，就来到了这个方法 这个方法的逻辑
        process_template_response 是完全一样的 ，只是后者是针对带有模板 response的处理
        """
        # if request.method == 'POST' and 'application/json' not in request.content_type:

        print(type(response))
        print(response)
        print(type(response.content))
        print(response.content)
        return response
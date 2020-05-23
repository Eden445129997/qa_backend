from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.controller import

# 这个类主要的作用就是重写rest_framework的viewset类的没有返回code的弊端（前端开发不好做判断处理）

class ReturnMsg:
    def __init__(self,code=1,msg="success",errors=None,data=None):
        self.code = code
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = data if data is None else data

    def dict(self):
        return {
            "code": self.code,
            "msg": self.msg,
            "errors": self.errors,
            "data": self.data
        }

class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        print("create")
        return Response(ReturnMsg(data=response.data).dict(),status=response.status_code)
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        print("retrieve")
        return Response(ReturnMsg(data=response.data).dict(),status=response.status_code)
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        print("update")
        return Response(ReturnMsg(data=response.data).dict(),status=response.status_code)
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        print("destroy")
        return Response(ReturnMsg(data=response.data).dict(),status=response.status_code)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print("list")
        return Response(ReturnMsg(data=response.data).dict(),status=response.status_code)


# 配置REST_FRAMEWORK的settings.py中的DEFAULTS字典
# 找到EXCEPTION_HANDLER字段
# 替换rest_framework.controller.exception_handler成为下面这个
from django.core.exceptions import PermissionDenied
from django.db import connection, transaction
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response


def set_rollback():
    atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
    if atomic_requests and connection.in_atomic_block:
        transaction.set_rollback(True)

def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None
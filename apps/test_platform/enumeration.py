#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class _WritelnDecorator(object):
    """这个类，打印红色字体到控制台的封装类"""

    def __init__(self, stream):
        self.stream = stream

    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream, attr)

    def writeln(self, arg=None):
        """有参数则打印，没有则换行"""
        if arg:
            self.write(arg)
        self.write('\n')  # text-mode streams translate to \r\n if needed

class HttpContentType(Enum):
    """http请求头的数据类型"""
    # 文本格式
    TEXT_HTML = u'text/html'
    TEXT_PLAIN = u'text/plain'
    TEXT_XML = u'text/xml'
    # 媒体格式
    APPLICATION_X_WWW_FORM_URLENCODED = 'application/x-www-form-urlencoded'
    APPLICATION_JSON = 'application/json'
    APPLICATION_XML = 'application/xml'
    APPLICATION_MSWORD = 'application/msword'
    APPLICATION_PDF = 'application/pdf'
    # 图片格式
    IMAGE_GIF = u'image/gif'
    IMAGE_JPEG = u'image/jpeg'
    IMAGE_PNG = u'image/png'


HTTP_CONTENT_TYPE = (
    (HttpContentType.TEXT_HTML,HttpContentType.TEXT_HTML),
    (HttpContentType.TEXT_PLAIN, HttpContentType.TEXT_PLAIN),
    (HttpContentType.TEXT_XML, HttpContentType.TEXT_XML),
    (HttpContentType.APPLICATION_X_WWW_FORM_URLENCODED, HttpContentType.APPLICATION_X_WWW_FORM_URLENCODED),
    (HttpContentType.APPLICATION_JSON, HttpContentType.APPLICATION_JSON),
    (HttpContentType.APPLICATION_XML, HttpContentType.APPLICATION_XML),
    (HttpContentType.APPLICATION_MSWORD, HttpContentType.APPLICATION_MSWORD),
    (HttpContentType.APPLICATION_PDF, HttpContentType.APPLICATION_PDF),
    (HttpContentType.IMAGE_GIF, HttpContentType.IMAGE_GIF),
    (HttpContentType.IMAGE_JPEG, HttpContentType.IMAGE_JPEG),
    (HttpContentType.IMAGE_PNG, HttpContentType.IMAGE_PNG),
)

class RequestMethod(Enum):
    """请求方式"""
    Get = u'GET'
    POST = u'POST'
    PUT = u'PUT'
    DELETE = u'DELETE'

REQUEST_METHOD = (
    (RequestMethod.Get, RequestMethod.Get),
    (RequestMethod.POST, RequestMethod.POST),
    (RequestMethod.PUT, RequestMethod.PUT),
    (RequestMethod.DELETE, RequestMethod.DELETE),
)

class TaskStatus(Enum):
    """任务状态"""
    WAIT = u'等待执行'
    EXECUTION = u'执行中'
    FINISH = u'完成'
    FAILSE = u'失败'

TASK_STUTAS = (
    (TaskStatus.WAIT,TaskStatus.WAIT),
    (TaskStatus.EXECUTION,TaskStatus.EXECUTION),
    (TaskStatus.FINISH,TaskStatus.FINISH),
    (TaskStatus.FAILSE, TaskStatus.FAILSE),
)

if __name__ == '__main__':
    if "POST" == RequestMethod.POST.value:
        print(1)
    print(RequestMethod.POST)
    print(type(RequestMethod.POST))
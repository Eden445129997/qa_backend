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

HTTP_CONTENT_TYPE_LIST = [const.value for const in HttpContentType]

HTTP_CONTENT_TYPE = (
    (HttpContentType.TEXT_HTML.value, HttpContentType.TEXT_HTML.value),
    (HttpContentType.TEXT_PLAIN.value, HttpContentType.TEXT_PLAIN.value),
    (HttpContentType.TEXT_XML.value, HttpContentType.TEXT_XML.value),
    (HttpContentType.APPLICATION_X_WWW_FORM_URLENCODED.value, HttpContentType.APPLICATION_X_WWW_FORM_URLENCODED.value),
    (HttpContentType.APPLICATION_JSON.value, HttpContentType.APPLICATION_JSON.value),
    (HttpContentType.APPLICATION_XML.value, HttpContentType.APPLICATION_XML.value),
    (HttpContentType.APPLICATION_MSWORD.value, HttpContentType.APPLICATION_MSWORD.value),
    (HttpContentType.APPLICATION_PDF.value, HttpContentType.APPLICATION_PDF.value),
    (HttpContentType.IMAGE_GIF.value, HttpContentType.IMAGE_GIF.value),
    (HttpContentType.IMAGE_JPEG.value, HttpContentType.IMAGE_JPEG.value),
    (HttpContentType.IMAGE_PNG.value, HttpContentType.IMAGE_PNG.value),
)


class HttpMethod(Enum):
    """请求方式"""
    Get = u'GET'
    POST = u'POST'
    PUT = u'PUT'
    DELETE = u'DELETE'

HTTP_METHOD_LIST = [const.value for const in HttpMethod]

HTTP_METHOD_TUPLE = (
    (HttpMethod.Get.value, HttpMethod.Get.value),
    (HttpMethod.POST.value, HttpMethod.POST.value),
    (HttpMethod.PUT.value, HttpMethod.PUT.value),
    (HttpMethod.DELETE.value, HttpMethod.DELETE.value),
)


class EventApiStatus(Enum):
    """任务状态"""
    WAIT = u'等待'
    EXECUTION = u'运行'
    FINISH = u'完成'
    FALSE = u'失败'


EVENT_API_STUTAS = (
    (EventApiStatus.WAIT.value, EventApiStatus.WAIT.value),
    (EventApiStatus.EXECUTION.value, EventApiStatus.EXECUTION.value),
    (EventApiStatus.FINISH.value, EventApiStatus.FINISH.value),
    (EventApiStatus.FALSE.value, EventApiStatus.FALSE.value),
)


class AssertMethod(Enum):
    """检查方法"""
    ASSERT_EQUAL = 'assertEqual'
    ASSERT_NOT_EQUAL = 'assertNotEqual'
    ASSERT_IN = 'assertIn'
    ASSERT_NOT_IN = 'assertNotIn'


CHECK_METHOD = (
    (AssertMethod.ASSERT_EQUAL.value, AssertMethod.ASSERT_EQUAL.value),
    (AssertMethod.ASSERT_NOT_EQUAL.value, AssertMethod.ASSERT_NOT_EQUAL.value),
    (AssertMethod.ASSERT_IN.value, AssertMethod.ASSERT_IN.value),
    (AssertMethod.ASSERT_NOT_IN.value, AssertMethod.ASSERT_NOT_IN.value)
)
#result.updateStatus
if __name__ == '__main__':

    # for i in HttpContentType:
    #     print(i.value)
    pass
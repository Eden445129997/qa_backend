#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3
import requests, json, logging, time

# 日志
runner_log = logging.getLogger('runner_log')

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _get(url, data, headers, timeout=10):
    return requests.request(method='GET', url=url, params=data, headers=headers, verify=False, timeout=timeout)


def _post(url, data, headers, timeout=10):
    return requests.request(method='POST', url=url, json=data, headers=headers, verify=False, timeout=timeout)


def _put(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="PUT", url=url, data=data, headers=headers, verify=False, timeout=timeout)


def _delete(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="DELETE", url=url, headers=headers, verify=False, timeout=timeout)


# 选择请求方式
choice = {
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}


class HttpBuilder(object):
    """
    http建造者
    """

    log = runner_log

    def __init__(self):
        self.result = {
            'response': None,
            'fail_times': 0,
            'error_list': []
        }

        self._url = None
        self._data = None
        self._headers = None
        self._reconnection_times = None
        self._rest_reconnection_times = None
        self._timeout = None
        self._fail_times = None

    def build_http(self, method, url, data, headers, reconnection_times=3, timeout=10):
        self._method = method
        self._url = url
        self._headers = headers if isinstance(headers, dict) else {}
        self._data = data if isinstance(data, dict) else {}
        self._reconnection_times = reconnection_times
        self._rest_reconnection_times = reconnection_times
        self._timeout = timeout
        # print(self._url)

    def send_http(self):
        """发送http请求"""
        # 发送请求，失败则递归重复发送
        try:
            # print(self._url)
            response = choice.get(self._method)(url=self._url, data=self._data, headers=self._headers,
                                                timeout=self._timeout)
            # 二进制字符集编码设置
            # response = response.content.decode("unicode_escape")
            response = response.text
            response = json.loads(response)
            self.result['response'] = response
            # 失败次数 = 重连次数 - 剩余重连次数
            self.result['fail_times'] = self._reconnection_times - self._rest_reconnection_times

        except Exception as e:
            self.log.error(e)
            self.result.get('error_list', []).append(e)
            # 剩余重连次数
            self._rest_reconnection_times = self._rest_reconnection_times - 1
            # 剩余重连次数 > 0，则递归
            if self._rest_reconnection_times:
                time.sleep(1)
                self.send_http()

        return self.result


if __name__ == '__main__':
    headers = {
        'CONTENT_TYPE': 'text/plain'
    }
    data = {
        'id': 1
    }
    try:
        print(choice.get("GET")('http://localhost:9998/platform/ProjectViews/', data, headers).text)
    except ConnectionError:
        pass

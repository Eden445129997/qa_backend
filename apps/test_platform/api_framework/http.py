#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3
import requests, json, logging, time

# 日志
runner_log = logging.getLogger('runner_log')

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HttpBuilder(object):
    """
    http建造者
    """

    log = runner_log

    def __init__(self):
        # return字典
        self.result = {
            'response': None,
            'fail_times': 0,
            'error_list': []
        }
        # 请求方法字典
        self._request_method_dict = {
            'GET': '_get',
            'POST': '_post',
            'PUT': '_put',
            'DELETE': '_delete',
        }

        self._url = None
        self._data = None
        self._headers = None
        self._reconnection_times = None
        self._rest_reconnection_times = None
        self._timeout = None
        self._fail_times = None

    def build_http(self, method, url, data, headers, reconnection_times=3, timeout=10):
        """构建参数"""
        self._method = method
        self._url = url
        self._headers = headers if isinstance(headers, dict) else {}
        self._data = data if isinstance(data, dict) else {}
        self._reconnection_times = reconnection_times
        self._rest_reconnection_times = reconnection_times
        self._timeout = timeout
        # print(self._url)

    def reset_http(self):
        """重置参数"""
        self._method = None
        self._url = None
        self._headers = None
        self._data = None
        self._reconnection_times = None
        self._rest_reconnection_times = None
        self._timeout = None

    def send_http(self):
        """发送http请求"""

        # 通过反射获取方法
        request_func = self._get_request_func(self._method)

        # 判空
        if request_func == None:
            self.result.get('error_list', []).append('url:{} & 不存在的方法:{}'.format(self._url, self._method))
            return self.result

        # 判空
        if None in (
                self._url, self._data, self._headers, self._reconnection_times, self._rest_reconnection_times,
                self._timeout
        ):
            self.result.get('error_list', []).append('url:{} & 不存在的方法:{}'.format(self._url, self._method))
            return self.result

        # 发送请求，失败则递归重复发送
        try:
            # print(self._url)
            response = request_func(url=self._url, data=self._data, headers=self._headers,
                                    timeout=self._timeout)
            # 如果响应是空，则当作超时处理
            if response == None:
                raise TimeoutError

            # 二进制字符集编码设置
            # response = response.content.encode('utf-8')
            response = response.text
            response = json.loads(response)
            self.result['response'] = response
            # 失败次数 = 重连次数 - 剩余重连次数
            self.result['fail_times'] = self._reconnection_times - self._rest_reconnection_times

        except TimeoutError as e:
            self.log.error(e)
            # 剩余重连次数
            self._rest_reconnection_times = self._rest_reconnection_times - 1
            # 剩余重连次数 > 0，则递归
            if self._rest_reconnection_times:
                time.sleep(1)
                self.send_http()

        except Exception as e:
            self.log.error(e)
            self.result.get('error_list', []).append(e)

        return self.result

    def _get_request_func(self, func_key):
        """获取请求方法"""
        func = self._request_method_dict.get(func_key)
        if func is not None:
            if isinstance(func, str):
                func = getattr(self, func)
            return func
        return None

    def _base_func(self, url, data, headers, timeout=10):
        """默认方法（暂不考虑使用）"""
        self.result.get('error_list', []).append(
            'url:{} & 不存在的方法:{} & 请求头:{} & 超时:{}'.format(url, data, headers, timeout)
        )

    def _get(self, url, data, headers, timeout=10):
        return requests.request(method='GET', url=url, params=data, headers=headers, verify=False, timeout=timeout)

    def _post(self, url, data, headers, timeout=10):
        return requests.request(method='POST', url=url, json=data, headers=headers, verify=False, timeout=timeout)

    def _put(self, url, data, headers, timeout=10):
        id = data.get("id", -1)
        url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
        return requests.request(method="PUT", url=url, data=data, headers=headers, verify=False, timeout=timeout)

    def _delete(self, url, data, headers, timeout=10):
        id = data.get("id", -1)
        url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
        return requests.request(method="DELETE", url=url, headers=headers, verify=False, timeout=timeout)


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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import urllib3

import requests

# https警告解除
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

METHOD_LIST = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']

CONTENT_TYPE = [
    "text/plain",
    "application/x-www-form-urlencoded",
    "application/json",
]


def _default(method, url, params=None, body=None, headers=None, timeout=10):
    if method.upper() not in METHOD_LIST:
        raise RuntimeError
    if headers and 'application/json' in headers.get('Content-Type') :
        return requests.request(method=method, url=url, params=params, json=body, headers=headers, verify=False,
                                timeout=timeout)
    return requests.request(method=method, url=url, params=params, data=body, headers=headers, verify=False,
                            timeout=timeout)


def _get(url, params, body, headers, timeout=10):
    return _default('GET', url, params, body, headers, timeout=timeout)


def _post(url, params, body, headers, timeout=10):
    return _default('POST', url, params, body, headers, timeout=timeout)


def _put(url, params, body, headers, timeout=10):
    return _default('PUT', url, params, body, headers, timeout=timeout)


def _delete(url, params, body, headers, timeout=10):
    return _default('DELETE', url, params, body, headers, timeout=timeout)


# 选择请求方式
choice = {
    'DEFAULT': _default,
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}

if __name__ == '__main__':
    headers = {
        'referer': 'https://employee.91jkys.com/sso/login',
        'origin': 'https://employee.91jkys.com',
        'upgrade-insecure-requests': 1,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        "redirect": "https://crm-new.91jkys.com",
    }
    body = {
        "name": "heyayun",
        "passwd": "hb123456.",
        # "c": "3"
    }
    response = choice.get('GET')('https://employee.91jkys.com/sso/login?redirect=https://crm-new.91jkys.com', params, body,
                                 {"Content-Type": "text/plain"}, 10)
    print(response.text)

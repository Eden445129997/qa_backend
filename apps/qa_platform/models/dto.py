#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from pydantic import (
    BaseModel, Json , validator, ValidationError
)
from apps.qa_platform.enumeration import (
    HTTP_CONTENT_TYPE_LIST, HTTP_METHOD_LIST
)

import collections
import multiprocessing
import queue
# import asyncio

class TestSuitForDeque(object):
    """
    测试套件（基础队列数据结构，双向队列）
    """

    def __init__(self):
        # 双向队列（性能最快），只实现了基础的队列数据结构，线程安全
        self._suit = collections.deque()

    def __len__(self):
        return len(self._suit)

    def __getitem__(self, position):
        return self._suit[position]

    def __str__(self):
        return str(self._suit)

    def append(self, case):
        self._suit.append(case)

class TestSuitForThreadQueue(object):
    """
    测试套件队列（线程使用）
    """

    def __init__(self):
        # 实现了面向多生产线程、多消费线程的队列，线程安全
        self._suit = queue.Queue()

    def __len__(self):
        return self._suit.qsize()

    def __str__(self):
        return str(self._suit)

    def put(self, case):
        return self._suit.put(case)

    def get(self):
        return self._suit.get()

    def size(self):
        return self._suit.qsize()

    def empty(self):
        return self._suit.empty()

    def task_done(self):
        self._suit.task_done()


class TestSuitForProcessQueue(object):
    """
    测试套件(进程使用)
    """

    def __init__(self):
        # 面向多成产进程、多消费进程的队列
        self._suit = multiprocessing.Queue()

class Context(BaseModel):
    # 测试计划id
    plan_id: int = 0
    # 测试用例id
    case_id: int = 0
    # 执行任务的用例id列表
    case_id_list: list = []
    # 接口请求的host
    host: str
    # headers
    # headers: Json or dict = {}
    headers: dict = {}

class Api(BaseModel):
    id : int
    project_id : int
    api_name : str
    content_type : str
    method : str
    path : str
    text : str
    is_status : bool
    is_delete : bool
    # create_time
    # update_time
    
    @validator('content_type')
    def content_type_validator(cls, val):
        assert val in HTTP_CONTENT_TYPE_LIST
        return val

    @validator('method')
    def method_validator(cls, val):
        assert val in HTTP_METHOD_LIST
        return val


class CaseApiNode(BaseModel):
    # 用例id
    case_id : int
    # 请求的接口
    api: Api
    # 重连次数
    reconnection_times: int
    # 超时设置
    timeout: int
    # 请求头
    # headers: str
    headers: Json
    # url后的查询参数
    # query: str
    query: Json
    # params: Json
    # 请求体
    # body: str
    body: Json
    # mock状态（0 不启用mock，1启用mock）
    is_mock: bool
    # mock返回
    mock_response: str
    # mock_response: Json
    # 表达式状态
    is_expression: bool
    # 检查点列表
    assert_list: list
    # 这个节点最终绑定的报告id
    result_id: int = 0
    # 数据id
    data_id : int
    # 执行顺序
    sort : int
    # 响应，这个是在执行用例之后，才会生成的结果
    response : str = None
    # 请求时候的失败次数
    fail_times = 0
    # 请求时候的失败信息
    err_record = []




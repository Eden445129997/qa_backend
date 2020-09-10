#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

class Project(models.Model):
    """
    工程表
    """
    # 工程id
    id = models.AutoField(primary_key=True)
    # 工程名
    project_name = models.CharField(verbose_name="项目名", max_length=64)
    # 工程描述
    text = models.CharField(verbose_name="描述", max_length=64)
    # 项目负责人
    project_leader = models.CharField("负责人", max_length=64)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_project"
        # django的admin界面的后台展示的数据
        verbose_name = "项目"
        verbose_name_plural = verbose_name


class Host(models.Model):
    """
    域名表
    """
    # 域名id
    id = models.AutoField(primary_key=True)
    # 外键—关联工程表
    project_id = models.IntegerField(verbose_name='所属项目id')
    # 环境名
    nickname = models.CharField(verbose_name='域名昵称', max_length=32)
    # host地址
    host = models.CharField(verbose_name='Host域名', max_length=64)
    # 环境描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_host"
        # django的admin界面的后台展示的数据
        verbose_name = "环境"
        verbose_name_plural = verbose_name

class Api(models.Model):
    """
    接口表
    """
    # 接口id
    id = models.AutoField(primary_key=True)
    # 工程id
    project_id = models.IntegerField(verbose_name='所属项目id', blank=True, null=True)
    # 接口名称
    api_name = models.CharField(verbose_name="接口名称", max_length=32)
    # 解析方式
    content_type = models.CharField(verbose_name="http报文body序列化类型content_type", choices=HTTP_CONTENT_TYPE,
                                    max_length=128)
    # 请求方式—1、get2、post3、put4、delete
    method = models.CharField(verbose_name="请求方式", choices=REQUEST_METHOD, max_length=255)
    # 资源路径
    path = models.CharField(verbose_name="资源路径", max_length=128)
    # 接口描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api"
        # django的admin界面的后台展示的数据
        verbose_name = "接口"
        verbose_name_plural = verbose_name


class QaPlan(models.Model):
    """
    测试计划表
    """
    # 计划id
    id = models.AutoField(primary_key=True)
    # 外键—关联工程表
    project_id = models.IntegerField(verbose_name='所属项目id', blank=True, null=True)
    # 计划名称
    plan_name = models.CharField(verbose_name="测试计划", max_length=32)
    # 计划描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_qa_plan"
        # django的admin界面的后台展示的数据
        verbose_name = "测试计划"
        verbose_name_plural = verbose_name


class QaCase(models.Model):
    """
    测试用例表
    """
    # 用例id
    id = models.AutoField(primary_key=True)
    # 外键—关联计划表
    plan_id = models.IntegerField(verbose_name='所属计划id')
    # 用例名称
    case_name = models.CharField(verbose_name="用例名称", max_length=32)
    # 排序
    sort = models.IntegerField(verbose_name="排序", default=0)
    # 用例描述
    text = models.CharField(verbose_name="描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_qa_case"
        # django的admin界面的后台展示的数据
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name


class ApiCaseModel(models.Model):
    """测试模型表(测试节点表)"""
    """
    比如用例ABCDE，如果c启用mock，则写入mock返回值，c校验直接为True，并直接取mock里面的值
    """

    # 用例id
    id = models.AutoField(primary_key=True)
    # 外键—关联用例表
    case_id = models.IntegerField(verbose_name='所属用例id')
    # 请求的path
    api_id = models.IntegerField(verbose_name='关联的接口id')
    # 重连次数
    reconnection_times = models.IntegerField(verbose_name="重连次数", default=3)
    # 超时设置
    timeout = models.IntegerField(verbose_name="最长等待时长", default=10)
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    query = models.TextField(verbose_name="请求头入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # mock状态（0 不启用mock，1启用mock）
    is_mock = models.BooleanField(verbose_name="mock状态（0 不启用mock，1启用mock）", default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock的返回值", default="{}")
    # 表达式状态
    is_expression = models.BooleanField(verbose_name="表达式状态（0 不启用jsonpath捕捉参数化，1 启用jsonpath捕捉参数化）", default=False)
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
    # 排序顺序
    sort = models.IntegerField(verbose_name="用例排序顺序", default=0)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_model"
        # django的admin界面的后台展示的数据
        verbose_name = "用例模型"
        verbose_name_plural = verbose_name


class ApiCaseData(models.Model):
    # 用例id
    id = models.AutoField(primary_key=True)
    # 关联用例表
    case_id = models.IntegerField(verbose_name='所属用例id')
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_data"
        # django的admin界面的后台展示的数据
        verbose_name = "用例参数"
        verbose_name_plural = verbose_name


class ApiCaseDataNode(models.Model):
    # 用例id
    id = models.AutoField(primary_key=True)
    # 关联用例表
    data_id = models.IntegerField(verbose_name='所属数据id', default=1)
    # 用例模型id
    model_id = models.IntegerField(verbose_name='所属用例模型id')
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    params = models.TextField(verbose_name="请求行入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # mock状态（0 不启用mock，1启用mock）
    is_mock = models.BooleanField(verbose_name="mock状态（0 不启用mock，1启用mock）", default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock的返回值", default="{}")
    # 表达式状态
    is_expression = models.BooleanField(verbose_name="表达式状态（0 不启用jsonpath捕捉参数化，1 启用jsonpath捕捉参数化）", default=False)
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_data_node"
        # django的admin界面的后台展示的数据
        verbose_name = "用例参数"
        verbose_name_plural = verbose_name


class ApiAssert(models.Model):
    """
    断言
    """
    id = models.AutoField(primary_key=True)
    # 关联的case_model_id
    api_model_id = models.IntegerField(verbose_name='所属的case_model')
    # 检查对象（仅仅支持json校验）
    assert_object = models.CharField(verbose_name='检查对象，jsonpath表达式', max_length=64)
    # 检查关系
    assert_method = models.CharField(verbose_name='校验方法', max_length=16, choices=CHECK_METHOD)
    # 检查值
    assert_value = models.TextField(verbose_name="校验的比对值")
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_assert"
        # django的admin界面的后台展示的数据
        verbose_name = "断言"
        verbose_name_plural = verbose_name


class Event(models.Model):
    """
    事件工单
    """
    id = models.AutoField(primary_key=True)
    # 业务开关（00000）类似二进制处理方式，0未处理，1已处理
    switch = models.CharField(verbose_name="业务字段（0为需要执行，1不需要处理）", max_length=16, null=True)
    # 事件数据（json存储）
    context = models.TextField(verbose_name="事件数据",default= "{}")
    # 当前执行次数
    current_times = models.IntegerField(verbose_name="最大执行次数", default=0)
    # 最大执行次数
    max_times = models.IntegerField(verbose_name="最大执行次数", default=3)
    # 事件描述
    text = models.CharField(verbose_name="事件备注", max_length=64, blank=True, null=True)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event"
        # django的admin界面的后台展示的数据
        verbose_name = "接口测试报告"
        verbose_name_plural = verbose_name

class EventApiResult(models.Model):
    """
    接口测试事件结果
    """
    id = models.AutoField(primary_key=True)
    # 执行的域名
    host = models.CharField(verbose_name="执行的域名", max_length=64, null=True)
    # 执行用例总数
    total = models.IntegerField(verbose_name="用例执行总数", blank=True, null=True)
    # 接口测试结果
    current_status = models.CharField(verbose_name="接口测试结果", choices=EVENT_API_STUTAS, max_length=8)
    # 所用时间(s为单位)
    time_taken = models.CharField(verbose_name="执行使用时间", max_length=16, blank=True, null=True)
    # 测试套件的数据准备是否成功
    is_prepared = models.BooleanField(verbose_name="套件准备：0未准备 1已准备", default=False)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event_api_result"
        # django的admin界面的后台展示的数据
        verbose_name = "接口测试结果"
        verbose_name_plural = verbose_name


class EventApiRecord(models.Model):
    """
    接口测试事件结果记录
    """
    id = models.AutoField(primary_key=True)
    # 外键关联报告id
    result_id = models.IntegerField(verbose_name='所属报告id')
    # 外键关联用例id
    case_id = models.IntegerField(verbose_name='所属用例id', blank=True, null=True)
    # 绑定的数据id
    data_id = models.IntegerField(verbose_name='所属数据id', blank=True, null=True)
    # 接口别名
    api_name = models.CharField(verbose_name="接口名称", null=True, max_length=32)
    # 请求的url
    url = models.CharField(verbose_name="请求地址", null=True, max_length=128)
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    params = models.TextField(verbose_name="请求行入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # 响应参数
    response = models.TextField(verbose_name="响应参数", blank=True, null=True)
    # 报错记录
    err_record = models.TextField(verbose_name="报错记录", blank=True, null=True)
    # 失败次数
    fail_times = models.IntegerField(verbose_name="请求失败次数", null=True)
    # 是否mock，该历史记录是否使用mock
    is_mock = models.BooleanField(verbose_name="是否mock", default=False)
    # 排序顺序
    sort = models.IntegerField(verbose_name="用例排序顺序", default=0)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除）", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_event_api_record"
        # django的admin界面的后台展示的数据
        verbose_name = "接口测试报告细节"
        verbose_name_plural = verbose_name

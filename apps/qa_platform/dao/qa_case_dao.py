#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def query_case_list_by_plan_id(plan_id: int):
    """
    1、根据测试计划获取测试用例id列表
    2、根据测试用例id列表获取测试套件
    :param plan_id:
    :return: 测试套件列表 or 数据异常为None
    """
    # 根据测试计划获取测试用例列表
    # return [
    #     id.get("id")
    #     # 循环queryset字典列表
    #     for id in domain.QaCase.objects
    #         .values("id")
    #         .filter(id=plan_id, is_status=1, is_delete=0)
    #         .order_by('-sort').order_by('id')
    # ]

    return query_set_list_serializers(
        domain.QaCase.objects
            .filter(
            plan_id=plan_id,
            is_status=1,
            is_delete=0
        )
            .order_by('-sort')
            .order_by('id')
    )
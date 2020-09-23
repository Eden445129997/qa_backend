#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def query_api_case_model_list_by_case_id(case_id : int):
    """根据用例id获取接口用例模型列表"""
    return query_set_list_serializers(
            domain.ApiCaseModel.objects.filter(
                case_id=case_id, is_status=1, is_delete=0
            ).order_by('-sort').order_by('id')
        )
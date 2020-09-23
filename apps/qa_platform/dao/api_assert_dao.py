#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def get_api_assert_list_by_data_id(data_id : int):
    return domain.ApiAssert.objects.values(
        'data_id', 'model_id', 'assert_method', 'assert_obj', 'assert_val'
    ).filter(
        data_id=data_id,
        is_status=1,
        is_delete=0
    )
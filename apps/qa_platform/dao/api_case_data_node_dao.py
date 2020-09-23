#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def query_case_api_data_node_list_by_data_id(data_id : int):
    return query_set_list_serializers(
        domain.ApiCaseDataNode.objects
            .filter(
            data_id=data_id,
            is_status=1,
            is_delete=0
        )
    )
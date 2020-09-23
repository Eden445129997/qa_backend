#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models import domain
# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

def query_api_case_data_id_list(case_id : int):
    return domain.ApiCaseData.objects \
        .values("id")\
        .filter(
        case_id=case_id,
        is_status=1,
        is_delete=0
    )
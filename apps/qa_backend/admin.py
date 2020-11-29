#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    django后台
"""

# from apps.qa_backend.models.domain import (
#     api, api_assert, api_case_data, api_case_data_node, api_case_model,
#     event, event_api_record, event_api_result, host, project, qa_case, qa_plan
# )

# #自定义后台的名字
# class QaAdminsite(admin.AdminSite):
#     site_header = '测试平台'
#     site_title = '测试平台'
#
# site = QaAdminsite()

from django.contrib import admin

from apps.qa_backend.models.admin import *

admin.site.site_header = 'Qa管理后台'
admin.site.index_title = "xxxx名称"


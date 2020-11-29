
# rest_framework 默认配置
from rest_framework import settings

# drf 配置
REST_FRAMEWORK = {
    # 3.1限流策略
    'DEFAULT_THROTTLE_RATES': {
        # 'user': '100/hour',  # 认证用户每小时100次
        # 'anon': '3/day',  # 未认证用户每天能访问3次
        'user': None,
        'anon': None,
    },
    # 全局过滤(字段查询)
    # pip install django-filter，使用的django插件
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 全局分页(两种)
    # rest_framework.pagination.PageNumberPagination
    # rest_framework.pagination.LimitOffsetPagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # pip install coreapi，新版drf自带文档接口配置
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
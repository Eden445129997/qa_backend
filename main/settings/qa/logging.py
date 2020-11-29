from .. import *

# 日志地址
LOG_DIR = BASE_DIR.path('logs')

LOGGING = {
    # 版本
    'version': 1,
    # 是否禁止默认配置的记录器
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '\n%(asctime)s %(levelname)s\n'
                      '%(pathname)s\n'
                      'process_id:%(process)d\n'
                      'thread_id:%(thread)d\n'
                      '%(message)s\n',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    # 过滤器
    # 'filters': {
    #     'request_info': {'()': 'apps.common.custom_middleware.DataReCordMiddleware'},
    # },
    'handlers': {
        # 标准输出
        'console': {
            # 'level': 'DEBUG',
            # 'level': 'ERROR',
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            # 'formatter': 'standard'
        },
        # 自定义 handlers，输出到文件
        'requests': {
            'level': 'DEBUG',
            # 时间滚动切分
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_DIR.path('http.log').__str__(),
            'encoding': 'utf-8',
            'formatter': 'standard',
            # 调用过滤器
            # 'filters': ['request_info'],
            # 每天凌晨切分
            # 'when': 'MIDNIGHT',
            # 保存 30 天
            # 'backupCount': 30,
        },
        # 自定义 handlers，输出到文件
        'event-api': {
            'level': 'DEBUG',
            # 时间滚动切分
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_DIR.path('event-api.log').__str__(),
            'encoding': 'utf-8',
            'formatter': 'standard',
            # 调用过滤器
            # 'filters': ['request_info'],
            # 每天凌晨切分
            # 'when': 'MIDNIGHT',
            # 保存 30 天
            # 'backupCount': 30,
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'http': {
            'handlers': ['requests'],
            'level': 'INFO',
            'propagate': False
        },
        'event': {
            'handlers': ['event-api', 'console'],
            'level': 'INFO',
            # 此记录器处理过的消息就不再让 django 记录器再次处理了
            'propagate': False
        },
    }
}
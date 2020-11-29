
# 如果为True，则将允许将cookie包含在跨站点HTTP请求中。默认为False
CORS_ALLOW_CREDENTIALS = True
# 如果为True，则将不使用白名单，并且将接受所有来源。默认为False
CORS_ORIGIN_ALLOW_ALL = False
# 允许跨域请求的白名单
# django3.0之后必须http开头
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8081',
    'http://localhost:8081'
)

# corsheaders默认配置
from corsheaders.defaults import (
    default_methods, default_headers
)
# 自定义接收的http请求方式
CORS_ALLOW_METHODS = list(default_methods) + [
    'POKE',
    'VIEW',
]
# 自定义接收的http请求头
CORS_ALLOW_HEADERS = list(default_headers) + [
    'XMLHttpRequest',
    'X_FILENAME',
    'Pragma',
    'Access-Control-Allow-Origin',
]
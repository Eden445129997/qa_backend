#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 别人的django代码
# git clone https://github.com/happyletme/requestnew.git
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import *

# 根Url
ROOT_URLCONF = 'main.urls'

# 服务器部署配置
WSGI_APPLICATION = 'main.wsgi.application'

# 应用配置
INSTALLED_APPS = [
    # simpleui ui框架
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 跨域请求解决方案的跨域包
    "corsheaders",
    # drf框架（更加方便开发）
    "rest_framework",
    # django全局过滤
    'django_filters',
    # demo服务
    # "apps.demo_service",
    # 测试人员服务
    "apps.qa_backend",
]

# 中间件配置
MIDDLEWARE = [
    # corsheaders的包
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 跨域设置（必须在django.middleware.csrf.CsrfViewMiddleware的上面）
    'django.middleware.common.CommonMiddleware',
    # csrf攻击跳过（前后端分离不需要做）
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # log中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义中间件
    'apps.common.middleware.CustomMiddleware'
]

# 数据库配置
DATABASES = {
    'default': env.db()
}

# rest_framework 配置
from .rest_framework import *

# 缓存配置
from .caches import *

# corsheaders配置
from .corsheaders import *

# 模版配置
from . import templates

# 语言设置
from .language import *

# 时区配置（该配置影响django orm的时间字段，还有时区国际化的问题）
from .time import *

# 静态资源配置
from .static import *

# simpleui配置
from .simpleui import *

# 定义媒体存放路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# logging的配置
from .logging import *

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import environ

# 根路径
BASE_DIR = environ.Path(__file__) - 3
# 创建环境对象
env = environ.Env()
# 读取.env文件
env.read_env(BASE_DIR.path('.env').__str__())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)
# 访问白名单
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# 白名单默认
ALLOWED_HOSTS = ALLOWED_HOSTS if ALLOWED_HOSTS else ['*',]


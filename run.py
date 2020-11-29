#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def start_app(app_name):
    """创建应用"""
    # 移动到项目文件下
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%project_dir)
    # 创建app
    os.system("python3 manage.py startapp %s"%app_name)

def inspectdb(db_models):
    """将数据库的表映射创建模板文件orm"""
    # 移动到项目文件下
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%project_dir)
    # 创建模板文件
    os.system("python3 manage.py inspectdb > %s/domain.py"%db_models)

def synchronized_db():
    """同步数据库和表结构"""
    # 移动到项目文件下
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%project_dir)
    # 生成迁移文件
    os.system("python3 manage.py makemigrations")
    # 执行迁移
    os.system("python3 manage.py migrate")

def flush():
    """清空数据库"""
    # 移动到项目文件下
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%project_dir)
    # 生成迁移文件
    os.system("python3 manage.py flush")

def runserver():
    """启动服务"""
    port = "9998"

    # 该文件位置
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print(project_dir)
    # os.system("ipconfig")
    # # 跳转到项目文件下
    os.system("cd %s"%project_dir)
    # os.system("python manage.py collectstatic")
    # # 开启服务，并且指定端口
    os.system("python3 manage.py runserver 0.0.0.0:%s --noreload"%(port))

if __name__ == '__main__':
    # start_app("batch_processing_service")
    # inspectdb("api_project")
    # synchronized_db()
    runserver()
    pass

# 创建django架构的应用
# python3 manage.py startapp appname

# 使用django的admin，创建用户
# python manage.py createsuperuser

# 根据setting配置创建css等静态资源文件（配合nginx使用）
# python manage.py collectstatic

# 启动服务（默认端口8080）
# python3 manage.py runserver ip:port


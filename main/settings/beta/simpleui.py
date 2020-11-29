#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 修改模板
# 在simpleui的基础上修改模板需要对django有一定了解
# 先把simpleui克隆到静态目录下，参考克隆静态文件
# 静态目录配置STATIC_URL、STATICFILES_DIRS、STATIC_ROOT
# 找到静态目录下的admin目录，里面就是simpleui的模板，直接修改相关html页面即可生效。

# True为开启， simpleui, 收集使用的信息，完善开源项目资源
SIMPLEUI_ANALYSIS = True


# 登录页粒子动画设置
SIMPLEUI_LOGIN_PARTICLES = True


# # simpleui文档以及github信息展示
SIMPLEUI_HOME_INFO = False
# # 快速操作展示
SIMPLEUI_HOME_QUICK = True
# # 最近动作展示
SIMPLEUI_HOME_ACTION = True

# 首页配置URL
# SIMPLEUI_HOME_PAGE = 'http://localhost:9998/docs/'
# 首页标题
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标
# SIMPLEUI_HOME_ICON = 'fa fa-user'
# 首页图标跳转的地址
# SIMPLEUI_INDEX = 'http://localhost:9998/docs/'
# 修改logo
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'


# 主题文件theme.js
# 路径 static/admin/simpleui-x/theme/{theme.js}
# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
# SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
SIMPLEUI_DEFAULT_THEME = 'ant.design.css'
# SIMPLEUI_DEFAULT_THEME = 'e-black.css'


# 默认图标，默认True
# 优先级： 自定义->系统配图->默认图标
SIMPLEUI_DEFAULT_ICON = True


# 自定义图标
# name：模块名字，请注意不是model的命名，而是菜单栏上显示的文本，因为model是可以重复的，会导致无法区分
# icon：图标
# SIMPLEUI_ICON = {
#     '系统管理': 'fab fa-apple',
#     '员工管理': 'fas fa-user-tie'
# }

# 侧边栏菜单
# 如果SIMPLEUI_CONFIG中存在menus字段，将会覆盖系统默认菜单。并且menus中输出的菜单不会受权限控制。
import time
SIMPLEUI_CONFIG = {
    # system_keep 保留系统菜单，如果改为True，自定义和系统菜单将会并存
    'system_keep': False,
    # menu_display 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    # 'menu_display': ['测试平台','Simpleui', '测试', '权限认证', '动态菜单测试'],
    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'dynamic': False,
    'menus': [
        {
            'name': '项目',
            'icon': 'fa fa-user',
            'url': 'qa_backend/project/'
        },
        {
            'name': 'HOST配置',
            'icon': 'fa fa-user',
            'url': 'qa_backend/host/'
        },
        {
            'name': '接口配置',
            'icon': 'fa fa-user',
            'url': 'qa_backend/api/'
        },
        {
            # 菜单名
            'name': '接口测试',
            # 图标，参考element-ui和fontawesome图标
            'icon': 'fas fa-code',
            # 链接地址，绝对或者相对,如果存在models字段，将忽略url
            # 'url': 'qa_backend/api/',
            # 子菜单
            'models': [
                {
                    'name': '测试计划',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/qaplan/'
                },
                {
                    'name': '测试用例',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/qacase/'
                },
                {
                    'name': '接口模型',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/apicasemodel/'
                },
                {
                    'name': '接口数据',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/apicasedata/'
                },
                {
                    'name': '接口数据节点',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/apicasedatanode/'
                },
                {
                    'name': '接口断言',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/apiassert/'
                },
                {
                    'name': '接口事件结果',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/eventapiresult/'
                },
                {
                    'name': '接口事件细节记录',
                    'icon': 'fa fa-user',
                    'url': 'qa_backend/eventapirecord/'
                },
            ]
        },
        {
            # 菜单名
            'name': 'Simpleui',
            # 图标，参考element-ui和fontawesome图标
            'icon': 'fas fa-code',
            # 链接地址，绝对或者相对,如果存在models字段，将忽略url
            'url': 'https://gitee.com/tompeppa/simpleui',
            # 子菜单
            # 'models': []
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [{
                'name': '用户',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            }]
        },
        {
            'name': '测试',
            'icon': 'fa fa-file',
            'models': [{
                'name': 'Baidu',
                'url': 'http://baidu.com',
                'icon': 'far fa-surprise'
            }, {
                'name': '内网穿透',
                'url': 'https://www.wezoz.com',
                'icon': 'fab fa-github'
            }]
        },
        {
            'name': '动态菜单测试' ,
            'icon': 'fa fa-desktop',
            'models': [
                {
                'name': time.time(),
                'url': 'http://baidu.com',
                'icon': 'far fa-surprise'
                }
            ]
        }
    ]
}
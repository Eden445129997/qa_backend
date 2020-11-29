#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from .. import (
    register, BaseTabularInline, BaseStackedInline
)

# 自定义基类
from .. import (
    BaseAdmin
)

# 获取所有文件列表
file_list = os.walk(os.path.dirname(os.path.abspath(__file__))).__next__()[2]
# 去掉指定文件
file_list.pop(file_list.index('__init__.py'))

__all__ = [abs_file_name[:-3] for abs_file_name in file_list]


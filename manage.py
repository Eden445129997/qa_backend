#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    print('请输入环境名称')
    env = input()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.%s' %env)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django。你确定它已经安装并且"
            "在PYTHONPATH环境变量中可用？是吗？"
            "忘记激活虚拟环境？"
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

from django.contrib import admin
from . import models

# Register your models here.
# Django的admin可以提供一个强大的后台管理功能，可以在web界面对数据库进行操作,我们需要修改admin.py将要操作的数据表注册到后台管理中
# 将demo的表模型注册到后台管理，可以通过admin管理进行管理
admin.site.register(models.DemoModel)
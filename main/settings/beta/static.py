from .. import *

# 浏览器访问静态资源的“根路径”，STATIC_URL
STATIC_URL = '/server/static/'

# 公共的静态文件的文件夹STATICFILES_DIRS
# STATICFILES_DIRS默认在公用文件中找，找不到就会在对应的app下找
# ###开发阶段放置项目自己的静态文件###

STATICFILES_DIRS = [
     # os.path.join(BASE_DIR, 'staticfile', ''),
]

# 上线配置使用
# 执行"python manage.py collectstatic"命令后会将项目中的静态文件收集到该目录下面来（所以不应该在该目录下面放置自己的一些静态文件，因为会覆盖掉）
# if not DEBUG:
STATIC_ROOT = BASE_DIR.path('static').__str__()
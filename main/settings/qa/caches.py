
CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # 指定缓存使用的引擎
        # 'LOCATION': 'cache_table',  # 数据库表
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 指定缓存使用的引擎
        # 'LOCATION': 'unique-snowflake',         # 写在内存中的变量的唯一值
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #指定缓存使用的引擎
        'LOCATION': '/var/tmp/django_cache',        #指定缓存的路径
        'TIMEOUT':300,              #缓存超时时间(默认为300秒,None表示永不过期)
        'OPTIONS':{
            'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
            'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
        }
    }
}
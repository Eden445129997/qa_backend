# django原生sql
from django.db import connection

# def db_cursor(sql):
#     return cursor.execute(sql)

class db(object):

    # cursor = connection.cursor()
    _instance = None

    # 单例设计模式
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(db,cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.cursor = connection.cursor()

    def db_cursor(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
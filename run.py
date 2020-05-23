import os

def start_app(app_name):
    """创建应用"""
    # 移动到项目文件下
    djangoProjectPath = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%djangoProjectPath)
    # 创建app
    os.system("python3 manage.py startapp %s"%app_name)

def inspectdb(db_models):
    """将数据库的表映射创建模板文件orm"""
    # 移动到项目文件下DyOl5spjCA;A
    djangoProjectPath = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%djangoProjectPath)
    # 创建模板文件
    os.system("python3 manage.py inspectdb > %s/models.py"%db_models)

def synchronized_db():
    """同步数据库和表结构"""
    # 移动到项目文件下
    djangoProjectPath = os.path.dirname(os.path.abspath(__file__))
    os.system("cd %s"%djangoProjectPath)
    # 迁移数据库和表结构
    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")


def run():
    """启动服务"""
    port = "9998"

    # 该文件位置
    djangoProjectPath = os.path.dirname(os.path.abspath(__file__))
    print(djangoProjectPath)
    # os.system("ipconfig")
    # # 跳转到项目文件下
    os.system("cd %s"%djangoProjectPath)
    # # 开启服务，并且指定端口
    os.system("python3 manage.py runserver 0.0.0.0:%s"%port)

if __name__ == '__main__':
    # start_app("batch_processing_service")
    # inspectdb("api_project")
    # synchronized_db()
    run()

# python manage.py createsuperuser
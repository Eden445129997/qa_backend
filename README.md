# 常见问题
##1、django与mysql8的用户加密兼容问题
解决方案：去mysql修改用户加密方式，则临时解决当前兼容问题
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';  
FLUSH PRIVILEGES;
备注：注意你的账号密码不要打错，'root'@'localhost'和'password'

##2、django对myclient版本限制
解决方案：
    __init__.py加入下面内容，（版本号可根据实际情况稍微修改）
import pymysql
pymysql.install_as_MySQLdb()
pymysql.version_info = (1, 4, 13, "final", 0)

##3、django与mysql编码问题
报错： AttributeError: 'str' object has no attribute 'decode'
解决方案：
    报错代码，将decode改为encode

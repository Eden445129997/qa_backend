# coding=UTF-8
import logging                                                                                                         #标准库,日志包
from .path import logPath                                                                            #自用包,路径模块
import time

'''
    Logger.setLevel() 指定了该 logger 对象将会处理的日志消息的最低的级别。
    DEBUG 是内置的最低的日志严重性级别，CRITICAL 是内置的最高的日志严重性级别。
    例如，如果严重性级别被设置为 INFO，那么这个 logger 将只会处理 INFO，WARNING，ERROR，CRITICAL 级别的日志消息，而忽略 DEBUG 级别的消息。
    日志等级：
    critical
    error
    warning
    info
    debug
'''

class log(object):

    __instance = None
    __logName = "testTask_"

    # 单例设计模式，并且存在该数据库存在在ini配置文件中（得加锁）
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(log,cls).__new__(cls)
        return cls.__instance

    def __init__(self,fileName=__logName):
        now = time.strftime('%Y-%m-%d',time.localtime())
        self.filename = fileName + now + ".log"

    def setMsg(self,Level,*args, **kwargs):

        logname = logPath() + self.filename                                                                             #(路径+文件名)
        fmt = logging.Formatter("%(asctime)s %(levelname)-8s:%(message)s")                                         #创建日志格式对象

        logger = logging.getLogger()                                                                                    #创建获取日志对象
        fh = logging.FileHandler(logname)                                                                               #输出日志对象
        sh = logging.StreamHandler()                                                                                    #输出日志控制台

        fh.setFormatter(fmt)                                                                                            #定义日志对象写入日志格式
        sh.setFormatter(fmt)                                                                                            #定义控制台写入日志格式

        #添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(sh)

        logger.setLevel(logging.INFO)                                                                                   #添加日志信息，输出INFO级别的日志信息

        if Level == "debug":
            logger.debug(*args, **kwargs)
        elif Level == "info":
            logger.info(*args, **kwargs)
        elif Level == "warning":
            logger.warning(*args, **kwargs)
        elif Level == "error":
            logger.error(*args, **kwargs)

        #移除日志输出平台，避免重复写入
        logger.removeHandler(fh)
        logger.removeHandler(sh)
        fh.close()

    def debug(self,*args, **kwargs):
        self.setMsg('debug',*args, **kwargs)
    def info(self,*args, **kwargs):
        self.setMsg('info',*args, **kwargs)
    def warning(self,*args, **kwargs):
        self.setMsg('warning',*args, **kwargs)
    def error(self,*args, **kwargs):
        self.setMsg('error',*args, **kwargs)

if __name__ == '__main__':
    l = log("aaa_")               #创建日志对象，定义日志文件名称
    l.error({"app-http1":"app-http1"})
    l.info("test2")
    l.warning("sss")
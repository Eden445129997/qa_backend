from .Log import log
import pymysql


class odbc(object):

    __instance = None
    __database = None

    # 单例设计模式，并且存在该数据库存在在ini配置文件中（得加锁）
    # def __new__(cls, *args, **kwargs):
    #     if not cls.__instance and not cls.__database:
    #         cls.__instance = super(odbc,cls).__new__(cls)
    #     return cls.__instance

    # 创建Mysql.ini对象
    def __init__(self,database):

        self.host = "10.113.248.127"
        self.port = 3306
        self.user = "root"
        self.password = "root"
        self.charset = "utf8"
        self.__database = database

        self.log = log()


    # 尝试数据库连接
    def __connectDB(self):
        # 判断连接的数据库是存在在ini配置文件中，存在才进行连接
        try:
            #连接数据库
            conn = pymysql.connect(
                host = self.host,
                port = int(self.port),
                user = self.user,
                password = self.password,
                database = self.__database,
                charset = self.charset
            )

            return conn
        except:
            self.log.error("连接数据库失败：" + self.__database)
            return False

    # 增删改SQL语句
    def commitSQL(self,sql):
        # 连接数据库，成功返回连接，失败返回false
        conn = self.__connectDB()
        if conn == False:
            return False
        else:
            # 创建游标来执行对数据库的操作
            cursor = conn.cursor()

            # 尝试执行sql语句，成功则关闭连接返回True
            try:
                cursor.execute(sql)
                conn.commit()
                self.log.info("执行sql成功：" + sql)

                #如果成功到return的时候，会先执行finally关键字，关闭数据库连接
                return True
            except:
                self.log.error(self.__database + "执行sql失败：" + sql)
                return False
            finally:
                # 关闭数据库连接
                cursor.close()
                conn.close()

    # 查询SQL
    def selectSQL(self,sql):
        # 连接数据库，成功返回连接，失败返回false
        conn = self.__connectDB()
        if conn == False:
            return False
        else:
            # 创建游标来执行对数据库的操作
            cursor = conn.cursor()

            # 尝试执行sql语句，成功则关闭连接返回True
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                self.log.info("执行sql成功：" + sql)

                #如果成功到return的时候，会先执行finally关键字，关闭数据库连接
                return result
            except:
                self.log.error(self.__database + "执行sql失败：" + sql)
                return False
            finally:
                # 关闭数据库连接
                cursor.close()
                conn.close()


if __name__ == '__main__':
    db = odbc("qiaoku_user")
    # db.commitSQL("delete from db_life_center.tb_ticket where id = 99")
    # db.commitSQL("INSERT INTO `db_life_center`.`tb_ticket` (`ticket_id`, `ticket_name`, `ticket_type`, `merchant_id`, `ticket_price`, `ticket_value`, `ticket_sold`, `total_count`, `low_pay`, `use_condition`, `buy_condition`, `validity_date`, `use_explain`, `chk_status`, `del_flag`, `create_time`, `last_update_time`) VALUES ('999999', 'testdata', NULL, '99999999', '5', '30', '175', '100', NULL, NULL, NULL, '5', NULL, NULL, '0', now(), now());")
    # db.a()
    # b = db.selectSQL("select * from tb_user_info where user_phone = 12345678901")
    # b = db.commitSQL("INSERT INTO `qiaoku_user`.`tb_user_info` (`id`, `user_id`, `qiaoku_id`, `nick_name`, `birthday`, `gender`, `avatar`, `avatar_large`, `user_phone`, `province`, `city`, `region`, `user_sign`, `user_origin`, `belong_back_user`, `udid`, `user_status`, `talent_mark`, `player_mark`, `total_publish_count`, `total_thumb_up_count`, `total_collection_count`, `user_follow_count`, `user_fans_count`, `binding_wx`, `binding_qq`, `del_flag`, `create_time`, `last_update_time`) VALUES ('1', '111111111111111111', '1111111111', '我是测试啊', NULL, '3', 'https://thirdwx.qlogo.cn/mmopen/vi_32/iblOuNxMNQoloaPo5xMM0acNt5jezgAyAIpnNDpRjJWDCxficmU4DPMEONuzpWor7FXOLDtYWIq8zOHHptpULUoQ/132', NULL, '12345678901', '', '', NULL, NULL, '0', NULL, '64d96dba-2e5f-4168-ade8-06652cbafeec', '1', '2', '1', NULL, NULL, NULL, NULL, NULL, '1', '2', '0', '2019-08-19 20:52:59', '2019-08-19 20:53:55');")
    b = db.selectSQL("show tables")
    print(b)
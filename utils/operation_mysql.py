# coding = utf-8
"""
@Time      : 2020/3/1 0001 10:11
@Author    : YunFan
@File      : operation_mysql.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import pymysql
import pymysql.cursors
from data.get_config_data import ReadConfig

class OperationMysql:
    def __init__(self):
        # 接收初始化的数据
        config = ReadConfig()
        self.host = config.get_mysql_config_var('db_host')
        self.port = int(config.get_mysql_config_var('db_port'))
        self.user = config.get_mysql_config_var('db_user')
        self.pwd = config.get_mysql_config_var('db_pwd')
        self.name = config.get_mysql_config_var('db_name')
        self.charset = config.get_mysql_config_var('db_charset')

        # 准备结果存储最后的结果
        self.result = []
        # 定义一个变量高速程序是否执行成功
        self.flag = False # True表示执行成功，False表示执行失败
        # 需要一个变量存储异常信息
        self.msg = ""



    def select_fetchall(self,sql:str):
        mysql_conn = ""
        try:
            # 实例化数据库连接
            mysql_conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,db=self.name,charset=self.charset)
            # 实例化一个游标指针
            cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL语句
            cursor.execute(sql)
            # 获取执行的结果
            self.result = list(cursor.fetchall())
            self.flag = True

        except Exception as e:
            # 如果出现异常，flag = False,捕获系统给的错误信息
            self.flag = False
            self.msg = "连接数据库操作出现异常，具体原因：" + str(e)
            print(self.msg)
        else:
            cursor.close()
            mysql_conn.close()
            return self.result

    def select_fetchone(self,sql:str):
        mysql_conn = ""
        try:
            # 实例化数据库连接
            mysql_conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,db=self.name,charset=self.charset)
            # 实例化一个游标指针
            cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL语句
            cursor.execute(sql)
            # 获取执行的结果
            self.result = cursor.fetchone()
            self.flag = True

        except Exception as e:
            # 如果出现异常，flag = False,捕获系统给的错误信息
            self.flag = False
            self.msg = "连接数据库操作出现异常，具体原因：" + str(e)
            print(self.msg)
        else:
            cursor.close()
            mysql_conn.close()
            return self.result


    def update_db(self,sql:str):
        mysql_conn = ""
        try:
            # 实例化数据库连接
            mysql_conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,db=self.name,charset=self.charset)
            # 实例化一个游标指针
            cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL语句
            cursor.execute(sql)
            # 向数据库提交数据
            mysql_conn.commit()

            self.flag = True
        except Exception as e:
            # 如果出现异常，flag = False,捕获系统给的错误信息
            # 对提交的数据进行回滚
            mysql_conn.rollback()
            self.msg = "连接数据库操作出现异常，具体原因：" + str(e)
            self.flag = False
        else:
            cursor.close()
            mysql_conn.close()


op = OperationMysql()
sql = "select * from student;"
d = op.select_fetchall(sql)
print(d)

sql = "select * from student where id=2;"
d = op.select_fetchone(sql)
print(d)


# s = "insert into student values(3,'王五',23);"
# x = op.update_db(s)
# k = op.msg
#
# print(k)


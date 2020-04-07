# coding = utf-8
"""
@Time      : 2020/2/21 0021 17:42
@Author    : YunFan
@File      : get_config_data.py
@Software  : PyCharm
@Version   : 1.0
@Description: 读取配置文件中的值
"""

from configparser import ConfigParser

class ReadConfig:
    """读取配置文件"""
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("../test_data/config.ini", encoding='utf-8')

    def get_email_config_var(self,name):
        value = self.config.get('EMAIL', name)
        return value

    def get_http_config_var(self,name):
        value = self.config.get('HTTP', name)
        return value

    def get_mysql_config_var(self,name):
        value =self.config.get('DATABASE', name)
        return value

    def get_servers_config_var(self,name):
        value = self.config.get('SERVERS', name)
        return value

    def get_filePath_config_var(self,name):
        value = self.config.get('FILEPATH', name)
        return value

    def get_logger_config_var(self,name):
        value = self.config.get('LOGGER',name)
        return value


if __name__ == '__main__':
    # 调用实例
    read_config = ReadConfig()
    s = eval(read_config.get_http_config_var('timeout'))
    print(type(s))
    print('EMAIL中的sender值为：',read_config.get_email_config_var('sender'))
    print('HTTP中的scheme值为：',read_config.get_http_config_var('timeout'))
# coding = utf-8
"""
@Time      : 2020/2/28 0028 13:21
@Author    : YunFan
@File      : get_headers_cookies.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from utils.operation_json import OperationJson

class GetHeadersCookies:
    def __init__(self):
        self.op_json = OperationJson()

    def get_headers_value(self):
        return self.op_json.get_key_words("header")

    def get_cookies_value(self):
        return self.op_json.get_key_words("cookie")

if __name__ == '__main__':
    g = GetHeadersCookies()
    print(g.get_headers_value())
    print(g.get_cookies_value())

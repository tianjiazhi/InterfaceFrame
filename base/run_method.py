# coding = utf-8
"""
@Time      : 2020/2/8 0008 13:29
@Author    : YunFan
@File      : run_method.py.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
# print(res.status_code)
# print(res.encoding)
# print(res.headers)
# print(res.request.headers)
# print(res.content)
# print(res.cookies)

import requests
import json
from data.get_config_data import ReadConfig


class RunMethod:
    def __init__(self):
        self.read_config = ReadConfig()
        self.timeout = eval(self.read_config.get_http_config_var('timeout'))

    def get_main(self,url,data=None,headers=None,cookies=None):
        res = None
        if headers is not None and cookies is not None:
            res = requests.get(url=url, data=data, headers=headers, cookies=cookies, timeout=self.timeout,verify=False)
        elif headers is not None and cookies is None:
            res = requests.get(url=url, data=data, headers=headers,timeout=self.timeout,verify=False)
        elif headers is None and cookies is not None:
            res = requests.get(url=url, data=data, cookies=cookies, timeout=self.timeout,verify=False)
        else:
            res = requests.get(url=url, data=data, timeout=self.timeout,verify=False)
        return res.json()


    def post_main(self,url,data=None,headers=None,cookies=None):
        res = None
        if headers is not None and cookies is not None:
            res = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=self.timeout,verify=False)
        elif headers is not None and cookies is None:
            res = requests.post(url=url, data=data, headers=headers,timeout=self.timeout,verify=False)
        elif headers is None and cookies is not None:
            res = requests.post(url=url, data=data, cookies=cookies, timeout=self.timeout,verify=False)
        else:
            res = requests.post(url=url, data=data, timeout=self.timeout,verify=False)
        return res.json()


    def run_method(self,method,url,data=None,headers=None,cookies=None):
        res = None
        if method.lower() == 'post':
            res = self.post_main(url,data,headers,cookies)
        elif method.lower() == 'get':
            res = self.get_main(url,data,headers,cookies)
        else:
            return "接口请求方式暂时不支持"
        """
            # ensure_ascii=False会输出真正的中文，否则会输出ASCII字符
            # sort_keys=True 是告诉编码器按照字典key排序(a到z)输出。
            # indent参数根据数据格式缩进显示，读起来更加清晰, indent的值，代表缩进空格式
        """
        return json.dumps(res,ensure_ascii=False)


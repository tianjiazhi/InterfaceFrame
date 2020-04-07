# coding = utf-8
"""
@Time      : 2020/2/18 0018 19:04
@Author    : YunFan
@File      : login_authorization.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

import requests
import json
from requests import utils
from utils.operation_json import OperationJson


class GetAuthorization:
    def __init__(self):
        self.session = requests.session()
        self.operation_json = OperationJson("../test_data/json_data/user.json")
        self.url = self.operation_json.get_key_words("login_url")
        self.data = self.operation_json.get_key_words("login_data")
        self.header = self.operation_json.get_key_words("header")
        self.cookie = {}
        self.context = {}


    def do_login(self):
        """登录操作"""
        res = self.session.post(url=self.url, data=self.data)
        status_code = res.status_code
        if status_code == 200:
            return res.json()
        else:
            return "登录失败"


    def api_authorize(self,data):
        res = requests.get(url=data)
        request_headers = res.request.headers
        cookie_jar = res.cookies
        response_cookie = utils.dict_from_cookiejar(cookie_jar)
        request_cookie = request_headers['Cookie']
        return request_cookie,response_cookie


    def data_transducer(self,string: str) -> dict:
        """
        :param string: token=eyJ0eXAiOiJK; auth_id=bd43fe2426081aa5a8b0a2773d006f70; auth_sys=d41d8cd98f00b204e9800998ecf8427e
        :return: {'token': 'eyJ0eXAiOiJK', 'auth_id': 'bd43fe2426081aa5a8b0a2773d006f70', 'auth_sys': 'd41d8cd98f00b204e9800998ecf8427e'}
        """
        dic = {}
        for s in string.split("; "):
            d = s.split("=")
            dic[d[0]] = d[1]
        return dic


    def get_authorization(self):
        do_login_res = self.do_login()
        link_url = do_login_res['info']
        api_authorize = list(self.api_authorize(link_url))

        request_cookie = self.data_transducer(api_authorize[0])
        response_cookie = api_authorize[1]

        self.cookie.update(response_cookie)
        self.cookie.update(request_cookie)
        token = self.cookie['token']
        self.cookie.pop("token")

        X_XSRF_TOKEN = response_cookie['XSRF-TOKEN']
        Authorization =  "Bearer " + token

        self.header['X-XSRF-TOKEN'] = X_XSRF_TOKEN
        self.header['Authorization'] = Authorization
        self.context['cookie'] = self.cookie
        self.context['header'] = self.header

        content = json.dumps(self.context,ensure_ascii=False,indent=2,sort_keys=True)

        file_path = "../test_data/json_data/header_cookie.json"
        self.operation_json.write_data(file_path,content)


get = GetAuthorization()
get.get_authorization()








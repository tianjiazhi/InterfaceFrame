# coding = utf-8
"""
@Time      : 2020/2/9 0009 13:31
@Author    : YunFan
@File      : mock_demo.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

from mock import mock
import json

def mock_test(mock_method, request_data, url, method, response_data):
    """

    :param mock_method:调用的方法名
    :param request_data:请求数据
    :param url:
    :param method: post/get
    :param response_data:响应数据
    :return:
    """
    mock_method = mock.Mock(return_value=response_data)
    print("mock_method",mock_method)
    res = mock_method(url, method, json.dumps(request_data))
    return res





# res1 = mock_test(self.run.run_main, data, url, 'POST', 'ssssssss')
# print('res1:', res1)

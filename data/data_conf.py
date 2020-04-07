# coding = utf-8
"""
@Time      : 2020/2/7 0007 18:47
@Author    : YunFan
@File      : data_conf.py.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

class global_val:

    case_id = 0                 # case_id
    name = 1                    # 名称
    url = 2                     # url
    is_run = 3                  # 是否运行
    request_method = 4          # 请求类型
    is_add_headers = 5          # 是否添加请求头
    is_add_cookies = 6          # 是否添加cookies
    case_depend = 7             # case依赖
    data_depend = 8             # 响应数据依赖
    filed_depend = 9            # 请求数据中的依赖字段
    request_data = 10           # 请求数据
    expect_result = 11          # 预期结果
    real_results = 12           # 实际结果


def get_id():
    return global_val.case_id

def get_name():
    return global_val.name

def get_url():
    return global_val.url

def get_run():
    return global_val.is_run

def get_request_method():
    return global_val.request_method

def get_request_header():
    return global_val.is_add_headers

def get_request_cookie():
    return global_val.is_add_cookies

def get_case_depend():
    return global_val.case_depend

def get_data_depend():
    return global_val.data_depend

def get_filed_depend():
    return global_val.filed_depend

def get_request_data():
    return global_val.request_data

def get_expect_result():
    return global_val.expect_result

def get_real_results():
    return global_val.real_results

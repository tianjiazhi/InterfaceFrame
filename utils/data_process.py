# coding = utf-8
"""
@Time      : 2020/3/1 0001 13:04
@Author    : YunFan
@File      : data_process.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import json


def str_to_dict(string:str)->dict:
    """
    功能描述：将字符串转换成为字典类型的数据
    :param string: 待处理的字符串：参数格式:param1=value1&param2=value2
    :return dictionary：字典类型的数据
    """
    dictionary = {}
    if string is None or string == '':
        return dictionary
    # 分割每一个键值对赋值给变量pp
    pp = string.split("&")
    # 遍历被分割的列表类型的键值对
    for s in pp:
        # 分割每个参数的键和值
        ppp = s.split("=")
        try:
            dictionary[ppp[0]] = ppp[1]
        except Exception as e:
            dictionary[ppp[0]] = None
    json_str1 = json.dumps(dictionary,ensure_ascii=False)
    json_str2 = json.dumps(dictionary, ensure_ascii=False, indent=4)
    print("<class  'str'> 打印原始的的json数据：{0}\n    {1}".format("->"*40,json_str1))
    print("<class  'str'> 打印美化后的json数据：{0}\n    {1}".format("->"*40,json_str2))
    print("<class 'dict'> 打印字典类型的数据：  {0}\n    {1}".format("->"*40,dictionary))
    return dictionary


def dict_to_str(dictionary:dict)->str:
    """
    功能描述：将字典类型的数据转换成为字符串
    :param dictionary: 待处理的字典类型的数据。 {'size': '10', 'page': '1'}
    :return string: 经过处理后的字符串类型的数据，返回格式：size=10&page=1
    """
    string = ''
    list_data = ["{0}={1}&".format(k,v) for k,v in dictionary.items()]
    for index,value in enumerate(list_data):
        string = string + value
    string = string[0:-1]   # 截取最后一个取消&符号
    print("<class 'str'> 打印转换后的字符串数据：{0}\n    {1}".format("->" * 40, string))
    return string


def print_dict_key_value(dictionary:dict,output_format = 1):
    """
    该方法可用来调试代码
    :param dictionary:  字典数据
    :param output_format:
    :return:
    """
    for key,values in dictionary.items():
        if output_format == 2:
            print("{0}={1}".format(key, values))   # key=values格式
        else:
            print("{0}: {1}".format(key, values))  # 浏览器上的请求参数格式

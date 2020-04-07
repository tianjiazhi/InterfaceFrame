# coding = utf-8
"""
@Time      : 2020/2/18 0018 17:32
@Author    : YunFan
@File      : demo.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

# import unittest
#
# class TestMethod(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("类执行之前的方法")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("类执行之后的方法")
#
#
#     def setUp(self):
#         """每次方法之前运行"""
#         print("test--setUp")
#
#     def tearDown(self):
#         """每次方法之后执行"""
#         print("test--tearDown")
#
#     def test_01(self):
#         print("这是测试方法1")
#
#     def test_02(self):
#         print("这是测试方法2")
#
#
# if __name__ == "__main__":
#     unittest.main()

# 数据依赖定义关系


#
# a = '[["sheet2", "case_id_20"], ["sheet2", "case_id_21"], ["sheet3", "case_id_32"], ["sheet3", "case_id_34"]]'
# a = eval(a)
#
# r = [["res_20_001", "res_20_003", "res_20_006"], ["res_21_005", "res_21_006", "res_21_008"],["res_32_002", "res_32_003"], ["res_34_002", "res_34_007"]]
# print(a)
# print(r)
# for i, j in zip(a, r):
#     print(i, j)















from jsonpath_rw import jsonpath,parse

# json_file = {'foo': [{'baz': 1}, {'baz': 2}]}
# jsonpath_expr = parse('foo.[*].baz')
#
# # 提取值
# value = [match.value for match in jsonpath_expr.find(json_file)]
# print(value)   # [1, 2]
#
#
# # 匹配记得他们来自何处
# full_path = [str(match.full_path) for match in jsonpath_expr.find(json_file)]
# print(full_path)  # ['foo.[0].baz', 'foo.[1].baz']
#
#
# # 对于没有ID的数据位自动提供ID（当前为全局开关）
# jsonpath.auto_id_field = 'id'
# jsonpath_expr = parse('foo[*].id')
# json_file = {'foo': [{'id': 'bizzle'}, {'baz': 3}]}
# d = [match.value for match in jsonpath_expr.find(json_file)]
# print(d)
#
#
# json_file = {'a': {'x': {'b': 1, 'c': 'number one'}, 'y': {'b': 2, 'c': 'number two'}}}
# # jsonpath_expr = parse('a.*.b.`parent`.c')
# jsonpath_expr = parse("$.*.`this`")
# # 一个方便的扩展:像' parent '这样的命名操作符
# d = [match.value for match in jsonpath_expr.find(json_file)]
# print(d)
#
#
#
#
#
#
# # # You can also build expressions directly quite easily
# # # 您还可以很容易地直接构建表达式
# # from jsonpath_rw.jsonpath import Fields
# # from jsonpath_rw.jsonpath import Slice
# #
# # jsonpath_expr_direct = Fields('foo').child(Slice('*')).child(Fields('baz'))  # This is equivalent
#
#
# """
#     1、	$  -->根节点对象
#     2、 `this`   -->当前节点对象
#     3、`parent`  -->点前节点的父节点
#     4、filed   --> 	指定字段
#         fieldname    字段（来自“当前”对象）
#         "fieldname"  字段，用于允许在字段名中使用特殊字符
#         'fieldname'  字段，用于允许在字段名中使用特殊字符
#         *            任意字段
#         field,field  任何一个命名字段（您始终可以使用|来构建等效的jsonpath ）
#
#
#     5、[filed] -->  指定字段,与4相同
#     6、[idx]   -->	数组访问
#         [n]	数组索引（可以是逗号分隔的列表）
#         [start：end]	数组切片（请注意，仅由于到目前为止没有必要，才执行该步骤）
#         [*]	任何数组索引
#
# """
#
# json_file = {'foo': [{'baz': [1,2,3,4]}, {'baz': 2}]}
# jsonpath_expr = parse('foo.[0].baz.[1:3]')
#
#
# # 提取值
# value = [match.value for match in jsonpath_expr.find(json_file)][0]
# print(value)   # [1, 2]

#
#
# def update_json_data(request_data_dict,key_expr,value):
#     key = key_expr.split(".")
#     key_length = len(key)
#     get_json_data = request_data_dict
#
#     counter = 0
#     while counter < key_length:
#         key_value = key[counter]
#         if key_value.startswith('[') and key_value.endswith(']'):
#             key_value = eval(key_value[1:-1])
#         if counter + 1 == key_length:
#             get_json_data[key_value] = value
#         else:
#             get_json_data = get_json_data[key_value]
#         counter = counter + 1
#     return request_data_dict
#
#
#
# def get_data_for_key(request_data,response_data,filed_depend,data_depend):
#     """根据依赖的key去获取执行依赖的case的响应，然后返回"""
#
#     for key, value in zip(filed_depend, data_depend):
#         jsonpath_expr_value = parse(value)
#         var_value = [match.value for match in jsonpath_expr_value.find(response_data)][0]
#         request_data = update_json_data(request_data,key,var_value)
#     return request_data
#
#
#
# response_data = { "store":{
#      "book":[
#       { "category":"参考",
#          "author":"Nigel Rees",
#          "title":"世纪风俗",
#          "price":8.95
#       },
#       { "category":"小说",
#          "author":"Evelyn Waugh",
#          "title":"荣誉剑",
#          "price":12.99
#       },
#       { "category":"小说",
#          "author":"Herman Melville",
#          "title":"Moby Dick",
#          "isbn":"0-553-21311-3",
#          "price":8.99
#       },
#       { "category":"小说",
#          "author":"JRR Tolkien",
#          "title":"指环王",
#          "isbn":"0-395-19395-8",
#          "price":22.99
#       }
#     ],
#     " bicycle":{
#        " color":"red",
#        " price":19.95
#     }
#   }
# }



# a = update_json_data(response_data,'store.book.[1].title',"修改内容")
# print(a)

# a = [{'category': '参考', 'author': 'Nigel Rees', 'title': '世纪风俗', 'price': 8.95}, {'category': '小说', 'author': 'Evelyn Waugh', 'title': '荣誉剑', 'price': 12.99}]
# print()



# s = '1'
# b= eval(s)
# print(a[b])




# request_data = {"parent_key1":{"parent_key2":[{"child_key11":1,"child_key12":2},{"child_key21":1,"child_key22":2}]}}
#
# data_depend = ['store.book.[2].title','store.book.[3].title']
# filed_depend = ['parent_key1.parent_key2.[0].child_key11','parent_key1.parent_key2.[1].child_key22']
#
# print(request_data)
# d = get_data_for_key(request_data,response_data,filed_depend,data_depend)
# print(d)
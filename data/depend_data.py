# coding = utf-8
"""
@Time      : 2020/2/24 0024 14:08
@Author    : YunFan
@File      : depend_data.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from base.run_method import RunMethod
from data.get_data import GetData
from utils.operation_excel import OperationExcel
from jsonpath_rw import jsonpath,parse
import json

class DependentData:

    def __init__(self,request_data,case_depend:list,data_depend:list,filed_depend:list):
        """

        :param case_depend: ['sheet_name','case_id']
        :param data_depend: ['store.book.[2].title','store.book.[3].title']
        :param filed_depend:['parent_key2.[0].child_key11','parent_key2.[1].child_key22']
        """
        self.request_data = request_data
        self.case_depend = case_depend
        self.sheet_name = self.case_depend[0]
        self.case_id = self.case_depend[1]
        self.data_depend = data_depend
        self.filed_depend = filed_depend
        self.operation_excel = OperationExcel()
        self.data = GetData()


    def update_json_data(self,key_expr:str,value:str):
        """
        将提取到的结果更新到 请求头 数据当中
        :param key_expr:请求头数据的key 'parent_key2.[0].child_key11'
        :param value: 从响应结果中获取到的值
        :return:
        """
        key = key_expr.split(".")
        key_length = len(key)
        get_json_data = self.request_data

        counter = 0
        while counter < key_length:
            key_value = key[counter]
            if key_value.startswith('[') and key_value.endswith(']'):
                key_value = eval(key_value[1:-1])
            if counter + 1 == key_length:
                get_json_data[key_value] = value
            else:
                get_json_data = get_json_data[key_value]
            counter = counter + 1
        return self.request_data


    def run_dependent(self):
        """执行依赖测试，获取结果"""
        # 通过sheet页名称读取对应sheet页的数据
        self.data.get_sheet_data(self.sheet_name)
        # 通过sheet_name和case_id获取行号
        row_num = self.operation_excel.get_rowNum_by_sheetName_and_caseId(self.sheet_name, self.case_id)


        url = self.data.get_request_url(row_num)
        method = self.data.get_request_method(row_num)
        request_data = self.data.get_request_data(self.sheet_name, row_num)

        headers = self.data.get_is_header(row_num)
        cookies = self.data.get_is_cookie(row_num)

        run_method = RunMethod()

        res = run_method.run_method(method,url,request_data,headers,cookies)
        return json.loads(res)


    def get_data_for_key(self):
        """根据依赖的key去获取执行依赖的case的响应，然后返回响应数据"""
        # 执行依赖测试，获取结果
        response_data = self.run_dependent()
        for request_key, response_key in zip(self.filed_depend, self.data_depend):
            json_path_expr_value = parse(response_key)
            # 根据依赖数据的json_path表达式从响应结果中提取依赖值
            var_value = [match.value for match in json_path_expr_value.find(response_data)][0]
            # 将提取到的结果更新到 请求头 数据当中
            self.request_data = self.update_json_data(request_key, var_value)
        return self.request_data



if __name__ == "__main__":
    lists = ['Sheet2', 'case_id_20']
    # d = DependentData(lists)
    # # d.get_case_line_data()
    # d.get_data_for_key()


# coding = utf-8
"""
@Time      : 2020/2/7 0007 19:12
@Author    : YunFan
@File      : get_data.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from data.get_config_data import ReadConfig
from data.get_headers_cookies import GetHeadersCookies
from utils.operation_excel import OperationExcel
from utils.operation_json import OperationJson
from data import data_conf



def string_to_eval(row_num:int,col_num:int,string: str):
    try:
        eval_value = eval(string)
    except Exception as e: # 异常时返回None
        error = "(行号:{0},列号:{1})异常信息:{2}".format(row_num,col_num,e)
        print(error)
        return False
    else:
        return eval_value


class GetData:
    def __init__(self):
        self.operation_excel = OperationExcel()
        self.get_headers_cookies  = GetHeadersCookies()
        self.get_config = ReadConfig()

    def get_sheet_names(self):
        """获取当前工作簿中所有工作表的名称"""
        return self.operation_excel.get_sheet_names()

    def get_sheet_data(self,sheet_name):
        """通过sheet页名称读取对应sheet页的数据"""
        return self.operation_excel.get_sheet_data(sheet_name)

    def get_sheet_lines(self):
        """获取当前sheet页的总行数"""
        return self.operation_excel.get_sheet_lines()

    def get_json_file_name(self,sheet_name):
        """获取json文件名称"""
        sheet_name = "../test_data/json_data/" + sheet_name + ".json"
        return sheet_name

    def get_save_result_path(self):
        '''获取结果文件路径'''
        return self.operation_excel.save_result_path



    def get_is_run(self, x):
        """获取case是否运行"""
        flag = None
        y = data_conf.get_run()
        run_value = self.operation_excel.get_cell_value(x, y)
        if run_value.lower() == 'yes':
            flag = True
        else:
            flag = False
        return flag


    def get_is_header(self, x):
        """是否携带headers"""
        y = data_conf.get_request_header()
        header = self.operation_excel.get_cell_value(x, y)

        if header == 'yes':
            return self.get_headers_cookies.get_headers_value()
        else:
            return None


    def get_is_cookie(self, x):
        """是否携带cookies"""
        y = data_conf.get_request_cookie()
        cookie = self.operation_excel.get_cell_value(x, y)
        if cookie == 'yes':
            return self.get_headers_cookies.get_cookies_value()
        return None


    def get_request_method(self, x):
        """获取请求方法"""
        y = data_conf.get_request_method()
        request_method = self.operation_excel.get_cell_value(x, y)
        return request_method


    def get_request_url(self, x):
        """获取请求地址"""
        y = data_conf.get_url()
        request_url = self.operation_excel.get_cell_value(x, y)
        base_url = self.get_config.get_http_config_var('baseurl')
        request_url = base_url + request_url
        return request_url


    def get_request_data(self, sheet_name,x):
        """获取请求数据"""
        y = data_conf.get_request_data()
        request_data_key = self.operation_excel.get_cell_value(x, y)
        if request_data_key == '':
            return None
        else:
            request_data = self.__get_data_for_json(sheet_name,request_data_key)
            return request_data


    def __get_data_for_json(self, sheet_name, request_data_key):
        """通过excel中关键字去获取json数据"""
        sheetName = self.get_json_file_name(sheet_name)
        op_json = OperationJson(file_path = sheetName)
        data = op_json.get_key_words(request_data_key)
        return data



    def get_expect_data(self, x):
        """获取预期结果数据"""
        y = data_conf.get_expect_result()
        expect_data = self.operation_excel.get_cell_value(x, y)
        if expect_data == '':
            return None
        else:
            return string_to_eval(x,y,expect_data)


    def get_module_name(self, x):
        """获取模块名称"""
        y = data_conf.get_name()
        module_name = self.operation_excel.get_cell_value(x, y)
        return module_name


    def write_real_result(self,sheet_name,row,value):
        """写测试结果到excel"""
        y = data_conf.get_real_results()
        self.operation_excel.write_value(sheet_name,row,y,value)


    def get_is_case_depend(self,x):
        """判断是否有case依赖"""
        y = data_conf.get_case_depend()
        case_depend = self.operation_excel.get_cell_value(x, y)
        if case_depend == "":
            return None
        else:
            return string_to_eval(x,y,case_depend)


    def get_depend_data(self,x):
        """获取响应结果中的依赖字段"""
        y = data_conf.get_data_depend()
        data_depend = self.operation_excel.get_cell_value(x,y)
        if data_depend == "":
            return None
        else:
            return string_to_eval(x,y,data_depend)

    def get_depend_filed(self,x):
        """获取数据依赖字段"""
        y = data_conf.get_filed_depend()
        filed_depend = self.operation_excel.get_cell_value(x, y)
        if filed_depend == "":
            return None
        else:
            return string_to_eval(x,y,filed_depend)


if __name__ == '__main__':
    get_data = GetData()
    d = get_data.get_is_run(1)
    print(d)

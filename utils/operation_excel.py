# coding = utf-8
"""
@Time      : 2020/2/7 0007 16:52
@Author    : YunFan
@File      : operation_excel.py.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import os,xlrd
from xlutils.copy import copy

from utils.get_time import get_format_time


class OperationExcel:

    def __init__(self,srcfile = None):
        if srcfile:
            self.srcfile = srcfile
        else:
            self.srcfile = '../test_data/interface_template.xlsx'
        format_time = get_format_time('%Y%m%d%H%M%S')
        self.save_result_path = "../result/report/InterfaceResult_" + format_time + ".xlsx"
        self.copy_workbook = self.copy_excel_file()
        self.workbook = None
        self.sheet_id  = 0
        self.sheet = self.open_workbook()
        self.rows = 0                 # 初始化当前sheet页的总行数
        self.row = 0                  # 初始化逐行读取时的行数


    def copy_excel_file(self):
        if os.path.isfile(self.srcfile):
            xlrd.Book.encoding = "utf8"
            workbook = xlrd.open_workbook(self.srcfile)
            write_data = copy(workbook)
            write_data.save(self.save_result_path)
        else:
            error = "%s 文件不存在!" % self.srcfile
            return error


    def open_workbook(self):
        """打开要读取的文件"""
        # 设置读取excel使用的utf8编码
        xlrd.Book.encoding = "utf8"
        # 读取excel内容到缓存workbook
        self.workbook = xlrd.open_workbook(filename=self.save_result_path)
        self.sheet = self.workbook.sheets()[self.sheet_id]
        return self.sheet



    def map_id_by_sheet_name(self,sheet_name):
        """通过表名称映射id"""
        sheet_name_list = self.get_sheet_names()
        if sheet_name in sheet_name_list:
            self.sheet_id = sheet_name_list.index(sheet_name)
            return self.sheet_id
        else:
            return "工作表名称：%s当前工作簿中不存在，请检查后重试！"%sheet_name


    def get_sheet_data(self,sheet_name):
        '''通过sheet_name，切换sheet页'''
        self.sheet_id = self.map_id_by_sheet_name(sheet_name)
        self.sheet = self.workbook.sheets()[self.sheet_id]
        return self.sheet


    def get_sheet_names(self):
        """获取当前工作簿中所有sheet页面的名称"""
        sheets = self.workbook.sheet_names()
        return sheets


    def get_sheet_lines(self):
        """获取当前sheet页的总行数"""
        self.rows = self.sheet.nrows
        return self.rows


    def get_cell_value(self,row,col):
        '''获取单元格中的内容'''
        return self.sheet.cell_value(row,col)


    def write_value(self,sheet_name,row,col,value):
        '''写数据到excel中'''
        workbook = xlrd.open_workbook(self.save_result_path)
        write_data = copy(workbook)
        sheet_id = self.map_id_by_sheet_name(sheet_name)
        sheet_data = write_data.get_sheet(sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.save_result_path)



    def get_rowNum_by_sheetName_and_caseId(self, sheet_name, case_id):
        """根据sheet_name和case_id获取行号"""
        self.sheet = self.get_sheet_data(sheet_name)
        row_num = self.get_row_num(case_id)
        return row_num


    def get_row_num(self,case_id):
        """通过case_id找到对应的行号"""
        row_num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return row_num
            row_num = row_num + 1


    def get_cols_data(self,col_id=None):
        '''获取某一列的内容'''
        if col_id is not None:
            cols = self.sheet.col_values(col_id)
        else:
            cols = self.sheet.col_values(0)
        return cols

    # def get_row_value(self,row_num):
    #     """根据行号，找到该行的内容"""
    #     row_data = self.sheet.row_values(row_num)
    #     return row_data


if __name__ == "__main__":

    reader = OperationExcel()
    sheetName = reader.get_sheet_names()   # 获取当前工作簿中所有工作表的名称
    print(sheetName)

    for sheet in sheetName:
        reader.get_sheet_data(sheet)       # 通过sheet页名称读取对应sheet页的数据
        rows = reader.get_sheet_lines()    # 获取sheet页的总行数
        for i in range(1,rows):
            print("工作表：%s-->行号：%d"% (sheet, i))
            print(reader.get_cell_value(i,1))    #
            reader.write_value("Sheet3",i,12,"我爱中国人")
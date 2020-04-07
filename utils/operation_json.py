# coding = utf-8
"""
@Time      : 2020/2/7 0007 17:54
@Author    : YunFan
@File      : operation_json.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import json

class OperationJson:
    def __init__(self, file_path = None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = "../test_data/json_data/header_cookie.json"
        self.data = self.__read_data()


    def __read_data(self):
        with open(self.file_path,encoding='utf-8') as f:
            data = json.load(f)
            return data

    def write_data(self,file_path,context):
        """将数据写到指定json文件中"""
        with open(file_path,"w+") as file:
            file.write(context)


    def get_key_words(self, key=None):
        """获取json文件中的数据"""
        if key:
            return self.data[key]
        else:
            return self.data


if __name__ == '__main__':
    reader_json = OperationJson("../test_data/json_data/test.json")
    # print(reader_json.get_key_words())
    res = reader_json.get_key_words("data")
    print(res)

    res = json.dumps(res, ensure_ascii=False, indent=4)
    print(res)







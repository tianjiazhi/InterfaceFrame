# coding = utf-8
"""
@Time      : 2020/2/27 0027 11:47
@Author    : YunFan
@File      : public_util.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

class PublicUtil:

    def is_contain(self,expect_list:list,result:str)->bool:
        """
        判断一个字符串是否包含另一个字符串
        :param expect: 期望结果 例如：['"category":"参考"','"title":"世纪风俗"','"category":"小说"']
        :param result: 响应结果
        :return:
        """
        flags = True
        for expect in expect_list:
            flag = None
            if str(expect) in result:
                flag = True
            else:
                flag = False
            flags = flags and flag
        return flags






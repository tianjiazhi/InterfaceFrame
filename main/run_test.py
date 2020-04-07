# coding = utf-8
"""
@Time      : 2020/2/8 0008 13:54
@Author    : YunFan
@File      : run_test.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
from base.run_method import RunMethod
from data.depend_data import DependentData
from data.get_config_data import ReadConfig
from data.get_data import GetData
from utils.operation_json import OperationJson
from utils.public_util import PublicUtil
from utils import logger
from utils.send_email import SendEmail

log = logger.logger
class RunTest(object):

    def __init__(self):
        read_conf = ReadConfig() # 邮件发送开关
        self.is_on = read_conf.get_email_config_var('on_off')
        self.run_method = RunMethod()
        self.data = GetData()
        self.public_util = PublicUtil()
        self.headers_and_cookies = OperationJson()
        self.cookies = self.headers_and_cookies.get_key_words("cookie")
        self.headers = self.headers_and_cookies.get_key_words("header")


    def request_depend_logic(self, request_data, depend_case, depend_data, depend_filed, sheet, row_count):

        if depend_case == False:
            error = "工作表{0}中的第{1}行的case_id字段的数据类型错误". \
                format(sheet, row_count + 1)
            log.error(error)
            return

        if not isinstance(depend_case, list):
            error = "工作表{0}中的第{1}行的case_id字段值外层数据不是列表类型的数据" \
                .format(sheet, row_count + 1)
            log.error(error)
            return

        if depend_data is None or depend_data == False:
            error = "工作表{0}中的第{1}行的depend_data字段值不可为空或者数据类型错误". \
                format(sheet, row_count + 1)
            log.error(error)
            return

        if not isinstance(depend_data, list):
            error = "工作表{0}中的第{1}行填写的depend_data字段值外层数据不是列表类型的数据". \
                format(sheet, row_count + 1)
            log.error(error)
            return

        if depend_filed is None or depend_filed == False:
            error = "工作表{0}中的第{1}行的depend_filed字段值不可为空或者数据类型错误！". \
                format(sheet, row_count + 1)
            log.error(error)
            return

        if not isinstance(depend_filed, list):
            error = "工作表{0}中的第{1}行的depend_filed字段值外层数据不是列表类型的数据". \
                format(sheet, row_count + 1)
            log.error(error)
            return

        if not (len(depend_case) == len(depend_data) == len(depend_filed)):
            error = "工作表{0}中的第{1}行填写的depend_case,depend_data,depend_filed三个外层列表的长度不相等" \
                .format(sheet, row_count + 1)
            log.error(error)
            return error

        for case_depend, data_depend, filed_depend in zip(depend_case, depend_data, depend_filed):

            if not isinstance(case_depend, list):
                error = "工作表{0}中的第{1}行的case_id字段值内层数据“{2}”不是列表类型的数据" \
                    .format(sheet, row_count + 1, case_depend)
                log.error(error)
                return

            if len(case_depend) != 2:
                error = "工作表{0}中的第{1}行的case_id字段值内层数据列表“{2}”的长度不等于2" \
                    .format(sheet, row_count + 1, case_depend)
                log.error(error)
                return

            if not isinstance(data_depend, list):
                error = "工作表{0}中的第{1}行的data_depend字段值内层数据“{2}”不是列表类型的数据" \
                    .format(sheet, row_count + 1, data_depend)
                log.error(error)
                return

            if not isinstance(filed_depend, list):
                error = "工作表{0}中的第{1}行的filed_depend字段值内层数据“{2}”不是列表类型的数据" \
                    .format(sheet, row_count + 1, filed_depend)
                log.error(error)
                return

            if len(data_depend) != len(filed_depend):
                error = "工作表{0}中的第{1}行的depend_data和depend_filed字段的内层列表数据{2}和{3}的长度不相等" \
                    .format(sheet, row_count + 1, data_depend, filed_depend)
                log.error(error)
                return

            depend_data = DependentData(request_data, case_depend, data_depend, filed_depend)
            request_data = depend_data.get_data_for_key()
        return request_data


    def run_case_logic(self):
        res = None
        pass_list = []
        fail_list = []
        result_path = self.data.get_save_result_path()  # 获取结果文件路径
        sheetName = self.data.get_sheet_names()         # 获取当前工作簿中所有工作表的名称
        for sheet in sheetName:
            self.data.get_sheet_data(sheet)             # 通过sheet页名称读取对应sheet页的数据
            row_counts = self.data.get_sheet_lines()    # 获取sheet页的总行数
            for row_count in range(1, row_counts):
                log.info("工作表：{0}-->行号：{1} {2}".format(sheet, row_count,"="*200))
                is_run = self.data.get_is_run(row_count)
                if is_run:
                    url = self.data.get_request_url(row_count)
                    log.info("请求地址：  {}".format(url))

                    method = self.data.get_request_method(row_count)
                    log.info("请求方法：  {}".format(method))

                    request_data = self.data.get_request_data(sheet, row_count)
                    log.info("请求数据：  {}".format(request_data))

                    header = self.data.get_is_header(row_count)
                    log.info("请求头部：  {}".format(header))

                    cookies = self.data.get_is_cookie(row_count)
                    log.info("Cookies：  {}".format(cookies))

                    expect_list = self.data.get_expect_data(row_count)
                    log.info("预期结果：  {}".format(expect_list))

                    depend_case = self.data.get_is_case_depend(row_count)


                    if depend_case is not None:# 处理依赖关系
                        log.info("开始处理接口之间的依赖关系流程{}".format(">"*150))
                        log.info("依赖case：  {}".format(depend_case))

                        depend_data = self.data.get_depend_data(row_count)
                        log.info("依赖数据：  {}".format(depend_data))

                        depend_filed = self.data.get_depend_filed(row_count)
                        log.info("依赖字段：  {}".format(depend_filed))

                        request_data = self.request_depend_logic(request_data,depend_case,depend_data,depend_filed,sheet,row_count)
                        log.info("更新请求数据:{}".format(request_data))
                        log.info("结束处理接口之间的依赖关系流程{}".format("<" * 150))

                    res = self.run_method.run_method(method, url, request_data, header, cookies)

                    if self.public_util.is_contain(expect_list,res):
                        self.data.write_real_result(sheet,row_count,'pass')
                        pass_list.append([sheet,row_count])
                    else:
                        log.info("结果比对fail的响应{}".format(res))
                        self.data.write_real_result(sheet,row_count, res)
                        fail_list.append([sheet,row_count])

        return pass_list,fail_list,result_path


    def run(self):
        # 运行所有case
        result = list(self.run_case_logic())
        # 发送邮件
        if self.is_on == 'on':
            sendEmail = SendEmail()
            sendEmail.send_email(result[0],result[1],result[2])
            log.info("本次测试完成，已将测试结果通过邮件发送至各位，请注意查收！")
        else:

            log.info("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")

if __name__ == '__main__':
    RunTest().run()


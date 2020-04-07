# coding = utf-8
"""
@Time      : 2020/2/29 0029 8:45
@Author    : YunFan
@File      : logger.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import logging
from logging.handlers import TimedRotatingFileHandler
from data.get_config_data import ReadConfig
from utils.get_time import get_format_time


class Logger(object):

    def __init__(self, logger_name='logs…'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)

        get_config_var = ReadConfig()
        format_time = get_format_time('%Y%m%d_%H%M%S')
        # 日志文件的名称
        self.log_file_short_path = get_config_var.get_logger_config_var('log_file_save_path')
        # 最多存放日志的数量
        self.backup_count = int(get_config_var.get_logger_config_var('log_save_count'))
        # 打印在控制台上的日志输出级别
        self.console_output_level = get_config_var.get_logger_config_var('console_output_level')
        # ;写在日志文件中的日志输出级别
        self.file_output_level = get_config_var.get_logger_config_var('file_output_level')
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        """"""
        if not self.logger.handlers:  # 避免重复日志

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)



            # 每隔一个小时重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=self.log_file_short_path, when='H',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)

        return self.logger

logger = Logger().get_logger()















# # 创建一个logger
# self.logger = logging.getLogger(logger)
# self.logger.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
# log_path = '../../logs/'
# log_name = log_path + rq + '.log'
# fh = logging.FileHandler(log_name)
# fh.setLevel(logging.INFO)
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
#
# # 定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 给logger添加handler
# self.logger.addHandler(fh)
# self.logger.addHandler(ch)
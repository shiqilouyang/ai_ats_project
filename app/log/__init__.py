import logging
import os
import time
from logging.handlers import RotatingFileHandler

from conf.Setting import userId


class DevelopmentConfig(object):
    LOG_LEVEL = logging.DEBUG


class SetLog():
    def __init__(self,u=None):
        self.DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
        self.rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.userid = u  if u  else  userId
        self.log_path = os.path.join( \
            os.path.dirname(os.path.realpath(__file__)), "{}.log".format(self.userid))
        self.loger = self.setup_log()

    def setup_log(self):
        logging.basicConfig(level=DevelopmentConfig.LOG_LEVEL,datefmt=self.DATE_FORMAT)
        file_log_handler = RotatingFileHandler(
            self.log_path, maxBytes=1024 * 1024 * 100, backupCount=10,encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
        file_log_handler.setFormatter(formatter)
        loger = logging.getLogger()
        # 为 loger 绑定 上述 格式
        loger.addHandler(file_log_handler)
        return loger

    def __getattr__(self, e):
        log_match = {
            "info": self.loger.info,
            "debug": self.loger.debug,
            "error": self.loger.error,
            "warn": self.loger.warn,
        }
        if e in log_match.keys():
            return log_match.get(e)


loger = SetLog()
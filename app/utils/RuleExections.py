import ctypes
import inspect

from log import loger


class NetWorkRxections(Exception):
    def __init__(self,exename,code):
        self.exename = exename
        self.code = code
    def __str__(self):
        loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
        " .format(self.exename,self.code))


class ReleSubjetOverRxections(Exception):
    def __init__(self,exename,max,current):
        self.exename = exename
        self.current = current
        self.max = max
    def __str__(self):
        loger.info("知识点{} \
        推送题目个数超出,最多 {},现在是{} " \
              .format(self.exename,self.max,self.current))


class ReleSubjetMvOverRxections(ReleSubjetOverRxections):
    def __str__(self):
        loger.info("知识点{} \
        推送视频题目个数超出,最多 {},现在是{} " \
              .format(self.exename,self.max,self.current))


class ReleSubjetIntervictiveOverRxections(ReleSubjetOverRxections):
    def __str__(self):
        loger.info("知识点{} \
        推送互动题目个数超出,最多 {},现在是{} " \
              .format(self.exename,self.max,self.current))


class ReleSubjetMixOverRxections(ReleSubjetOverRxections):
    def __str__(self):
        loger.info("知识点{} \
        推送混合(学习加测试)题目个数超出,最多 {},现在是{} " \
              .format(self.exename,self.max,self.current))


class UserNotExist(Exception):
    def __init__(self,current):
        self.current = current
    def __str__(self):
        loger.info("用户{} 不存在 " \
              .format(self.current))


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
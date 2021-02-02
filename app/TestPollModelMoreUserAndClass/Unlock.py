import json
import os

import requests


from log import loger
from conf.Setting import *
from utils.RuleExections import NetWorkRxections


class Unlock():
    def __init__(self,data,i = None):
        self.loger = loger
        self.url = UNlockProdUrl

        self.data = {
            "token": "debug",
            "userId": userId if i is None else i,
            "accountId": accountId,
            "courseId": data.get("course_id"),
            "classIds": data.get("class_id"),
            "sectionId": data.get("section_id"),
            "requestId": rand,
            "times": ticks
        }
        self.header = {'Content-Type': 'application/json'}


    def testUnlock(self):
        from app import at
        loger.info("UserId is {}".format(userId))
        loger.info("解锁请求参数为 : {}".format(str(self.data)))
        res1 = requests.post(url=self.url, data=json.dumps(self.data), headers=self.header)
        if json.loads(res1.text).get("message") == "解锁课程不存在":
            loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
                    ".format("解锁 ", res1.status_code))
            at(501,res1.text)
            raise NetWorkRxections("解锁 ",res1.status_code)
        else:
            pass

        loger.info("用户 {} 解锁请求响应{}".format(userId, res1.text))
        self.loger.info("解锁完成，请求返回状态码为 {} "\
                        .format(res1.status_code))

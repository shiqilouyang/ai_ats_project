import json

import requests

from conf.Setting import *
from log import loger
from utils.RuleExections import NetWorkRxections


class GetSession():

    def __init__(self,data, i = None):
        self.url = GetSessionProdUrl

        self.data = {
            "token": "debug",
            "userId": userId if i is None else i,
            "accountId": accountId,
            "courseId": data.get("course_id"),
            "sectionId": data.get("section_id"),
            "requestId": rand,
            "redoNum": "1"
        }
        self.loger = loger
        self.header = {'Content-Type': 'application/json'}

    def testGetSessionId(self):
        from app import at
        loger.info("获取 sessionId请求的参数为 {}".format(str(self.data)))
        res1 = requests.post(url=self.url, data=json.dumps(self.data), headers=self.header)
        if json.loads(res1.text).get("message") == "getSession失败":
            at(501, res1.text)
            loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
                                ".format("获取sessionId ", res1.status_code))
            raise NetWorkRxections("获取 sessionId ",res1.status_code)

        self.loger.info("开始获取 sessionID，请求返回状态码为 {} SessionId为：{}"\
                        .format(res1.status_code,json.loads(res1.text)["result"]["sessionId"]))
        self.loger.info("获取 sessionId 完成 ,响应为{}".format(res1.text))
        return json.loads(res1.text)["result"]["sessionId"]

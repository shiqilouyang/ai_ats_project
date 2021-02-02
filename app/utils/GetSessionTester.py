import json
from imp import reload

import requests

from TestPoolModel.model import OperationtableTester
from TestPoolModel.model import db
from conf.Setting import *


class GetSessionTester():

    def __init__(self,body):
        self.body = body
        if self.body.get("env")=="4":
            self.url = GetSessionProdUrl
        if self.body.get("env")=="2":
            self.url = GetSessionProdUrl_test
        if self.body.get("env")=="3":
            self.url = GetSessionPreUrl
        self.db = db
        self.data = {
            "token": "debug",
            "userId": self.body.get("u"),
            "accountId": accountId,
            "courseId": self.body.get("courseId"),
            "sectionId": self.body.get("sectionId"),
            "requestId": rand,
            "redoNum": "1"
        }
        self.loger = self.body.get("loger")
        self.header = {'Content-Type': 'application/json','grayTestList': \
                           'W3siY29kZSI6IkRZTkFNSUNfVEFSR0VUIiwibmFtZSI6Ilx1ODFlYVx1NTJhOFx1N2I1NFx1Njg0OCJ9LHsiY29kZSI6IlRSQUNJTkdCQUNLIiwibmFtZSI6Ilx1NWY1Mlx1NGUwMFx1NTMxNlx1OGZmZFx1NjgzOVx1NmVhZlx1NmU5MCJ9XQ'}

    def testGetSessionId(self):
        loger = self.loger
        loger.info("获取 sessionId请求的参数为 {}".format(str(self.data)))
        try:
            res1 = requests.post(url=self.url, data=json.dumps(self.data), headers=self.header,timeout = 5)
        except Exception as e:
            loger.error("异常为{}".format(e))
            loger.error("获取 sessionId响应的参数 {}".format(res1.text))
            OperationtableTester.query.filter(OperationtableTester.rid == self.body.get("rid")).update({
                OperationtableTester.status: "ERROR",
                OperationtableTester.message: "getSession失败",
                OperationtableTester.starttime: int(round(time.time()))
            })
            self.db.session.commit()
            self.db.session.close()
            loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
                                ".format("获取sessionId ", res1.status_code))
            # raise NetWorkRxections("获取 sessionId ",res1.status_code)
        if json.loads(res1.text).get("message") == "getSession失败":
            loger.info("获取 sessionId响应的参数 {}".format(res1.text))
            OperationtableTester.query.filter(OperationtableTester.rid == self.body.get("rid")).update({
                OperationtableTester.status: "ERROR",
                OperationtableTester.message: "getSession失败",
                OperationtableTester.starttime: int(round(time.time()))
            })
            self.db.session.commit()
            self.db.session.close()
            loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
                                            ".format("获取sessionId ", res1.status_code))
        self.loger.info("开始获取 sessionID，请求返回状态码为 {} SessionId为：{}"\
                        .format(res1.status_code,json.loads(res1.text)["result"]["sessionId"]))
        self.loger.info("获取 sessionId 完成 ,响应为{}".format(res1.text))
        import logging
        reload(logging)
        logging.shutdown()
        return json.loads(res1.text)["result"]["sessionId"]

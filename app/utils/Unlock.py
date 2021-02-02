import json
from imp import reload

import requests

from TestPoolModel.model import Operationtable
from TestPoolModel.model import db
from conf.Setting import userId, UNlockProdUrl_test, UNlockProdUrl, accountId, rand, ticks, UNlockPreUrl


class Unlock():
    def __init__(self,body):
        self.loger = body.get("loger")
        self.body =  body
        if self.body.get("env")=="4":
            self.url = UNlockProdUrl
        if self.body.get("env")=="2":
            self.url = UNlockProdUrl_test
        if self.body.get("env")=="3":
            self.url = UNlockPreUrl
        self.u = self.body.get("u")
        self.db = db
        self.data = {
            "token": "debug",
            "userId": self.u,
            "accountId": accountId,
            "courseId": self.body.get("courseId"),
            "classIds": self.body.get("classIds"),
            "sectionId": self.body.get("sectionId"),
            "requestId": rand,
            "times": ticks
        }
        self.header = {'Content-Type': 'application/json', \
                       'grayTestList': \
                           'W3siY29kZSI6IkRZTkFNSUNfVEFSR0VUIiwibmFtZSI6Ilx1ODFlYVx1NTJhOFx1N2I1NFx1Njg0OCJ9LHsiY29kZSI6IlRSQUNJTkdCQUNLIiwibmFtZSI6Ilx1NWY1Mlx1NGUwMFx1NTMxNlx1OGZmZFx1NjgzOVx1NmVhZlx1NmU5MCJ9XQ'}



    def testUnlock(self):
        loger = self.loger
        loger.info("UserId is {}".format(self.u))
        loger.info("解锁请求参数为 : {}".format(str(self.data)))
        loger.info("解锁请求url 是 {}".format(self.url))
        operationtable = Operationtable(
            user_id=self.data.get("userId"),
            status="RUNNIG"
        )
        self.db.session.add_all([operationtable])
        self.db.session.commit()
        self.db.session.close()
        try:
            res1 = requests.post(url=self.url, data=json.dumps(self.data), headers=self.header,timeout = 3)
        except Exception as e:
            loger.error("异常为{}".format(e))
            import time
            reload(time)
            Operationtable.query.filter(Operationtable.user_id == self.data.get("userId")).update({
                Operationtable.status: "ERROR",
                Operationtable.message: "解锁失败",
                Operationtable.starttime:int(round(time.time()))

            })
            self.db.session.commit()
            self.db.session.close()
            import logging
            reload(logging)
            logging.shutdown()
            loger.error("{} 请求失败，返回状态码是 {}，请检查请求参数和 URL \
                    ".format("解锁 ", res1.status_code))
        if json.loads(res1.text).get("message") == "解锁课程不存在":
            import time
            reload(time)
            Operationtable.query.filter(Operationtable.user_id == self.data.get("userId")).update({
                Operationtable.status: "ERROR",
                Operationtable.message: "解锁失败",
                Operationtable.starttime: int(round(time.time()))

            })
            self.db.session.commit()
            self.db.session.close()
            import logging
            reload(logging)
            logging.shutdown()
        loger.info("解锁响应{}".format(res1.text))
        loger.info("用户 {} 解锁请求响应{}".format(userId, res1.text))
        self.loger.info("解锁完成，请求返回状态码为 {} "\
                        .format(res1.status_code))

import copy
import json
import threading
from imp import reload
from pprint import pprint

import requests

from TestPoolModel.model import models_, OperationtableTester
from TestPoolModel.model import  db
from conf.Setting import *
from log import SetLog



from utils.GetSessionTester import GetSessionTester
from utils.UnlockTester import UnlockTester

# {'courseId': '10000840', 'classIds': ['10000842'], 'sectionId': '10000841', 'rate': 0.classes, 'env': 1, 'user_name': 'xs1', 'u': 'xfl-4684-1607661580'}
class interfaceEngineTester():
    def __init__(self,body = None):
        self.model_data = {}
        self.body = body
        self.loger = SetLog(body.get("u"))
        # self.u = body.get("")
        # if self.body.get("env")=="4":
        #     self.nextActivityProdUrl = nextActivityProdUrl
        #     self.submitEventProUrl = submitEventProdUrl
        if self.body.get("env")=="2":
            self.nextActivityProdUrl = nextActivityProdUrl_test
            self.submitEventProUrl = submitEventProUrl_test
        # if self.body.get("env")=="3":
        #     self.nextActivityProdUrl = nextActivityPreUrl
        #     self.submitEventProUrl = submitEventPreUrl

        self.db = db
        self.a = rateConf(self.body.get("rate"))
        self.g = (x for x in self.a.rataList_1 * 1000)
        self.sessionId = ""
        self.module = {
            "testmodule": {"testModelExeList": [], "testModuleNum": 0, "loCodes": {"number": 0}},
            "studymodule": {
                "intervictivestartModelExeList": [],
                "mixstartModelExeList": [],
                "mvstartModelExeList": [],
                "studymoduleNum": 0, "loCodes": {},
                "mvNum": {}, "intervictive": {}, "mix": {}},
            "restudymodule": {"mvrestartModelExeList": [],
                              "mixrestartModelExeList": [], "restudymoduleNum": 0, "loCodes": {},
                              "mix": {}, "mvNum": {}},
            "countDict": {}
        }

    #  下一步 根据 sessionId 智能推荐下一步
    def nextActivity(self, sessionId, model_data):
        loger = self.loger
        data = {
            "appId": "1",
            "requestId": rand,
            "sessionId": sessionId,
            "token": "debug"
        }
        header = {'Content-Type': 'application/json'}
        loger.info("获取下一步 请求参数为 {}".format(str(data)))
        res3 = requests.post(url=self.nextActivityProdUrl, data=json.dumps(data), headers=header)
        activityType = res3.json()['result']['data'][0]['activityType']
        usage = res3.json()['result']['data'][0]['usage']
        itemId = res3.json()['result']['data'][0]['itemId']
        itemForm = res3.json()['result']['data'][0]['itemForm']
        loCode = res3.json()['result']['data'][0]['ncode']
        curPoolCode = res3.json()['result']['section']['curPoolCode']
        loger.info("根据 sessionId {} ,获取下一步。当前知识点为 {} ".format(sessionId, loCode))
        loger.info("获取下一步响应内容{}".format(res3.text))
        self.model_data.update({"curPoolCode": curPoolCode,
                                "studylonum": res3.json()['result']['section']["studyLoNum"],
                                'prePoolCode': res3.json()['result']['section']["prePoolCode"],
                                'unlockLoNum': res3.json()['result']['section']["unlockLoNum"],
                                'curlocode': res3.json()['result']['section']["curLoCode"],
                                'preLoCode': res3.json()['result']['section']["preLoCode"]
                                })
        return itemId, usage, activityType, loCode, itemForm, curPoolCode

    def Module(self, itemId, usage, activityType, loCode, itemForm, ale_result_record):
        loger = self.loger
        loCodes = self.module.get("studymodule")["loCodes"]
        self.model_data.update({"usage": usage, "activityType": activityType})
        if loCode in loCodes:
            loCodes[loCode] = loCodes.get(loCode) + 1
            self.model_data.update({"loCode": loCode})
        else:
            loCodes[loCode] = 1
            self.model_data.update({"loCode": loCode})

        if activityType == 'RVIDEO' or activityType == 'LO':
            data = {
                "sensor": "FINISH",
                "requestId": ticks,
                "sendTime": ticks,
                "token": "debug",
                "sessionId": self.sessionId,
                "data": [{
                    "actor": userId,
                    "action": "FINISHED",
                    "object": {
                        "itemId": itemId,
                        "itemType": usage,
                        "duration": rand11,
                        "endTime": ticks,
                        "startTime": ticks
                    },
                    "eventTime": ticks,
                    "appId": "10.10.10.77"
                }]
            }

        elif activityType == 'DQUEST':
            h2 = next(self.g)
            data = {
                "token": "debug",
                "sessionId": self.sessionId,
                "requestId": rand,
                "sensor": "ASSESSMENTITEM",
                "sendTime": ticks,
                "data": [{
                    "actor": userId,
                    "action": "SUBMITTED",
                    "object": {
                        "loCode": loCode,
                        "score": h2,
                        "totalScore": totalScore,
                        "itemId": itemId,
                        "itemType": usage,
                        "itemForm": itemForm,
                        "startTime": ticks,
                        "endTime": ticks,
                        "duration": rand11,
                        "systemResult": h2,
                        "subItems": []
                    },
                    "eventTime": ticks,
                    "appId": "10.10.10.77"
                }]
            }
        header = {'Content-Type': 'application/json',
                  'grayTestList': 'W3siY29kZSI6IkRZTkFNSUNfVEFSR0VUIiwibmFtZSI6Ilx1ODFlYVx1NTJhOFx1N2I1NFx1Njg0OCJ9LHsiY29kZSI6IlRSQUNJTkdCQUNLIiwibmFtZSI6Ilx1NWY1Mlx1NGUwMFx1NTMxNlx1OGZmZFx1NjgzOVx1NmVhZlx1NmU5MCJ9XQ'}
        loger.info(" 知识点 {} 重在学习模块 请求参数为 {}".format(loCode,data))
        res4 = requests.post(url=self.submitEventProUrl, data=json.dumps(data), headers=header)
        re_ = json.loads(res4.text)
        if re_["result"] !=None and re_["result"]['sessionId'] != None:
            self.model_data.update({"itemId" : itemId,
                "ability": re_["result"]["loObject"]["ability"],
                                    "initAbility": re_["result"]["loObject"]["initAbility"],
                                    "starttime": data["data"][0]["object"]["startTime"],
                                    "duration": data["data"][0]["object"]["duration"],
                                    "score": data["data"][0]["object"]["score"] if "score" in data["data"][0][
                                        "object"] else ""
                                    })
            ale_result_record1 = ale_result_record(
                session_id=self.model_data.get("session_id"),
                user_id=self.model_data.get("user_id"),
                class_id=self.model_data.get("class_id"),
                course_id=self.model_data.get("course_id"),
                section_id=self.model_data.get("section_id"),
                user_name=self.model_data.get("user_name"),
                env=self.model_data.get("env"),
                itemId = self.model_data.get("itemId") if self.model_data.get("itemId") else "",
                activityType=self.model_data.get("activityType"),
                usage=self.model_data.get("usage"),
                loCode=self.model_data.get("loCode"),
                ability=self.model_data.get("ability"),
                initability=self.model_data.get("initAbility"),
                curPoolCode=self.model_data.get("curPoolCode"),
                studylonum=self.model_data.get("studylonum"),
                prePoolCode=self.model_data.get("prePoolCode"),
                unlockLoNum=self.model_data.get("unlockLoNum"),
                curlocode=self.model_data.get("curlocode"),
                preLoCode=self.model_data.get("preLoCode"),
                starttime=self.model_data.get("starttime"),
                duration=self.model_data.get("duration"),
                score=self.model_data.get("score"),
                rate=self.model_data.get("rate")
            )
            self.db.session.add_all([ale_result_record1])
            self.db.session.commit()
            self.db.session.close()
            loger.info(" 当前模块是{}模块,提交做题 activityType/知识点 是 {}/{} 记录接口返回：{}" \
                       .format(self.model_data.get("curPoolCode"),activityType, str(loCode), res4.text))
            loger.info("{}模块响应{}".format(self.model_data.get("curPoolCode"),res4.text))
        else:
            ale_result_record1 = ale_result_record(
                session_id=self.model_data.get("session_id"),
                user_id=self.model_data.get("user_id"),
                class_id=self.model_data.get("class_id"),
                course_id=self.model_data.get("course_id"),
                section_id=self.model_data.get("section_id"),
                user_name=self.model_data.get("user_name"),
                env=self.model_data.get("env"),
                activityType=self.model_data.get("activityType"),
                usage=self.model_data.get("usage"),
                loCode=self.model_data.get("loCode"),
                ability=0.0,
                initability=0.0,
                curPoolCode=self.model_data.get("curPoolCode"),
                studylonum=self.model_data.get("studylonum"),
                prePoolCode=self.model_data.get("prePoolCode"),
                unlockLoNum=self.model_data.get("unlockLoNum"),
                curlocode=self.model_data.get("curlocode"),
                preLoCode=self.model_data.get("preLoCode"),
                starttime=ticks,
                duration=rand11,
                score='null',
                rate=self.model_data.get("rate")
            )
            self.db.session.add_all([ale_result_record1])
            self.db.session.commit()
            self.db.session.close()
            loger.info(" 当前模块是{}模块,提交做题 activityType/知识点 是 {}/{} 记录接口返回：{}" \
                       .format(self.model_data.get("curPoolCode"), activityType, str(loCode), res4.text))
            loger.info("{}模块响应{}".format(self.model_data.get("curPoolCode"), res4.text))

    def run(self):
        loger = self.loger
        self.body.update({
            "loger":loger
        })
        unlock = UnlockTester(self.body)
        ale_result_record = models_.get(unlock.data.get("userId")[-1])
        loger.info("当前数据库是 Ale_result_record_{}".format(unlock.data.get("userId")[-1]))
        rid_ = unlock.testUnlock()
        self.model_data.update({"user_id": unlock.data.get("userId"),
                                "course_id": unlock.data.get("courseId"),
                                "section_id": unlock.data.get("sectionId"),
                                "user_name":self.body.get("user_name"),
                                "env":self.body.get("env"),
                                "class_id": ",".join(unlock.data.get("classIds")),
                                'rid':rid_
                                })
        import time
        from imp import reload
        reload(time)
        OperationtableTester.query.filter(OperationtableTester.rid == rid_).update({
            OperationtableTester.course_id: unlock.data.get("courseId"),
            OperationtableTester.section_id: unlock.data.get("sectionId"),
            OperationtableTester.user_name: self.body.get("user_name"),
            OperationtableTester.env: self.body.get("env"),
            OperationtableTester.rate: self.body.get("rate"),
            OperationtableTester.class_id: ",".join(unlock.data.get("classIds")),
            OperationtableTester.starttime: int(round(time.time())),
            OperationtableTester.thid: str(threading.current_thread().ident)
        })
        db.session.commit()
        db.session.close()
        self.body.update({'rid':rid_})
        getSession = GetSessionTester(self.body)
        self.sessionId = getSession.testGetSessionId()
        self.model_data.update({"session_id": self.sessionId,"rate":self.body.get("rate")})
        OperationtableTester.query.filter(OperationtableTester.rid == rid_).update({
            OperationtableTester.session_id: self.sessionId,
        })
        db.session.commit()
        db.session.close()
        countDict = {"DQUEST": 0, "RVIDEO": 0, "LO": 0}
        loger.info(self.model_data)
        import time
        from imp import reload
        reload(time)
        a = time.time()
        while True:
            from imp import reload
            reload(time)
            b = time.time()
            if b > a + 600:
                loger.error("到了10min规定时间，停止")
                OperationtableTester.query.filter(OperationtableTester.rid == rid_).update({
                    OperationtableTester.status: "ERROR",
                    OperationtableTester.message: "到了10min规定时间，停止"
                })
                db.session.commit()
                db.session.close()
                import logging
                reload(logging)
                logging.shutdown()
                break
            # Opstatus = OperationtableTester.query.filter(OperationtableTester.user_id == unlock.data.get("userId")).first().status
            Opstatus = self.db.session.query(OperationtableTester).filter(OperationtableTester.rid == rid_).first()
            self.db.session.close()
            if Opstatus.status == "RUNNIG":
                loger.info("状态是 RUNNING 状态")
                itemId, usage, activityType, loCode, itemForm, curPoolCode = self.nextActivity(self.sessionId,
                                                                                               self.model_data)
                if activityType == 'DQUEST' or activityType == 'RVIDEO' or activityType == 'LO':
                    countDict[activityType] = countDict.get(activityType) + 1
                    self.Module(itemId, usage, activityType, loCode, itemForm, ale_result_record)
                else:
                    loger.info(self.module)
                    loger.info("状态为退出：" + activityType)
                    loger.info("测试结束！")
                    loger.info("测试成功 {}".format(self.model_data.get("user_name")))
                    OperationtableTester.query.filter(OperationtableTester.rid == rid_).update({
                        OperationtableTester.status: "END",
                        OperationtableTester.message: "做题成功"
                    })
                    db.session.commit()
                    db.session.close()
                    import logging
                    reload(logging)
                    logging.shutdown()
                    # ruleChech(userId, self.sessionId,self.body.get("groupId"))  #335889686564130816
                    from TestPoolModel.model import Exercese_rule
                    group_id_from_sql = Exercese_rule.query.filter(Exercese_rule.rule_groupId == self.body.get("groupId")).first()
                    break
            if Opstatus.status == "KILL":
                loger.error("手动终止程序")
                break
        from utils.csvMaker import CsvMaker
        CsvMaker(self.model_data.get("user_id"), self.model_data.get("session_id")).make()
        return self.model_data.get("session_id"),self.model_data.get("user_id")


def moreTask1(body):
    def asynctask1(bodys):
        h = bodys.get("classIds")
        bodys.update({
            "classIds" : h if h.find(",") == "-1" else h.split(",")
        })
        return  interfaceEngineTester(bodys).run()
    data = {}
    list_data = []
    for k, v in body.items():
        if k != 'classList':
            data.update({k: v})
    for item in body.get('classList'):
        section__find = [1]
        for i in section__find:
            item.update({
                "groupId": "NONE"
            })
        list_data.append(item)
    for i in list_data:
        print(i)
        i.update(data)
        t = threading.Thread(target=asynctask1, args=(i,))
        t.setDaemon(True)
        t.start()
        t.join()
#
if __name__ == '__main__':
    from conf.Setting import utils_init_path, userId
    u = userId
    rq = {'classList': [
        # {"classIds": "10003071",
        #  "courseId": "10003067",
        #  "sectionId": "10003070"},

        {"classIds": "10003073",
         "courseId": "10003067",
         "sectionId": "10003072"}

        # {"classIds": "10003050",
        #  "courseId": "10003048",
        #  "sectionId": "10003049"},
        #
        # 冲刺章
        # {"classIds": "10003092,10003093",
        #  "courseId": "10003090",
        #  "sectionId": "10003091"}
               ],
             'env': '2',
             'rate': [0.25,0.35,0.5,0.75,1],
             'u': 'xfl-4684-16081188447',
             'user_name': 'xushuai'}
    body = rq
    rate_list = rq.get("rate")
    th_list = []
    for i in rate_list:
        bodys = copy.deepcopy(body)
        import time
        reload(time)
        bodys.update({
            "u": "autoTest-xfl-4684-" + str(int(round(time.time()))) + str(i).replace('.','') ,
            "rate": i
        })
        t = threading.Thread(target=moreTask1, args=(bodys,))
        th_list.append(t)
    for th in th_list:
        th.start()
    for t in th_list:
        t.join()




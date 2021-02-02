import json

import requests
from flask_sqlalchemy import SQLAlchemy



from conf.Setting import *
from log import loger
from TestPollModelMoreUserAndClass.GetSession import GetSession
from TestPollModelMoreUserAndClass import Unlock

class interfaceEngineTesterMoreUser():
    def __init__(self,rate = None,i = None):
        from app import app
        self.rate = rate
        self.i = i
        self.model_data = {}
        self.nextActivityProdUrl = nextActivityProdUrl
        self.submitEventProUrl = submitEventProUrl
        self.db = SQLAlchemy(app)
        self.a = rateConf(rate)
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
    def nextActivity(self, sessionId):
        from utils import classIds
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

    def testModule(self, itemId, usage, activityType, loCode, itemForm, ale_result_record):
        loCodes = self.module.get("testmodule")["loCodes"]
        self.model_data.update({"usage": usage, "activityType": activityType})
        if loCode in loCodes:
            self.model_data.update({"loCode": loCode})
            loCodes[loCode] = loCodes.get(loCode) + 1
        else:
            self.model_data.update({"loCode": loCode})
            loCodes[loCode] = 1

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
            h = next(self.g)
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
                        "score": h,
                        "totalScore": totalScore,
                        "itemId": itemId,
                        "itemType": usage,
                        "itemForm": itemForm,
                        "startTime": ticks,
                        "endTime": ticks,
                        "duration": rand11,
                        "systemResult": h,
                        "subItems": []
                    },
                    "eventTime": ticks,
                    "appId": "10.10.10.77"
                }]
            }
        header = {'Content-Type': 'application/json'}
        res4 = requests.post(url=self.submitEventProUrl, data=json.dumps(data), headers=header)
        re_ = json.loads(res4.text)
        self.model_data.update({"ability": re_["result"]["loObject"]["ability"],
                                "initAbility": re_["result"]["loObject"]["initAbility"],
                                "starttime": data["data"][0]["object"]["startTime"],
                                "duration": data["data"][0]["object"]["duration"],
                                "score": data["data"][0]["object"]["score"] if "score" in data["data"][0][
                                    "object"] else ""
                                })
        ale_result_record1 = ale_result_record(
            session_id=self.model_data.get("session_id"),
            user_id=self.model_data.get("user_id"),
            class_id="_".join(self.model_data.get("class_id")),
            course_id=self.model_data.get("course_id"),
            section_id=self.model_data.get("section_id"),
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
        loger.info("测试模块的请求参数为: {}".format(str(data)))
        loger.info(" 当前模块是测试模块,提交做题 activityType/知识点 是 {}/{} 记录接口返回：{}" \
                   .format(activityType, str(loCode), res4.text))
        loger.info("测试模块响应{}".format(res4.text))

    def restudyModule(self, itemId, usage, activityType, loCode, itemForm, ale_result_record):
        loCodes = self.module.get("restudymodule")["loCodes"]
        self.model_data.update({"usage": usage, "activityType": activityType})
        if loCode in loCodes:
            self.model_data.update({"loCode": loCode})
            loCodes[loCode] = loCodes.get(loCode) + 1
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
            h1 = next(self.g)
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
                        "score": h1,
                        "totalScore": totalScore,
                        "itemId": itemId,
                        "itemType": usage,
                        "itemForm": itemForm,
                        "startTime": ticks,
                        "endTime": ticks,
                        "duration": rand11,
                        "systemResult": h1,
                        "subItems": []
                    },
                    "eventTime": ticks,
                    "appId": "10.10.10.77"
                }]
            }
        header = {'Content-Type': 'application/json'}
        res4 = requests.post(url=self.submitEventProUrl, data=json.dumps(data), headers=header)
        re_ = json.loads(res4.text)
        self.model_data.update({"ability": re_["result"]["loObject"]["ability"],
                                "initAbility": re_["result"]["loObject"]["initAbility"],
                                "starttime": data["data"][0]["object"]["startTime"],
                                "duration": data["data"][0]["object"]["duration"],
                                "score": data["data"][0]["object"]["score"] if "score" in data["data"][0][
                                    "object"] else ""
                                })
        from utils import classIds
        ale_result_record1 = ale_result_record(
            session_id=self.model_data.get("session_id"),
            user_id=self.model_data.get("user_id"),
            class_id="_".join(self.model_data.get("class_id")),
            course_id=self.model_data.get("course_id"),
            section_id=self.model_data.get("section_id"),
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
        loger.info("重学习模块的 请求参数为 {}".format(str(data)))
        loger.info(" 当前模块是重学习模块,提交做题 activityType/知识点 是 {}/{} 记录请求返回接口：{}" \
                   .format(activityType, str(loCode), res4.text))
        loger.info("重学习模块请求响应{}".format(res4.text))

    def studyModule(self, itemId, usage, activityType, loCode, itemForm, ale_result_record):
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
        header = {'Content-Type': 'application/json'}
        loger.info("学习模块的 请求参数为 {}".format(str(data)))
        res4 = requests.post(url=self.submitEventProUrl, data=json.dumps(data), headers=header)
        re_ = json.loads(res4.text)
        self.model_data.update({"ability": re_["result"]["loObject"]["ability"],
                                "initAbility": re_["result"]["loObject"]["initAbility"],
                                "starttime": data["data"][0]["object"]["startTime"],
                                "duration": data["data"][0]["object"]["duration"],
                                "score": data["data"][0]["object"]["score"] if "score" in data["data"][0]["object"] else ""
                                })
        ale_result_record1 = ale_result_record(
            session_id=self.model_data.get("session_id"),
            user_id=self.model_data.get("user_id"),
            class_id="_".join(self.model_data.get("class_id")),
            course_id=self.model_data.get("course_id"),
            section_id=self.model_data.get("section_id"),
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
        loger.info(" 当前模块是学习模块,提交做题 activityType/知识点 是 {}/{} 记录接口请求返回：{}".format(activityType, str(loCode), res4.text))
        loger.info("学习模块响应{}".format(res4.text))

    def run(self,data):
        unlock = Unlock.Unlock(data,self.i)
        from TestPoolModel.model import Ale_test_result_record
        ale_result_record = Ale_test_result_record
        loger.info("当前数据库是 Ale_result_record_{}".format(unlock.data.get("userId")[-1]))
        unlock.testUnlock()
        self.model_data.update({"user_id": unlock.data.get("userId"),
                                "course_id": unlock.data.get("courseId"),
                                "section_id": unlock.data.get("sectionId"),
                                "class_id" :data.get("class_id")
                                })

        session = GetSession(data,self.i)
        self.sessionId = session.testGetSessionId()
        self.model_data.update({"session_id": self.sessionId,"rate":self.rate})
        countDict = {"DQUEST": 0, "RVIDEO": 0, "LO": 0}
        while True:
            itemId, usage, activityType, loCode, itemForm, curPoolCode = self.nextActivity(self.sessionId)
            if activityType == 'DQUEST' or activityType == 'RVIDEO' or activityType == 'LO':
                countDict[activityType] = countDict.get(activityType) + 1
                if curPoolCode == "TEST_MODULE":
                    loger.info("开始执行测试模块")
                    self.testModule(itemId, usage, activityType, loCode, itemForm, ale_result_record)
                if curPoolCode == "RESTUDY_MODULE":
                    loger.info("开始执行重学习模块")
                    self.restudyModule(itemId, usage, activityType, loCode, itemForm, ale_result_record)
                if curPoolCode == "STUDY_MODULE":
                    loger.info("开始执行学习模块")
                    self.studyModule(itemId, usage, activityType, loCode, itemForm, ale_result_record)
                if curPoolCode == "SECTION_OVER":
                    break
            else:
                loger.info(self.module)
                loger.info("状态为退出：" + activityType)
                loger.info("测试结束！")
                break
        return [self.model_data.get("user_id"),self.model_data.get("session_id")]

#
# if __name__ == '__main__':
#     interfaceEngineTesterOneUser().run({'course_id': 10004604, 'class_id': ['10005784', '10005785', '10005786'], 'section_id': 10005783})
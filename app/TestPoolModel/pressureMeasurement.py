import json
import random
import time
from pprint import pprint

from locust import task, between, HttpUser, SequentialTaskSet

accountId = "autoTest-xfl-468464722054645611402"
ticks = int(round(time.time()))
rand = random.randint(0, 9999999)
rand11 = random.randint(60, 240)
rand12 = random.randint(0, 1)

# {'accountId': 'autoTest-xfl-468464722054645611402',
#  'courseId': '10003067',
#  'redoNum': '1',
#  'requestId': 9012897,
#  'sectionId': '10003068',
#  'token': 'debug',
#  'userId': 'autoTest-xfl-4684-16106960861'}

class UserTask(SequentialTaskSet):

    # header = {'Content-Type': 'application/json', \
    #                'grayTestList': \
    #                    'W3siY29kZSI6IkRZTkFNSUNfVEFSR0VUIiwibmFtZSI6Ilx1ODFlYVx1NTJhOFx1N2I1NFx1Njg0OCJ9LHsiY29kZSI6IlRSQUNJTkdCQUNLIiwibmFtZSI6Ilx1NWY1Mlx1NGUwMFx1NTMxNlx1OGZmZFx1NjgzOVx1NmVhZlx1NmU5MCJ9XQ'}

    header = {'Content-Type': 'application/json'}
    sessionId = ''
    u = None
    g = (x for x in "10" * 1000)

    def on_start(self):
        self.u = "autoTest-xfl-4684-" + str(int(round(time.time())))

    @task
    def unlock(self):
        self.data = {
            "token": "debug",
            "userId": self.u ,
            "accountId": accountId,
            "courseId": '10003067',
            "classIds": ['10003069'],
            "sectionId": '10003068',
            "requestId": rand,
            "times": ticks
        }
        self.data = json.dumps(self.data)
        r = self.client.post("/v1/recom/unlock",self.data,headers = self.header)
        unlock_re = json.loads(r.text)
        # print(self.u)
        assert unlock_re['code'] == "200"

    @task
    def getsession(self):
        data = {  'accountId': accountId,
                         "courseId": '10003067',
                         'redoNum': '1',
                         'requestId': rand,
                         'sectionId': '10003068',
                         'token': 'debug',
                         'userId': self.u
                     }
        data = json.dumps(data)
        r = self.client.post("/v1/recom/getSession",data,headers=self.header)
        self.sessionId = json.loads(r.text)["result"]["sessionId"]
        assert json.loads(r.text).get("code") == "200"

    def nextActivity(self,sessionId):
        data = {
            "appId": "1",
            "requestId": rand,
            "sessionId": sessionId,
            "token": "debug"
        }
        res3 = self.client.post("/v1/recom/nextActivity", data=json.dumps(data), headers=self.header)
        assert res3.status_code == 200
        activityType = res3.json()['result']['data'][0]['activityType']
        usage = res3.json()['result']['data'][0]['usage']
        itemId = res3.json()['result']['data'][0]['itemId']
        itemForm = res3.json()['result']['data'][0]['itemForm']
        loCode = res3.json()['result']['data'][0]['ncode']
        curPoolCode = res3.json()['result']['section']['curPoolCode']
        return itemId, usage, activityType, loCode, itemForm, curPoolCode

    def Module(self, itemId, usage, activityType, loCode, itemForm):

        if activityType == 'RVIDEO' or activityType == 'LO':
            data = {
                "sensor": "FINISH",
                "requestId": ticks,
                "sendTime": ticks,
                "token": "debug",
                "sessionId": self.sessionId,
                "data": [{
                    "actor": self.u,
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
                    "actor": self.u,
                    "action": "SUBMITTED",
                    "object": {
                        "loCode": loCode,
                        "score": h2,
                        "totalScore": 1,
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
        res4 = self.client.post("/v1/recom/submitEvent", data=json.dumps(data), headers=self.header)
        assert json.loads(res4.text)["code"] =="200"

    @task
    def run__(self):
        while True:
            itemId, usage, activityType, loCode, itemForm, curPoolCode = self.nextActivity(self.sessionId)
            if activityType == 'DQUEST' or activityType == 'RVIDEO' or activityType == 'LO':
                self.Module(itemId, usage, activityType, loCode, itemForm)
            else:
                break

    def on_stop(self):
        '''销毁数据，每个虚拟用户只执行一次'''
        # self.client.post("https://www.baidu.com")
        pass


class WebsiteUser(HttpUser):
    host = 'http://10.173.11.162:9999'

    tasks = [UserTask]
    # 每个任务之间设置间隔时间，随机从3~5区间内取，单位是 s
    wait_time = between(0, 2)

# if __name__ == "__main__":
#     # -u 并发量 为 100  -r 指定并发加压速率  -t 脚本运行时间
#     os.system('locust -f 1.py --headless -u 100 -r 20 -t 120')


#  locust -f 1.py --headless -u 100 -r 20  -t 3 --csv=example


#  locust -f 1.py --headless -u 1 -r 1  -t 1 --csv=example



# locust -f 1.py --web-host="127.0.0.1"
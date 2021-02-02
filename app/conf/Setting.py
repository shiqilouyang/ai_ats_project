import os
import random
import time
import decimal
from fractions import Fraction


userId = "autoTest-xfl-4684" + str(int(round(time.time())))
accountId = "autoTest-xfl-468464722054645611402"
ticks = int(round(time.time()))
rand = random.randint(0, 9999999)
rand11 = random.randint(60, 240)
rand12 = random.randint(0, 1)

execl_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "execl","{}.csv")
classes_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "conf","classes")
conf_init_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "conf","__init__.py")
utils_init_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "utils","__init__.py".format(1))
html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "templates","{}.html")
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "log","{}.log")

#生产环境
UNlockProdUrl = "http://algo-ale-server.k8s.prod.internal.classba.cn/unlock/v1/recom/unlock"
GetSessionProdUrl = "http://algo-ale-server.k8s.prod.internal.classba.cn/session/v1/recom/getSession"
nextActivityProdUrl = "http://algo-ale-server.k8s.prod.internal.classba.cn/recom/v1/recom/nextActivity"
submitEventProdUrl = "http://algo-ale-server.k8s.prod.internal.classba.cn/submit/v1/event/submitEvent"

#测试环境
UNlockProdUrl_test = "http://algo-ale-server.k8s.test.internal.classba.cn/unlock/v1/recom/unlock"
GetSessionProdUrl_test = "http://algo-ale-server.k8s.test.internal.classba.cn/session/v1/recom/getSession"
nextActivityProdUrl_test = "http://algo-ale-server.k8s.test.internal.classba.cn/recom/v1/recom/nextActivity"
submitEventProUrl_test = "http://algo-ale-server.k8s.test.internal.classba.cn/submit/v1/event/submitEvent"

# algo-ale-irs-submit-server  预发环境
UNlockPreUrl = "http://algo-ale-irs-unlock-server.k8s.pre.internal.classba.cn/v1/recom/unlock"
GetSessionPreUrl = "http://algo-ale-irs-session-server.k8s.pre.internal.classba.cn/v1/recom/getSession"
nextActivityPreUrl = "http://algo-ale-irs-recom-server.k8s.pre.internal.classba.cn/v1/recom/nextActivity"
submitEventPreUrl = "http://algo-ale-irs-submit-server.k8s.pre.internal.classba.cn/v1/event/submitEvent"


score = 0 # TestPoolModel  "score=1"
systemResult = 0
totalScore = 0


class rateConf():
    def __init__(self,rate = None):
        rate = float(rate)
        if rate == 0:
            self.rataList_1 = "00"
        if rate ==1:
            self.rataList_1 = "11"
        if rate != 0 and rate!= 1:
            self.rate = str(Fraction(decimal.Decimal(str(rate)))).split("/")
            self.rataList = []
            for i in range(0, int(float(self.rate[0]))):
                self.rataList.append(1)
            for i in range(0, int(float(self.rate[1])) - int(float(self.rate[0]))):
                self.rataList.append(0)
            random.shuffle(self.rataList)
            self.rataList_1 = "".join(str(i) for i in self.rataList)



class Config():
    '''mysql 配置'''
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:x@127.0.0.1:3306/test'
    SQLALCHEMY_DATABASE_URI = 'mysql://db_admin:Projectx@2017@10.31.210.18:3306/sc_normal_center'
    # SQLALCHEMY_DATABASE_URI = 'mysql://db_admin:hello@2017@106.14.214.32:3306/sc_normal_center'
    MONGO_DATABASE_URI = "mongodb://{user_name}:{pass_word}@{host}:{port}/{database}".format(
        user_name='irs_middle',
        pass_word='TdgjJSVKSGxSwkGU',
        host='algo-ale-primary.mongodb.rds.aliyuncs.com',
        port=3717,
        database='alenormal'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_TIMEOUT = 90  # 超时时间
    SQLALCHEMY_POOL_RECYCLE = 280  # 空闲连接自动回收时间
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_MAX_OVERFLOW = 128 # 控制在连接池达到最大值后可以创建的连接数。

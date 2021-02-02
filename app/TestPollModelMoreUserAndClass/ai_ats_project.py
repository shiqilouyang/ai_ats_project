import json
import os
import threading
import time
from imp import reload
from pprint import pprint
import copy
from sqlalchemy import func

from log import loger


lock = threading.Lock()
from flask import request
from TestPollModelMoreUserAndClass import ai_ats_project
from conf.Setting import utils_init_path, userId, log_path

body = {}
path = utils_init_path

@ai_ats_project.errorhandler(501)
def handler_error(error):
    return error


def asynctask(body):
    h = body.get("classIds")
    body.update({
        "classIds" : h if h.find(",") == "-1" else h.split(",")
    })
    from TestPoolModel.interfaceEngine import interfaceEngine
    return  interfaceEngine(body).run()



def asynctask8(body):
    results_data = {}
    body.get("")
    list_users = []
    data = {}
    l = []
    for i in range(2):
        list_users.append(userId +"{}".format(i))
    #     i 代表是 user
    for i in list_users:
        # k 是 class1_   class2_   class3_
        for k,v in body.items():
            for rate1 in range(2):
                data.update({"course_id": int(v.get("courseId"))})
                data.update({"class_id": v.get("classIds") if v.get("classIds").find("_") == "-1" else v.get("classIds").split("_")})
                data.update({"section_id": int(v.get("sectionId"))})
                from TestPollModelMoreUserAndClass import interfaceEngineTesterMoreUser
                user_id , session_id = interfaceEngineTesterMoreUser.interfaceEngineTesterMoreUser(rate1/10,i).run(data,rate1/10)
                results_data.update({
                    "{}|{}|{}|{}|{}".format(data.get("course_id"),data.get("class_id"), data.get("section_id"),user_id,rate1/10): (user_id , session_id)
                })
    pprint(results_data)
    loger.info("results is {}".format(results_data))


# 多个用户跑多个课程
@ai_ats_project.route('/moreUser', methods=["GET", "POST"] , strict_slashes=False)
def moreUsergetMoreClassMessage():
    if request.method == "POST":
        body = json.loads(request.get_data(as_text=True))
        t = threading.Thread(target=asynctask8, args=(body,))
        t.setDaemon(True)
        t.start()
    return userId



# 一个用户跑一个个课程 获取 log 信息
@ai_ats_project.route('/getlog', methods=["GET", "POST"])
def getlog():
    from TestPoolModel.model import models_,Operationtable
    if request.method == "GET":
        userId_ = request.args.get("userId")
        users = Operationtable.query.filter(Operationtable.user_id == userId_).first()
        if users is None:
            return {"message": "获取log 信息失败! 没有当前用户操作信息"}, 200
        logpath = log_path.format(userId_)
        try:
            with open(logpath, "r", encoding="UTF-8") as f:
                log = f.read()
        except FileNotFoundError:
            log = "没有找到日志文件"
        return {"message":log}, 200


@ai_ats_project.route('/getSessionId', methods=["POST"])
def getSessionId():
    if request.method == "POST":
        from conf.Setting import utils_init_path, userId
        u =  userId
        rq = request.get_data(as_text=True)
        body = json.loads(rq)
        import time
        reload(time)
        body.update({
            "u": "autoTest-xfl-4684-" + str(int(round(time.time())))
        })
        try:
            t = threading.Thread(target=asynctask, args=(body,))
            t.setDaemon(True)
            t.start()
        except Exception as e:
            from TestPoolModel.model import Operationtable
            Operationtable.query.filter(Operationtable.user_id == body.get("u")).update({
                Operationtable.status: "ERROR",
                Operationtable.message: '程序异常'
            })
            from TestPoolModel.model import db
            db.session.commit()
            db.session.close()
        return u, 200


def moreTask(body):
    from info import mongo
    def asynctask1(bodys):
        h = bodys.get("classIds")
        bodys.update({
            "classIds" : h if h.find(",") == "-1" else h.split(",")
        })
        from TestPoolModel.interfaceEngineTester import interfaceEngineTester
        return  interfaceEngineTester(bodys).run()
    data = {}
    list_data = []
    for k, v in body.items():
        if k != 'classList':
            data.update({k: v})
    for item in body.get('classList'):
        section__find = mongo.db["ALE_SECTION"].find(
            {"sectionId": item.get("sectionId"), "courseId": item.get("courseId"), "storageStatus": "USEING"},
            {"ruleGroupId": 1, "_id": 0})
        for i in section__find:
            item.update({
                "groupId":i["ruleGroupId"] if section__find else "NONE"
            })
        list_data.append(item)
    import time
    reload(time)
    data.update({
        "u": "autoTest-xfl-4684-" + str(int(round(time.time())))
    })
    for i in list_data:
        i.update(data)
        try:
            t = threading.Thread(target=asynctask1, args=(i,))
            t.setDaemon(True)
            t.start()
            t.join()
        except Exception as e:
            from TestPoolModel.model import Operationtable
            Operationtable.query.filter(Operationtable.user_id == i.get("u")).update({
                Operationtable.status: "ERROR",
                Operationtable.message: '程序异常'
            })
            from TestPoolModel.model import db
            db.session.commit()
            db.session.close()


@ai_ats_project.route('/getSessionIdMoreClass', methods=["POST"])
def getSessionIdMoreClass():
    if request.method == "POST":
        from conf.Setting import utils_init_path, userId
        u = userId
        rq = request.get_data(as_text=True)
        body = json.loads(rq)
        t = threading.Thread(target=moreTask, args=(body,))
        t.start()
        return u, 200


def moreTask1(body):
    from info import mongo
    def asynctask1(bodys):
        h = bodys.get("classIds")
        bodys.update({
            "classIds" : h if h.find(",") == "-1" else h.split(",")
        })
        from TestPoolModel.interfaceEngineTester import interfaceEngineTester
        return  interfaceEngineTester(bodys).run()
    data = {}
    list_data = []
    for k, v in body.items():
        if k != 'classList':
            data.update({k: v})
    for item in body.get('classList'):
        section__find = mongo.db["ALE_SECTION"].find(
            {"sectionId": item.get("sectionId"), "courseId": item.get("courseId"), "storageStatus": "USEING"},
            {"ruleGroupId": 1, "_id": 0})
        for i in section__find:
            item.update({
                "groupId":i["ruleGroupId"] if section__find else "NONE"
            })
        list_data.append(item)
    for i in list_data:
        i.update(data)
        try:
            t = threading.Thread(target=asynctask1, args=(i,))
            t.setDaemon(True)
            t.start()
            t.join()
        except Exception as e:
            from TestPoolModel.model import Operationtable
            Operationtable.query.filter(Operationtable.user_id == i.get("u")).update({
                Operationtable.status: "ERROR",
                Operationtable.message: '程序异常'
            })
            from TestPoolModel.model import db
            db.session.commit()
            db.session.close()




@ai_ats_project.route('/getSessionIdMoreUserMoreClass', methods=["POST"])
def getSessionIdMoreUserMoreClass():
    if request.method == "POST":
        from conf.Setting import utils_init_path, userId
        u = userId
        rq = request.get_data(as_text=True)
        body = json.loads(rq)
        rate_list = body.get("rate")
        th_list = []
        for i in rate_list:
            bodys = copy.deepcopy(body)
            import time
            reload(time)
            bodys.update({
                "u": "autoTest-xfl-4684-" + str(int(round(time.time()))) +str(i).replace('.',''),
                "rate": i
            })
            t = threading.Thread(target=moreTask1, args=(bodys,))
            th_list.append(t)
        for th in th_list:
            th.start()
        return u, 200

@ai_ats_project.route('/getuserlist', methods=["GET"])
def getuserlist():
    from TestPoolModel.model import Operationtable, Exercese_rule
    from TestPoolModel.model import db
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    userName = request.args.get("userName")
    class_id = request.args.get("classId")
    course_id = request.args.get("courseId")
    section_id = request.args.get("sectionId")
    session_id = request.args.get("sessionId")
    user_id = request.args.get("userId")
    rate = request.args.get("rate")
    starttime = request.args.get("startTime")
    endtime = request.args.get("endTime")
    # starttime = time.mktime(time.strptime(starttime, "%Y-%m-%d %H:%M:%S"))
    # endtime = time.mktime(time.strptime(endtime, "%Y-%m-%d %H:%M:%S"))
    # loger.info(userName + "'s endtime is{} and starttime is {}".format(endtime,starttime))
    env = request.args.get("env")
    if (course_id is None or course_id == "" ) and (userName is None or userName == "" )and (class_id is None \
            or class_id == ""  )and (section_id is None or section_id == "") \
            and (rate is None or rate == ""  )and (starttime is None or starttime == "") and (env is None or env == "") \
            and (endtime is None or endtime == "") and (session_id is None or session_id == "") \
            and (user_id is None or user_id == ""):
        message_list = []
        message_dir = {}
        # all = Operationtable.query.order_by('starttime').all()

        Opstatus_all = db.session.query(Operationtable).filter().all()
        db.session.close()

        paginate = db.session.query(Operationtable).order_by(Operationtable.starttime.desc()).paginate(page=page, per_page=per_page,error_out=False)
        db.session.close()
        for i in paginate.items:
            message_list.append(i.to_dict())
        message_dir.update({
                    "count": len(Opstatus_all),
                    'recordList': message_list
                })
        return  json.dumps(message_dir),200
    else:
        conditions = []
        message_list = []
        message_dir = {}
        if course_id != None and course_id != "":
            conditions.append(Operationtable.course_id == course_id)
        if userName != None and userName != "":
            conditions.append(Operationtable.user_name == userName)
        if class_id != None and class_id != "":
            conditions.append(Operationtable.class_id == class_id)
        if section_id != None and section_id != "":
            conditions.append(Operationtable.section_id == section_id)
        if env != None and env != "":
            conditions.append(Operationtable.env == env)
        if rate != None and rate != "":
            conditions.append(Operationtable.rate == float(rate))
        if session_id != None and session_id != "":
            conditions.append(Operationtable.session_id == session_id)
        if user_id != None and user_id != "":
            conditions.append(Operationtable.user_id == user_id)
        if starttime != None and endtime != None:
            if starttime != None and starttime != "":  # from_unixtime(1451997924)
                conditions.append(func.from_unixtime(Operationtable.starttime, "%Y-%m-%d %H:%i:%s") \
                                  > func.from_unixtime(starttime, "%Y-%m-%d %H:%i:%s"))
            if endtime != None and endtime != "":
                conditions.append(func.from_unixtime(Operationtable.starttime, "%Y-%m-%d %H:%i:%s") \
                                  < func.from_unixtime(endtime, "%Y-%m-%d %H:%i:%s"))
        db.session.close()
        print(conditions)
        paginate = db.session.query(Operationtable).filter(*conditions) \
            .order_by(Operationtable.starttime.desc()) \
            .paginate(page=page, per_page=per_page, error_out=False)
        db.session.close()
        for i in paginate.items:
            message_list.append(i.to_dict())
        message_dir.update({
            "count": len(message_list),
            'recordList': message_list
        })
        return json.dumps(message_dir), 200


@ai_ats_project.route('/ruleCheck_result', methods=["GET"])
def ruleCheck_result():
    from TestPoolModel.model import Exercese_rule
    user_id = request.args.get("userId")
    session_id = request.args.get("sessionId")
    group_id = request.args.get("groupId")
    group_id_from_sql = Exercese_rule.query.filter(Exercese_rule.rule_groupId == group_id).first()
    if group_id_from_sql != None:
        from ruleCheck.extendMath import ExtendMath
        from ruleCheck.prepMath import PreMath
        from ruleCheck.layFoundation import layFoundation
        from ruleCheck.prePhysicalChemistry import prePhysicalChemistry
        from ruleCheck.extendPhysicalChemistry import ExtendPhysicalChemistry
        from ruleCheck.conventionandReviewMath import ConventionandReviewMath
        from ruleCheck.conventionPhysicalChemistry import ConventionPhysicalChemistry
        from ruleCheck.mathPhysicalAndChemistrysprint import MathPhysicalAndChemistrysprint
        try:
            if group_id_from_sql.rule_groupId == "21301":
                ''' 数学高中秋季课复习章 '''
                c = ConventionandReviewMath(user_id,session_id,group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20301":
                ''' 数学初中秋季复习章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22301":
                ''' 数学小学秋季复习章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "21401":
                ''' 数学高中秋季课常规章 '''
                c = ConventionandReviewMath(user_id,session_id,group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20401":
                ''' 数学初中秋季常规章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22401":
                ''' 数学小学秋季常规章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22401_mock":
                ''' 语文常规章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20304":
                ''' 数学冲刺章 '''
                c = MathPhysicalAndChemistrysprint(user_id, session_id, group_id)
                results = c.sprints()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "40304":
                ''' 物理冲刺章 '''
                c = MathPhysicalAndChemistrysprint(user_id, session_id, group_id)
                results = c.sprints()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "50304":
                ''' 化学冲刺章 '''
                c = MathPhysicalAndChemistrysprint(user_id, session_id, group_id)
                results = c.sprints()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "40301":
                ''' 物理常规章 '''
                c = ConventionPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "50301":
                ''' 化学常规章 '''
                c = ConventionPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "40402":
                '''寒假 物理复习章 '''
                c = ConventionPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "50402":
                ''' 寒假 化学复习章 '''
                c = ConventionPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22403":
                ''' 数学小学秋季扩展章节 '''
                c = ExtendMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20303":
                ''' 数学初中暑假扩展章节 '''
                c = ExtendMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20403":
                ''' 数学初中秋季扩展章节 '''
                c = ExtendMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "21403":
                ''' 数学高中秋季扩展章节 '''
                c = ExtendMath(user_id, session_id, group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "21303":
                ''' 数学高中暑假扩展章节 '''
                c = ExtendMath(user_id, session_id, group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "50303":
                ''' 化学秋季扩展章 '''
                c = ExtendPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "40303":
                ''' 物理秋季扩展章 '''
                c = ExtendPhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22302":
                ''' 小学暑假预习章 '''
                c = PreMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20302":
                ''' 中学暑假预习章 '''
                c = PreMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22502":
                ''' 小学寒假预习章 '''
                c = PreMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "22501":
                ''' 数学小学寒假复习章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.primarySchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "21501":
                ''' 数学高中寒假课复习章 '''
                c = ConventionandReviewMath(user_id,session_id,group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20502":
                ''' 中学寒假预习章 '''
                c = PreMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "21502":
                ''' 高中寒假预习章 '''
                c = PreMath(user_id, session_id, group_id)
                results = c.seniorMiddleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "20501":
                ''' 数学初中寒假复习章 '''
                c = ConventionandReviewMath(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "40401":
                ''' 物理初中寒假预习章 '''
                c = prePhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "50401":
                ''' 化学初中寒假预习章 '''
                c = prePhysicalChemistry(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200
            if group_id_from_sql.rule_groupId == "990101":
                ''' 化学初中寒假复习章 '''
                c = layFoundation(user_id, session_id, group_id)
                results = c.middleSchool()
                return json.dumps(results), 200

        except Exception as e:
            return json.dumps({"code": 403, "results": []})

    return json.dumps({"code":403,"results":[]})


@ai_ats_project.route('/killTh', methods=["GET"])
def killTh():
    from TestPoolModel.model import db
    from TestPoolModel.model import Operationtable, Exercese_rule
    userId = request.args.get("userId")
    message_dir = {}
    try:
        Operationtable.query.filter(Operationtable.user_id == userId).update({
            Operationtable.status: "KILL",
            Operationtable.message: "手动终止程序"
        })
        db.session.commit()
        db.session.close()
        message_dir.update({
            "status":"OK"
        })
    except Exception as e:
        message_dir.update({
            "status":"failure"
        })
    return json.dumps(message_dir),200



@ai_ats_project.route('/hello', methods=["GET"])
def hello():
    from info import mongo
    # db.ALE_SECTION.find({"sectionId":"10000841","courseId":"10000840","storageStatus":"USEING"},{"ruleGroupId":1,"_id":0})
    section__find = mongo.db["ALE_SECTION"].find({"sectionId": "10000841", "courseId": "10000840", "storageStatus": "USEING"},
                                        {"ruleGroupId": 1, "_id": 0})
    for i in section__find:
        message_dir = i
    return json.dumps(message_dir),200



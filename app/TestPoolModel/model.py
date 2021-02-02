import sys
from flask_sqlalchemy import SQLAlchemy

from info import app

db = SQLAlchemy(app)

#  做题 记录表
class Ale_result_record_0(db.Model):
    __tablename__ = "ale_result_record_0"

    rid = db.Column(db.BIGINT,autoincrement=True, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate,
            'score':self.score
        }
        return resp_dict



class Ale_result_record_1(db.Model):
    __tablename__ = "ale_result_record_1"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_2(db.Model):
    __tablename__ = "ale_result_record_2"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict


class Ale_result_record_3(db.Model):
    __tablename__ = "ale_result_record_3"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict


class Ale_result_record_4(db.Model):
    __tablename__ = "ale_result_record_4_copy_4"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_5(db.Model):
    __tablename__ = "ale_result_record_5"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_6(db.Model):
    __tablename__ = "ale_result_record_6"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_7(db.Model):
    __tablename__ = "ale_result_record_7"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_8(db.Model):
    __tablename__ = "ale_result_record_8"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict



class Ale_result_record_9(db.Model):
    __tablename__ = "ale_result_record_9"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False)
    env = db.Column(db.String(32), nullable=False)
    itemId = db.Column(db.String(64), nullable=False)
    activityType = db.Column(db.String(32), nullable=False)
    usage = db.Column(db.String(32), nullable=False)
    loCode = db.Column(db.String(32), nullable=False)
    ability = db.Column(db.FLOAT, nullable=False)
    initability = db.Column(db.FLOAT, nullable=False)
    curPoolCode = db.Column(db.String(32), nullable=False)
    studylonum = db.Column(db.INT, nullable=False)
    prePoolCode = db.Column(db.String(32), nullable=False)
    unlockLoNum = db.Column(db.INT, nullable=False)
    curlocode = db.Column(db.String(32), nullable=False)
    preLoCode = db.Column(db.String(32), nullable=False)
    starttime = db.Column(db.String(32), nullable=False)
    duration = db.Column(db.INT, nullable=False)
    score = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.FLOAT, nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "session_id": self.session_id,
            'user_id': self.user_id,
            "course_id": self.course_id,
            "section_id": self.section_id,
            'activityType': self.activityType,
            "usage": self.usage,
            "loCode": self.loCode,
            'ability': self.ability,
            "initability": self.initability,
            "curPoolCode": self.curPoolCode,
            'studylonum': self.studylonum,
            "prePoolCode": self.prePoolCode,
            "unlockLoNum": self.unlockLoNum,
            'curlocode': self.curlocode,
            "preLoCode": self.preLoCode,
            "starttime": self.starttime,
            'duration': self.duration,
            'rate': self.rate
        }
        return resp_dict


#  用户操作表, 1.0 版本在使用, 一个用户, 一个课程
class Operationtable(db.Model):
    __tablename__ = "operation_table"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=True)
    user_id = db.Column(db.String(32), nullable=True)
    class_id = db.Column(db.String(32), nullable=True)
    course_id = db.Column(db.String(32), nullable=True)
    section_id = db.Column(db.String(32), nullable=True)
    user_name = db.Column(db.String(32), nullable=True)
    env = db.Column(db.String(32), nullable=True)
    starttime = db.Column(db.String(32), nullable=True)
    rate = db.Column(db.String(32), nullable=True)
    thid = db.Column(db.String(32), nullable=True)
    message = db.Column(db.String(32), nullable=True)
    status = db.Column(db.String(32), nullable=True)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "sessionId": self.session_id,
            'userId': self.user_id,
            "classId": self.class_id,
            "courseId": self.course_id,
            "sectionId": self.section_id,
            "startTime": self.starttime,
            "env" : self.env,
            'rate': "{}%".format(int(float(self.rate) *100)) if self.rate else None,
            "userName": self.user_name,
            "th" : self.thid,
            "message" :self.message,
            "status":self.status
        }
        return resp_dict


#  多用户 ,多课程
class OperationtableTester(db.Model):
    __tablename__ = "operation_table_tester"

    rid = db.Column(db.BIGINT, primary_key=True)
    session_id = db.Column(db.String(32), nullable=True)
    user_id = db.Column(db.String(32), nullable=True)
    class_id = db.Column(db.String(32), nullable=True)
    course_id = db.Column(db.String(32), nullable=True)
    section_id = db.Column(db.String(32), nullable=True)
    user_name = db.Column(db.String(32), nullable=True)
    env = db.Column(db.String(32), nullable=True)
    starttime = db.Column(db.String(32), nullable=True)
    rate = db.Column(db.String(32), nullable=True)
    thid = db.Column(db.String(32), nullable=True)
    message = db.Column(db.String(32), nullable=True)
    status = db.Column(db.String(32), nullable=True)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "sessionId": self.session_id,
            'userId': self.user_id,
            "classId": self.class_id,
            "courseId": self.course_id,
            "sectionId": self.section_id,
            "startTime": self.starttime,
            "env" : self.env,
            'rate': "{}%".format(int(float(self.rate) *100)) if self.rate else None,
            "userName": self.user_name,
            "th" : self.thid,
            "message" :self.message,
            "status":self.status
        }
        return resp_dict


# 主要记录了 课程校验规则
class Exercese_rule(db.Model):
    __tablename__ = "exercese_rule"

    rid = db.Column(db.BIGINT, primary_key=True)
    testmodeRule = db.Column(db.TEXT, nullable=False)
    studymodeRule = db.Column(db.TEXT, nullable=False)
    restudymodeRule = db.Column(db.TEXT, nullable=False)
    testcheckmodeRule = db.Column(db.TEXT, nullable=False)
    studycheckmodeRule = db.Column(db.TEXT, nullable=False)
    academicSeason_subject = db.Column(db.String(32), nullable=False)
    testModeNum = db.Column(db.String(32), nullable=False)
    studyModeNum = db.Column(db.String(32), nullable=False)
    restudyModeNum = db.Column(db.String(32), nullable=False)
    test_ability = db.Column(db.FLOAT, nullable=False)
    testcheckModeNum = db.Column(db.String(32), nullable=False)
    studycheckModeNum = db.Column(db.String(32), nullable=False)
    testcheck_ability = db.Column(db.FLOAT, nullable=True)
    studycheck_ability = db.Column(db.FLOAT, nullable=True)
    study_ability = db.Column(db.String(32), nullable=False)
    restudy_ability = db.Column(db.FLOAT, nullable=False)
    test_exerceseTime = db.Column(db.String(32), nullable=False)
    study_exerceseTime = db.Column(db.String(32), nullable=False)
    restudy_exerceseTime = db.Column(db.String(32), nullable=False)
    rule_groupId = db.Column(db.String(32), nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "course_id": self.course_id,
            'class_id': self.class_id,
            "section_id": self.section_id,
            "academicSeason_subject": self.academicSeason_subject,
            'testModeNum': self.testModeNum,
            "studyModeNum": self.studyModeNum,
            "restudyModeNum": self.restudyModeNum,
            'test_ability': self.test_ability,
            "study_ability": self.study_ability,
            "restudy_ability": self.restudy_ability,
            'test_exerceseTime': self.test_exerceseTime,
            "study_exerceseTime": self.study_exerceseTime,
            "restudy_exerceseTime": self.restudy_exerceseTime,
        }
        return resp_dict


class Rule_activity_test_result_record(db.Model):
    __tablename__ = "rule_activity_test_result_record"

    user_id = db.Column(db.String(32), nullable=False)
    rid = db.Column(db.BIGINT, primary_key=True)
    course_id = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.String(32), nullable=False)
    section_id = db.Column(db.String(32), nullable=False)
    academicSeason_subject = db.Column(db.String(32), nullable=False)
    message = db.Column(db.TEXT,nullable=False)
    testMode_maxNum = db.Column(db.String(32), nullable=True)
    studyMod_maxNum = db.Column(db.String(32), nullable=True)
    restudyMode_maxNum = db.Column(db.String(32), nullable=True)
    testMode_minNum = db.Column(db.String(32), nullable=True)
    studyMod_minNum = db.Column(db.String(32), nullable=True)
    restudyMode_minNum = db.Column(db.String(32), nullable=True)
    is_success = db.Column(db.INT, nullable=False)
    test_Time = db.Column(db.String(32), nullable=False)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            "course_id": self.course_id,
            'class_id': self.class_id,
            "section_id": self.section_id,
            "academicSeason_subject": self.academicSeason_subject,
            'message': self.message,
            "testMode_maxNum": self.testMode_maxNum,
            "studyMod_maxNum": self.studyMod_maxNum,
            'restudyMode_maxNum': self.restudyMode_maxNum,
            "testMode_minNum": self.testMode_minNum,
            "studyMod_minNum": self.studyMod_minNum,
            'restudyMode_minNum': self.restudyMode_minNum,
            "is_success": self.is_success,
            'test_Time': self.test_Time,
        }
        return resp_dict

class Log_id_record(db.Model):
    __tablename__ = "log_id_record"

    rid = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.String(32), nullable=True)

    def to_dict(self):
        resp_dict = {
            "rid": self.rid,
            'userId': self.user_id
        }
        return resp_dict



models_ = {
    "0": Ale_result_record_0,
    "1": Ale_result_record_1,
    "2": Ale_result_record_2,
    "3": Ale_result_record_3,
    "4": Ale_result_record_4,
    "5": Ale_result_record_5,
    "6": Ale_result_record_6,
    "7": Ale_result_record_7,
    "8": Ale_result_record_8,
    "9": Ale_result_record_9,
}
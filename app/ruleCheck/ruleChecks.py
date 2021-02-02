from pprint import pprint

from six import add_metaclass
from abc import ABCMeta, abstractmethod, abstractproperty
from TestPoolModel.model import Exercese_rule, Operationtable, db, OperationtableTester, models_
from itertools import groupby
from log import SetLog


@add_metaclass(ABCMeta)
class RuleChecks():

    ''' 规则系列 '''

    def __init__(self,user_id,session_id,group_id):
        # 每个模块,每轮的做题记录
        self.all_order = {}
        # 每个模块之中的每轮做题记录的知识点对应知识点所有做题记录(包括视频与互动题)
        self.all_order_locode = {}
        self.user_id = user_id
        self.db = db
        self.model_data = {}
        self.model_data = {}
        self.html_data = {"u":user_id}
        self.html_datas = {}
        self.ik_t = ""
        self.ik_r = ""
        self.ik_s = ""
        self.ik_tc = ""
        self.ik_sc = ''
        self.session_id = session_id
        self.group_id = group_id
        self.loger = SetLog(self.user_id)
        self.season_subject__first = Exercese_rule.query.filter(
            Exercese_rule.rule_groupId == self.group_id).first()
        Ot = Operationtable.query.filter(
            Operationtable.user_id == self.user_id).filter(
            Operationtable.session_id == self.session_id).first()
        if Ot is not None:
            self.message = Exercese_rule.query.filter(
                Exercese_rule.rule_groupId == self.group_id).first().academicSeason_subject
            self.rate = Ot.rate
            self.courseId = Ot.course_id
            self.classIds = Ot.class_id
            self.sectionId = Ot.section_id
            self.me = Ot.message
            self.ruleChecksMiddleware()
        else:
            Ot =OperationtableTester.query.filter(
                OperationtableTester.user_id == self.user_id).filter(
                OperationtableTester.session_id == self.session_id).first()
            self.message = Exercese_rule.query.filter(
                Exercese_rule.rule_groupId == self.group_id).first().academicSeason_subject
            self.rate = Ot.rate
            self.courseId = Ot.course_id
            self.classIds = Ot.class_id
            self.sectionId = Ot.section_id
            self.me = Ot.message
            self.ruleChecksMiddleware()

    def ruleChecksMiddleware(self):
        print("In RuleChecks this is userId {}".format(self.user_id))
        #  所有的知识点
        id_all = models_[self.user_id[-1]].query.filter(
            models_[self.user_id[-1]].user_id == self.user_id) \
            .filter(models_[self.user_id[-1]].session_id == self.session_id).all()
        # 切换模块的知识点
        id__filter = models_[self.user_id[-1]].query.filter(
            models_[self.user_id[-1]].user_id == self.user_id) \
            .filter(models_[self.user_id[-1]].session_id == self.session_id) \
            .filter(models_[self.user_id[-1]].curPoolCode != models_[self.user_id[-1]].prePoolCode).all()

        id__filters = models_[self.user_id[-1]].query.filter(
            models_[self.user_id[-1]].user_id == self.user_id) \
            .filter(models_[self.user_id[-1]].session_id == self.session_id) \
            .filter(models_[self.user_id[-1]].curlocode != models_[self.user_id[-1]].preLoCode) \
            .filter(models_[self.user_id[-1]].curPoolCode == models_[self.user_id[-1]].prePoolCode) \
            .filter(models_[self.user_id[-1]].curPoolCode == 'RESTUDY_MODULE') \
            .all()
        # 模块切换 + 重学模块之中上一个知识点不等于这一个知识点
        id__filter = id__filter + id__filters
        data = {}
        h = []
        for j in id_all:
            for i in id__filter:
                if j.rid == i.rid:
                    h.append(id_all.index(i))
        # 找到 id__filter 在 id_all 之中的 index, 并添加到 h 之中
        h.append(len(id_all))
        # 找到所有切换知识点的 index 集合
        list__ = [h[i:i + 2] for i in range(0, len(h), 1)][0:-1] if \
            len([h[i:i + 2] for i in range(0, len(h), 1)][-1]) == 1 else \
            [h[i:i + 2] for i in range(0, len(h), 1)]
        # 将 module 与 value 进行捆绑
        for j in list__:
            if id_all[j[0]].curPoolCode in data:
                data[id_all[j[0]].curPoolCode].append(id_all[j[0]:j[-1]])
            else:
                data[id_all[j[0]].curPoolCode] = []
                data[id_all[j[0]].curPoolCode].append(id_all[j[0]:j[-1]])
        self.all_order = data
        datas = {}
        for j in list__:
            if id_all[j[0]].curPoolCode in datas:
                ve__loCode = []
                ve_ = {}
                for ve in id_all[j[0]:j[-1]]:
                    # 所有的 知识点放到一起,作为 k
                    ve__loCode.append(ve.loCode)
                # 相同的知识点 放在一起
                a = [list(v) for _, v in groupby(ve__loCode)]
                for i in a:
                    ve_list = []
                    for l in id_all[j[0]:j[-1]]:
                        if i[0] == l.loCode:
                            ve_list.append(l)

                    ve_.update({
                        i[0]:ve_list
                    })
                datas[id_all[j[0]].curPoolCode].append(ve_)
            else:
                datas[id_all[j[0]].curPoolCode] = []
                ve__loCode = []
                ve_ = {}
                for ve in id_all[j[0]:j[-1]]:
                    # 所有的 知识点放到一起,作为 k
                    ve__loCode.append(ve.loCode)
                # 相同的知识点 放在一起
                a = [list(v) for _, v in groupby(ve__loCode)]
                for i in a:
                    ve_list = []
                    for l in id_all[j[0]:j[-1]]:
                        if i[0] == l.loCode:
                            ve_list.append(l)

                    ve_.update({
                        i[0]:ve_list
                    })
                datas[id_all[j[0]].curPoolCode].append(ve_)
        self.all_order_locode = datas

    @abstractmethod
    def middleSchool(self):
        pass

    @abstractmethod
    def primarySchool(self):
        pass

    @abstractmethod
    def seniorMiddleSchool(self):
        pass
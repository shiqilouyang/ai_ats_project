import copy

from ruleCheck.ruleChecks import RuleChecks
from TestPoolModel.model import models_


class PhysicalAndChemistry(RuleChecks):

    ''' 物理化学 系列'''

    def __init__(self,user_id,session_id,group_id):
        super(PhysicalAndChemistry, self).__init__(user_id,session_id,group_id)
        self.physicalAndChemistryMiddleware()

    def physicalAndChemistryMiddleware(self):
        print(" In PhysicalAndChemistry this is userId {}".format(self.user_id))
        if models_[self.user_id[-1]].query.filter(
                models_[self.user_id[-1]].user_id == self.user_id).filter(
            models_[self.user_id[-1]].session_id == self.session_id).all() == []:
            self.loger.info("没有找到校验用户!")
        testcheck = []
        studyMoudel = self.all_order_locode.get("STUDY_MODULE")
        restudyMoudel = self.all_order_locode.get("RESTUDY_MODULE")
        studyCheckMoudel = self.all_order_locode.get("STUDY_CHECK_MODULE")
        # 每一轮测试模块知识点数量
        self.TestMoudelper = self.all_order_locode.get("TEST_MODULE")
        if self.TestMoudelper:
            for i in self.TestMoudelper:
                for k,v in i.items():
                    i.update({
                        k:len(v)
                    })

        # 补漏测模块知识点 对应的做题个数
        self.TestCheckMoudelper = self.all_order_locode.get("TEST_CHECK_MODULE")
        if self.TestCheckMoudelper:
            for i in self.TestCheckMoudelper:
                for k, v in i.items():
                    i.update({
                        k: len(v)
                    })

        # 补漏学模块, 一个知识点推送视频个数
        self.studyCheckMoudelmvper = copy.deepcopy(studyCheckMoudel)
        if self.studyCheckMoudelmvper:
            l_ = []
            for i in self.studyCheckMoudelmvper:
                for k, v in i.items():
                    v1 = copy.deepcopy(v)
                    for l in v1:
                        if l.usage == 'LO':
                            l_.append(l)
                    i.update({k: len(l_)})
                    l_.clear()

        # 补漏学模块, 一个知识点推送混合个数
        self.studyCheckMoudelintervictiveper = copy.deepcopy(studyCheckMoudel)
        if self.studyCheckMoudelintervictiveper:
            l_ = []
            for i in self.studyCheckMoudelintervictiveper:
                for k, v in i.items():
                    for l in v:
                        if l.usage == 'INTERACT':
                            l_.append(l)
                    i.update({k: len(l_)})
                    l_.clear()

        # 补漏学模块, 一个知识点推送混合个数
        self.studyCheckMoudelmixper = copy.deepcopy(studyCheckMoudel)
        if self.studyCheckMoudelmixper:
            for i in self.studyCheckMoudelmixper:
                for k, v in i.items():
                    for l in v:
                        if l.usage == 'LO':
                            v.remove(l)
                    for l in v:
                        if l.usage == 'INTERACT':
                            v.remove(l)
                    i.update({k: len(v)})

        # 学习模块, 一个知识点推送视频个数
        self.studyMoudelmvper = copy.deepcopy(studyMoudel)
        if self.studyMoudelmvper:
            l_ = []
            for i in self.studyMoudelmvper:
                for k, v in i.items():
                    v1 = copy.deepcopy(v)
                    for l in v1:
                        if l.usage == 'LO':
                            l_.append(l)
                    i.update({k: len(l_)})
                    l_.clear()

        # 学习模块, 一个知识点推送互动个数
        self.studyMoudelintervictiveper = copy.deepcopy(studyMoudel)
        if self.studyMoudelintervictiveper:
            l_ = []
            for i in self.studyMoudelintervictiveper:
                for k, v in i.items():
                    for l in v:
                        if l.usage == 'INTERACT':
                            l_.append(l)
                    i.update({k: len(l_)})
                    l_.clear()

        self.studyMoudelmixper = copy.deepcopy(studyMoudel)
        if self.studyMoudelmixper:
            for i in self.studyMoudelmixper:
                for k,v in i.items():
                    for l in v:
                        if l.activityType == 'LO' :
                            v.remove(l)
                    for l in v:
                        if  l.usage == 'INTERACT':
                            v.remove(l)
                    i.update({k:len(v)})
        self.restudyMoudelmixper = copy.deepcopy(restudyMoudel)
        if self.restudyMoudelmixper:
            for i in self.restudyMoudelmixper:
                for k, v in i.items():
                    for l in v:
                        if l.activityType == 'LO' :
                            v.remove(l)
                    for l in v:
                        if  l.usage == 'INTERACT':
                            v.remove(l)
                    i.update({k: len(v)})

        # TODO restudyMoudelmixper len(v) > 4 并且 之间的有 LO pass

        self.restudyMoudelmvper = copy.deepcopy(restudyMoudel)
        if self.restudyMoudelmvper:
            l_ = []
            for i in self.restudyMoudelmvper:
                for k, v in i.items():
                    v1 = copy.deepcopy(v)
                    for l in v1:
                        if l.usage == 'LO':
                            l_.append(l)
                    i.update({k: len(l_)})
                    l_.clear()


        self.testModeNum = self.season_subject__first.testModeNum
        self.studyModeNum = self.season_subject__first.studyModeNum
        self.restudyModeNum = self.season_subject__first.restudyModeNum
        self.testcheckModeNum = self.season_subject__first.testcheckModeNum
        self.studycheckModeNum = self.season_subject__first.studycheckModeNum

    def middleSchool(self):
        pass

    def primarySchool(self):
        pass

    def seniorMiddleSchool(self):
        pass



# if __name__ == '__main__':
#     PhysicalAndChemistry()
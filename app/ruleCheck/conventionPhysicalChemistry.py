import copy
import time

from TestPoolModel.HtmlMake import HtmlMake
from TestPoolModel.model import models_, Rule_activity_test_result_record

from ruleCheck.physicalAndChemistry import PhysicalAndChemistry


class ConventionPhysicalChemistry(PhysicalAndChemistry):
    '''  物理常规章 化学常规章(只有初中) '''

    def middleSchool(self):
        ''' 中学检验规则:
                    1, 测试模块  2个练习题
                    classes, 学习模块
                        1,一个知识点一个视频, 最多一个互动题目, 混合最多4道题
                        classes, 做完三道题目后,每次判断能力值是否达标, 能力值大于 0.7,最多做4道题
                    3, 重学习模块
                        1, 视频一道题
                        classes, 混合一轮4道, 最多三轮(根据LO)数据
                    4, 补漏测
                        1, 2个练习题
                    5,补漏学
                        1, 一个知识点有视频，最多4道题, 做完三道题目后,每次判断能力值是否达标, 能力值大于 0.7,最多做4道题
         '''
        if self.me != "做题成功":
            self.html_datas.update({
                "code": 200,
                "results": [{
                    "userId": self.user_id,
                    "sectionResults": [{
                        "message": self.message,
                        "ruleResults": [
                            {
                                "moduleType": "测试模块",
                                "rule": self.season_subject__first.testmodeRule,
                                "rates": [{
                                    "rate": self.rate,
                                    "iR": "Failure ,具体请查看 log",
                                }]

                            },
                            {
                                "moduleType": "重学习模块",
                                "rule": self.season_subject__first.restudymodeRule,
                                "rates": [{
                                    "rate": self.rate,
                                    "iR": "Failure ,具体请查看 log",
                                }]
                            },
                            {
                                "moduleType": "学习模块",
                                "rule": self.season_subject__first.studymodeRule,
                                "rates": [{
                                    "rate": self.rate,
                                    "iR": "Failure ,具体请查看 log",
                                }]
                            },
                            {
                                "moduleType": "补漏测模块",
                                "rule": self.season_subject__first.testcheckmodeRule,
                                "rates": [{
                                    "rate": self.rate,
                                    "iR": "Failure ,具体请查看 log",
                                }]
                            }
                            ,
                            {
                                "moduleType": "补漏学模块",
                                "rule": self.season_subject__first.studycheckmodeRule,
                                "rates": [{
                                    "rate": self.rate,
                                    "iR": "Failure ,具体请查看 log",
                                }]
                            }
                        ]
                    }]
                }
                ]})
            self.testcheck = []
            self.html_data.update({
                "testmodeRule": self.season_subject__first.testmodeRule,
                "studymodeRule": self.season_subject__first.studymodeRule,
                "restudymodeRule": self.season_subject__first.restudymodeRule,
                "testcheckModeNum": self.season_subject__first.testcheckmodeRule,
                "studycheckModeNum": self.season_subject__first.studycheckmodeRule,
                "rate": self.rate,
                "ik_t": "Failure ,具体请查看 log",
                "ik_s": "Failure ,具体请查看 log",
                "ik_r": "Failure ,具体请查看 log",
                "ik_tc": "Failure ,具体请查看 log",
                "ik_sc": "Failure ,具体请查看 log",
                "mesaage": self.message
            })
            HtmlMake().primarySchoolHtmlMake(self.html_data)
            return self.html_datas
        issussess = 1
        r = s = ""
        self.testcheck = []
        try:
            if self.TestMoudelper is None:
                self.ik_t = '没有测试模块'
            else:
                for i in self.TestMoudelper:
                    for k, v in i.items():
                        if v > int(self.testModeNum):
                            s += k + ","
                self.ik_t = "测试模块知识点{}数量大于最大数量".format(s) + "\n" if s else ""
        except Exception as e:
            self.ik_t = '测试模块出现异常'
        try:
            self.ik_tc = ''
            s = ''
            if self.TestCheckMoudelper is None:
                self.ik_tc = '没有出现补漏测'
            else:
                for i in self.TestCheckMoudelper:
                    for k, v in i.items():
                        if v > int(self.testcheckModeNum):
                            s += k + ","
                self.ik_tc = "补漏测模块知识点{}数量大于最大数量".format(s) + "\n" if s else ""
        except Exception as e:
            self.ik_tc = '补漏测模块出现异常'
            pass
        s = ''
        try:  # 视频有可能两个一样的
            if self.studyMoudelmvper is None:
                self.ik_s = '没有经历学习模块'
            else:
                for i in self.studyMoudelmvper:
                    for k, v in i.items():
                        if v > int(self.studyModeNum.split("_")[1]):
                            s += k + ","
                self.ik_s += " 学习模块 知识点{} 视频个数 超过规则个数".format(s) if s else ""
                s = ""
                for i in self.studyMoudelintervictiveper:
                    for k, v in i.items():
                        if v > int(self.studycheckModeNum.split("_")[-1]):
                            s += k + ","
                self.ik_s += s + " 知识点互动个数 超过规则个数" if s else ""
                s = ""
                for i in self.studyMoudelmixper:
                    for k, v in i.items():
                        if v > int(self.studyModeNum.split("_")[3]):
                            s += k + ","
                self.ik_s += "学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
                s = ""
        except Exception:
            self.ik_s = '学习模块异常'

        try:
            if self.studyCheckMoudelmvper is None:
                self.ik_sc = '没有经历补漏学模块'
            else:
                for i in self.studyCheckMoudelmvper:
                    for k,v in i.items():
                        if int(v) != int(self.studycheckModeNum.split("_")[1]):
                            s += k + ","
                self.ik_sc += s + " 补漏学知识点 视频个数 超过规则个数" if s else ""
                s = ""
                for i in self.studyCheckMoudelintervictiveper:
                    for k, v in i.items():
                        if v > int(self.studycheckModeNum.split("_")[-1]):
                            s += k + ","
                self.ik_sc += s + " 知识点互动个数 超过规则个数" if s else ""
                s = ""
                for i in self.studyCheckMoudelmixper:
                    for k, v in i.items():
                        if v > int(self.studycheckModeNum.split("_")[3]):
                            s += k + ","
                self.ik_sc += "补漏学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
                s = ""
        except Exception:
            self.ik_sc = '补漏学模块异常'
        s = ''
        try:
            if self.restudyMoudelmixper is None:
                self.ik_r = '没有经历重学习模块'
            else:
                for i in self.restudyMoudelmixper:
                    for k, v in i.items():
                        if v > int(self.restudyModeNum.split("_")[-1]):
                            s += k + ","
                self.ik_r += "重学习" + s + " 知识点 混合题个数 超过规则个数" if s else ""
                s = ''
                for i in self.restudyMoudelmvper:
                    for k, v in i.items():
                        if v > int(self.restudyModeNum.split("_")[-1]):
                            s += k + ","
                self.ik_r += "重学习" + s + " 知识点 视频个数 超过规则个数" if s else ""
        except Exception:
            self.ik_r = '重学模块出现异常'
        if 1:
            try:
                restart_models = self.all_order_locode.get("RESTUDY_MODULE")
                if restart_models is None:
                    self.ik_r = '没有重学模块'
                else:
                    # 删除视频
                    for i in restart_models:
                        for k, v in i.items():
                            for l in v:
                                if l.activityType == 'LO':
                                    v.remove(l)

                    for i in restart_models:

                        for k, v in i.items():
                            # 两个重复视频
                            if v != []:
                            # 重学模块 每轮之中做了两道题的
                                if len(v) <= 3:
                                    # 1,三道题目进行能力值判断，是否大于 0.7
                                    if i.get(k)[-1].ability < float(self.season_subject__first.restudy_ability):
                                        issussess = 0
                                        r += i.get(k)[1].loCode + ","
                    self.ik_r += " 知识点{} 在重学模块做了两道题,但是第二道题能力值小于 0.7".format(r) if r != "" else ""
                    r = ""
            except Exception as e:
                self.ik_r = "重学习模块出现异常"
            # TODO  进入顽固池 判断条件
            try:
                start_models = self.all_order_locode.get("STUDY_MODULE")
                if start_models  is None:
                    self.ik_s = '没学习模块'
                else:
                    # 删除视频
                    for i in start_models:
                        for k, v in i.items():
                            for l in v:
                                if l.activityType == 'LO':
                                    v.remove(l)
                    s = 0
                    for i in start_models:
                        for k, v in i.items():
                            # 学习模块 做了三道题判断能力值是否大于 0.7
                            if len(v) < 4:
                                if i.get(k)[-1].ability < float(self.season_subject__first.study_ability.split("_")[2]):
                                    issussess = 0
                                    self.ik_s += i.get(k)[-1].loCode + ','
                                    s = 1
                            self.ik_s += "做了4道题以内,但是最后一道能的能力值小于{} ".format(
                                self.season_subject__first.study_ability.split("_")[2]) if s else ""
                            s = 0
            except Exception as e:
                self.ik_s = "学习模块出现了异常"

            try:
                start_check_models = self.all_order_locode.get("STUDY_CHECK_MODULE")
                if start_check_models is None:
                    self.ik_sc = '没有出现补漏学模块'
                else:
                    # 删除视频
                    for i in start_check_models:
                        for k, v in i.items():
                            for l in v:
                                if l.activityType == 'LO':
                                    v.remove(l)
                    for i in start_check_models:
                        for k, v in i.items():
                            s = ''
                            # 做了三道题，判断能力值是否大于 0.7 , 最多 4个题目
                            if len(v) < 4:
                                if i.get(k)[-1].ability < float(self.season_subject__first.study_ability.split("_")[2]):
                                    issussess = 0
                                    self.ik_sc += i.get(k)[-1].loCode + ','
                                    s = 1
                            self.ik_sc += "做了4道题以内,但是最后一道能的能力值小于{} ".format(
                                self.season_subject__first.study_ability.split("_")[2]) if s else ""
                            s = 0
            except Exception as e:
                self.ik_sc = '补漏学出现异常'
        academicSeason_subject = self.season_subject__first.academicSeason_subject

        rule_activity_test_result_record = Rule_activity_test_result_record(
            user_id=self.user_id,
            course_id=self.courseId, class_id="_".join(self.classIds), section_id=self.sectionId,
            academicSeason_subject=academicSeason_subject, message="...",
            testMode_maxNum=self.model_data.get("TestMoudelpermaxcount"),
            studyMod_maxNum="mv_{}_mix_{}_iv_{}".format(
                self.model_data.get("studyMoudelmvpermaxcount"),
                self.model_data.get("studyMoudelmixpermaxcount"),
                self.model_data.get("studyMoudelintervictivepermincount")),
            restudyMode_maxNum="mv_{}_mix_{}".format(
                self.model_data.get("restudyMoudelmvpermaxcount"),
                self.model_data.get("restudyMoudelmixpermaxcount")),
            testMode_minNum=self.model_data.get("TestMoudelpermincount"),
            studyMod_minNum="mv_{}_mix_{}_iv_{}".format(
                self.model_data.get("studyMoudelmvpermincount"),
                self.model_data.get("studyMoudelmixpermincount"),
                self.model_data.get("studyMoudelintervictivepermaxcount")),
            restudyMode_minNum="mv_{}_mix_{}".format(
                self.model_data.get("restudyMoudelmvpermincount"),
                self.model_data.get("restudyMoudelmixpermincount")),
            is_success=issussess,
            test_Time=time.asctime(time.localtime(time.time())))

        self.db.session.add_all([rule_activity_test_result_record])
        self.db.session.commit()
        self.html_data.update({
            "testmodeRule": self.season_subject__first.testmodeRule,
            "studymodeRule": self.season_subject__first.studymodeRule,
            "restudymodeRule": self.season_subject__first.restudymodeRule,
            "testcheckModeNum": self.season_subject__first.testcheckmodeRule,
            "studycheckModeNum": self.season_subject__first.studycheckmodeRule,
            "rate": self.rate,
            "ik_t": "pass" if self.ik_t == "" else self.ik_t,
            "ik_s": "pass" if self.ik_s == "" else self.ik_s,
            "ik_r": "pass" if self.ik_r == "" else self.ik_r,
            "ik_tc": "pass" if self.ik_tc == "" else self.ik_tc,
            "ik_sc": "pass" if self.ik_sc == "" else self.ik_sc,
            "mesaage": self.message
        })
        self.html_datas.update({
            "code": 200,
            "results": [{
                "userId": self.user_id,
                "sectionResults": [{
                    "message": self.message,
                    "ruleResults": [
                        {
                            "moduleType": "测试模块",
                            "rule": self.season_subject__first.testmodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "pass" if self.ik_t == "" else self.ik_t,
                            }]

                        },
                        {
                            "moduleType": "重学习模块",
                            "rule": self.season_subject__first.restudymodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "pass" if self.ik_r == "" else self.ik_r,
                            }]
                        },
                        {
                            "moduleType": "学习模块",
                            "rule": self.season_subject__first.studymodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "pass" if self.ik_s == "" else self.ik_s,
                            }]
                        },
                        {
                            "moduleType": "补漏测模块",
                            "rule": self.season_subject__first.testcheckmodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "pass" if self.ik_tc == "" else self.ik_tc,
                            }]
                        },
                        {
                            "moduleType": "补漏学模块",
                            "rule": self.season_subject__first.studycheckmodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "pass" if self.ik_sc == "" else self.ik_sc,
                            }]
                        }

                    ]
                }]
            }]
        })

        HtmlMake().primarySchoolHtmlMake(self.html_data)
        self.db.session.close()
        return self.html_datas



# if __name__ == '__main__':
#     user_id = "autoTest-xfl-4684-1609925227"
#     session_id = "336688327934567424"
#     group_id = "40402"
#     c = ConventionPhysicalChemistry(user_id,session_id,group_id)
#     c.middleSchool()
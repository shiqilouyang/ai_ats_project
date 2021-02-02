import time

from TestPoolModel.HtmlMake import HtmlMake
from TestPoolModel.model import models_, Rule_activity_test_result_record
from ruleCheck.maths import Maths


class prePhysicalChemistry(Maths):

    ''' 物理化学 寒假预习章 '''

    def middleSchool(self):
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
                            }]
                    }]
                }
                ]})
            self.html_data.update({
                "testmodeRule": self.season_subject__first.testmodeRule,
                "studymodeRule": self.season_subject__first.studymodeRule,
                "restudymodeRule": self.season_subject__first.restudymodeRule,
                "rate": self.rate,
                "ik_t": "Failure ,具体请查看 log",
                "ik_s": "Failure ,具体请查看 log",
                "ik_r": "Failure ,具体请查看 log",
                "mesaage": self.message
            })
            HtmlMake().primarySchoolHtmlMake(self.html_data)
            return self.html_datas
        studyModeNum = self.season_subject__first.studyModeNum
        restudyModeNum = self.season_subject__first.restudyModeNum
        issussess = 1
        r = s = ""
        try:
            if self.studyMoudelmvper is None:
                self.ik_s = '没有学习模块'
            else:
                for i in self.studyMoudelmvper:
                    for k, v in i.items():
                        if v > int(self.studyModeNum.split("_")[1]):
                            s += k + ","
                    self.ik_s += " 学习模块 知识点{} 视频个数 超过规则个数".format(s) if s else ""
                s = ""
                for i in self.studyMoudelintervictiveper:
                    for k, v in i.items():
                        if v > int(self.studyModeNum.split("_")[-1]):
                            s += k + ","
                self.ik_s += s + " 知识点互动个数 超过规则个数" if s else ""
                s = ""
                for i in self.studyMoudelmixper:
                    for k, v in i.items():
                        if v > int(self.studyModeNum.split("_")[3]):
                            s += k + ","
                self.ik_s += "学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
                s = ""
        except Exception as e:
            self.ik_s = '学习模块出现异常'
        try:
            if self.restudyMoudelmixper is None:
                self.ik_r = '没有重学习模块'
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
                r = ""
        except Exception as e:
            self.ik_r = '重学习模块出现异常'
        if 1:
            try:
                start_models = self.all_order_locode.get("STUDY_MODULE")
                if start_models is None:
                    self.ik_s = '没有学习模块'
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
                            # 学习模块 能力值大于等于 4判断能力值是否 0.7
                            if 3 == len(v):
                                if float(self.season_subject__first.study_ability) < i.get(k)[-1].ability:
                                    issussess = 0
                                    self.ik_s += i.get(k)[-1].loCode + ','
                                    s = 1
                    self.ik_s += "做了3道题,但是最后一道能的能力值小于{} ".format(
                        float(self.season_subject__first.study_ability)) if s else ""
                    s = 0
            except Exception as e:
                self.ik_s = "学习模块出现异常"
        if 1:
            try:
                restart_models = self.all_order_locode.get("RESTUDY_MODULE")
                # 删除视频
                if restart_models is None:
                    self.ik_r = '没有出现重学习模块'
                else:
                    l_ = []
                    for i in restart_models:
                        for k, v in i.items():
                            for l in v:
                                if l.activityType == 'LO':
                                    v.remove(l)
                    s = 0
                    for i in restart_models:
                        for k, v in i.items():
                            # 重学习模块 能力值大于等于 4判断能力值是否 0.7
                            if 3 <= len(v) <5:
                                if i.get(k)[-1].ability < float(self.season_subject__first.study_ability)  :
                                    issussess = 0
                                    self.ik_r += i.get(k)[-1].loCode + ','
                                    s = 1
                    self.ik_r += " 做了4道题以下,但是最后一道能的能力值小于{} ".format(
                        float(self.season_subject__first.study_ability)) if s else ""
                    s = 0
            except Exception as e:
                self.ik_r = "重学习模块出现异常h"

        academicSeason_subject = self.season_subject__first.academicSeason_subject

        rule_activity_test_result_record = Rule_activity_test_result_record(
            user_id=self.user_id,
            course_id=self.courseId, class_id="_".join(self.classIds), section_id=self.sectionId,
            academicSeason_subject=academicSeason_subject, message="....",
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
            "rate": self.rate,
            "ik_t": "无测试模块",
            "ik_s": "pass" if self.ik_s == "" else self.ik_s,
            "ik_r": "pass" if self.ik_r == "" else self.ik_r,
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
                                "iR": "无" if self.ik_t == "" else self.ik_t,
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
                        }]
                }]
            }

            ]})
        HtmlMake().primarySchoolHtmlMake(self.html_data)
        self.db.session.close()
        return self.html_datas




# if __name__ == '__main__':
#     user_id = "autoTest-xfl-4684-1609833246"
#     session_id = "336591083585328128"
#     group_id = "50402"
#     c = prePhysicalChemistry(user_id,session_id,group_id)
#     c.middleSchool()
import time

from TestPoolModel.HtmlMake import HtmlMake
from TestPoolModel.model import models_, Rule_activity_test_result_record
from ruleCheck.maths import Maths


class ExtendMath(Maths):
    ''' 暑假扩展章 秋季扩展章 '''

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
        s = ""
        r = ""
        try:
            s = ""
            for i in self.studyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.studyModeNum.split("_")[3]):
                        s += k + ","
            self.ik_s += "学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
            s = ""
        except Exception as e:
            self.ik_s = '无学习模块或者学习模块出现了异常'
        try:
            s = ''
            for i in self.restudyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.restudyModeNum.split("_")[3]):
                        s += k + ","
            self.ik_r += "重学习" + s + " 知识点 混合题个数 超过规则个数" if s else ""
        except Exception as  e:
            self.ik_r = "无重学习模块或者重学习模块出现了异常"
        # if 1:
        #     try:
        #         sc_ = {}
        #         for i in range(len(self.restudyMoudelmixper)):
        #             if self.restudyMoudelmixper[i][0] == 3:
        #                 code_restudy_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.restudyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].curPoolCode == "RESTUDY_MODULE").filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").all()
        #                 sc = 0
        #                 for i in code_restudy_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_r += "重学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_r = "无重学习模块或者重学习模块出现了异常"
        #     try:
        #         # TODO  进入顽固池 判断条件
        #         sc_ = {}
        #         for i in range(len(self.studyMoudelmixper)):
        #             if self.studyMoudelmixper[i][0] == 3:  # 第二题 能力值大于 0.7
        #                 code_study_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.studyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").filter(
        #                     models_[self.user_id[-1]].curPoolCode == "STUDY_MODULE").all()
        #                 sc = 0
        #                 for i in code_study_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_s += "学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_s = "无学习模块或者学习模块出现了异常"

        academicSeason_subject = self.season_subject__first.academicSeason_subject

        rule_activity_test_result_record = Rule_activity_test_result_record(
            user_id=self.user_id,
            course_id=self.courseId, class_id="_".join(self.classIds), section_id=self.sectionId,
            academicSeason_subject=academicSeason_subject, message="---",
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
            "ik_t": "pass" if self.ik_t == "" else self.ik_t,
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
                        }]
                }]
            }

            ]})
        HtmlMake().primarySchoolHtmlMake(self.html_data)
        self.db.session.close()
        return self.html_datas

    def primarySchool(self):
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
        s = ""
        r = ""
        try:
            s = ""
            for i in self.studyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.studyModeNum.split("_")[3]):
                        s += k + ","
            self.ik_s += "学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
            s = ""
        except Exception as e:
            self.ik_s = '无学习模块或者学习模块出现了异常'
        try:
            s = ''
            for i in self.restudyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.restudyModeNum.split("_")[3]):
                        s += k + ","
                self.ik_r += "重学习" + r + " 知识点 混合题个数 超过规则个数" if s else ""
        except Exception as  e:
            self.ik_r = "无重学习模块或者重学习模块出现了异常"
        # if 1:
        #     try:
        #         sc_ = {}
        #         for i in range(len(self.restudyMoudelmixper)):
        #             if self.restudyMoudelmixper[i][0] == 3:
        #                 code_restudy_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.restudyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].curPoolCode == "RESTUDY_MODULE").filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").all()
        #                 sc = 0
        #                 for i in code_restudy_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_r += "重学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_r = "无重学习模块或者重学习模块出现了异常"
        #     try:
        #         # TODO  进入顽固池 判断条件
        #         sc_ = {}
        #         for i in range(len(self.studyMoudelmixper)):
        #             if self.studyMoudelmixper[i][0] == 3:  # 第二题 能力值大于 0.7
        #                 code_study_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.studyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").filter(
        #                     models_[self.user_id[-1]].curPoolCode == "STUDY_MODULE").all()
        #                 sc = 0
        #                 for i in code_study_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_s += "学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_s = "无学习模块或者学习模块出现了异常"

        academicSeason_subject = self.season_subject__first.academicSeason_subject

        rule_activity_test_result_record = Rule_activity_test_result_record(
            user_id=self.user_id,
            course_id=self.courseId, class_id="_".join(self.classIds), section_id=self.sectionId,
            academicSeason_subject=academicSeason_subject, message="---",
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
            "ik_t": """无测试模块""",
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
                                "iR": "无测试模块",
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

    def seniorMiddleSchool(self):
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
        s = ""
        r = ""
        try:
            s = ""
            for i in self.studyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.studyModeNum.split("_")[3]):
                        s += k + ","
            self.ik_s += "学习模块" + s + " 知识点 混合题个数 超过规则个数" if s else ""
            s = ""
        except Exception as e:
            self.ik_s = '无学习模块或者学习模块出现了异常'
        try:
            s = ''
            for i in self.restudyMoudelmixper:
                for k, v in i.items():
                    if v > int(self.restudyModeNum.split("_")[3]):
                        s += k + ","
                self.ik_r += "重学习" + r + " 知识点 混合题个数 超过规则个数" if s else ""
        except Exception as  e:
            self.ik_r = "无重学习模块或者重学习模块出现了异常"
        # if 1:
        #     try:
        #         sc_ = {}
        #         for i in range(len(self.restudyMoudelmixper)):
        #             if self.restudyMoudelmixper[i][0] == 3:
        #                 code_restudy_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.restudyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].curPoolCode == "RESTUDY_MODULE").filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").all()
        #                 sc = 0
        #                 for i in code_restudy_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_r += "重学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_r = "无重学习模块或者重学习模块出现了异常"
        #     try:
        #         # TODO  进入顽固池 判断条件
        #         sc_ = {}
        #         for i in range(len(self.studyMoudelmixper)):
        #             if self.studyMoudelmixper[i][0] == 3:  # 第二题 能力值大于 0.7
        #                 code_study_module__all = models_[self.user_id[-1]].query.filter(
        #                     models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                     models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                     models_[self.user_id[-1]].loCode == self.studyMoudelmixper[i][1]).filter(
        #                     models_[self.user_id[-1]].usage != "LO").filter(
        #                     models_[self.user_id[-1]].usage != "INTERACT").filter(
        #                     models_[self.user_id[-1]].curPoolCode == "STUDY_MODULE").all()
        #                 sc = 0
        #                 for i in code_study_module__all:
        #                     if i.score == "0":
        #                         sc += 1
        #                     #  错误个数 大于 classes
        #                     if sc >= 2:
        #                         sc_.update({
        #                             i.loCode: sc
        #                         })
        #         for k in sc_.values():
        #             if k > int(restudyModeNum.split("_")[-3]):
        #                 self.ik_s += "学习模块 知识点 {} 学习到重学到学习".format(sc_.get(k))
        #     except Exception as e:
        #         self.ik_s = "无学习模块或者学习模块出现了异常"

        academicSeason_subject = self.season_subject__first.academicSeason_subject

        rule_activity_test_result_record = Rule_activity_test_result_record(
            user_id=self.user_id,
            course_id=self.courseId, class_id="_".join(self.classIds), section_id=self.sectionId,
            academicSeason_subject=academicSeason_subject, message="---",
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
            "ik_t": """无测试模块""",
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
                                "iR": "无测试模块",
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
#     user_id = "autoTest-xfl-4684-1608992090"
#     session_id = "335709067137381376"
#     group_id = "20403"
#     c = ExtendMath(user_id, session_id, group_id)
#     results = c.middleSchool()
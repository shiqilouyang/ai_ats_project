import time

from TestPoolModel.HtmlMake import HtmlMake
from ruleCheck.physicalAndChemistry import PhysicalAndChemistry


class  ExtendPhysicalChemistry(PhysicalAndChemistry):
    ''' 物理化学扩展章 没有补漏测,补漏学模块'''

    def middleSchool(self):
        '10001979   10001985  10001984  测试'
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
        from TestPoolModel.model import models_, Rule_activity_test_result_record
        issussess = 1
        s = ""
        studyMoudelmixper_error = []
        # if 1:
        #     try:
        #     # TODO  进入顽固池 判断条件
        #         for i in range(len(self.studyMoudelmixper)):
        #             code_study_module__all = models_[self.user_id[-1]].query.filter(
        #                 models_[self.user_id[-1]].user_id == self.user_id).filter(
        #                 models_[self.user_id[-1]].session_id == self.session_id).filter(
        #                 models_[self.user_id[-1]].loCode == self.studyMoudelmixper[i][1]).filter(
        #                 models_[self.user_id[-1]].usage != "LO").filter(
        #                 models_[self.user_id[-1]].usage != "INTERACT").filter(
        #                 models_[self.user_id[-1]].curPoolCode == "STUDY_MODULE").all()
        #             for i in code_study_module__all:
        #                 if i.score == "0":
        #                     studyMoudelmixper_error.append(i.loCode)
        #         print(studyMoudelmixper_error)
        #
        #     except Exception as e:
        #         self.ik_s = "学习模块出现了异常"

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
                                "iR": '无测试模块',
                            }]

                        },
                        {
                            "moduleType": "重学习模块",
                            "rule": self.season_subject__first.restudymodeRule,
                            "rates": [{
                                "rate": self.rate,
                                "iR": "无重学习模块",
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

#
# if __name__ == '__main__':
#     user_id = "autoTest-xfl-4684-1608984980"
#     session_id = "335701612543210496"
#     group_id = "40303"
#     c = ExtendPhysicalChemistry(user_id,session_id,group_id)
#     c.middleSchool()
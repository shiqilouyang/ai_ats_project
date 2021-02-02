'''

allure 使用文档
https://cloud.tencent.com/developer/article/1516907

    pytest --alluredir=./allure-results/
    allure generate allure-results -o allure-reports/ --clean
'''

import os

get_studentlevel_url_old = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/getStudentLevel'
getloname_url = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/getLoName'
getStudentLoStudyCost_url = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/getStudentLoStudyCost'
getStudentQuestionList_url = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/getStudentQuestionList'
getStudentTestStaus_url = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/getStudentTestStatus'
studentLevelOfCourse_url = 'http://algo-irs-data.k8s.pre.internal.classba.cn/v1/student/studentLevelOfCourse'



getLoName_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", 'getLoName')

getStudentLevel_math_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'algo_irs_data_student_level_details_hbase_math.txt')
getStudentLevel_chem_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'algo_irs_data_student_level_details_hbase_chem.txt')
getStudentLevel_phy_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'algo_irs_data_student_level_details_hbase_phy.txt')
getStudentLoStudyCost_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'ale_account_locode_tag1.txt')
getStudentQuestionList_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'irs_result_question.txt')
getStudentTestStaus_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'irs_account_locode_tag.txt')
studentLevelOfCourse_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) \
                                         , "data", 'feature_student_level.json')
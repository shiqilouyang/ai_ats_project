import json
import random
import requests

from dataCenter.config.conf import getStudentQuestionList_url

def test_getStudentQuestionList(getStudentQuestionList_file,request_header):
    getStudentQuestionList_files = []
    getStudentQuestionList_files.append(getStudentQuestionList_file[0])
    l = random.sample(getStudentQuestionList_file[1:],5)
    getStudentQuestionList_files += l
    irs_result_question_readline_map = {}
    for u in getStudentQuestionList_files[1:]:
        u1 = u.replace("\n", '')
        u__split = u1.split("\t")
        irs_result_question_readline_map.update({
            u__split[0]:u__split[1:]
        })
    for k,v in irs_result_question_readline_map.items():
        data = {
            "appId": "debug",
            "token": "debug",
            "requestId": "666666",
            "accountId": k,
            "loCode": v[0],
            "subjectId": v[1],
            "courseId": v[2],
            "classSectionId": v[3],
            "taskSectionId": v[4],
            "sectionId": v[5],
            "beforeTime": json.loads(v[6])[0].get('last_create_time') - 10,
            "laterTime": json.loads(v[6])[0].get('last_create_time') + 10
        }
        response = requests.post(url=getStudentQuestionList_url, data=json.dumps(data), headers=request_header)
        re = json.loads(response.text)
        assert re.get("code") == 200

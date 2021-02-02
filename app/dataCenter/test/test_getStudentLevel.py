import json
import random
from pprint import pprint
import requests

from dataCenter.config.conf import get_studentlevel_url_old


def test_getStudentLevel(getStudentLevel_math_file,request_header):
    readlines_list_map = []
    readlines_list = []
    getStudentLevel_math_files = []
    getStudentLevel_math_files.append(getStudentLevel_math_file[0])
    l = random.sample(getStudentLevel_math_file, 5)
    getStudentLevel_math_files +=l
    for i in getStudentLevel_math_files:
        readlines_list.append(i.replace("\n", ""))

    # 每一行 \t 进行切割， 第一行切割结果作为 key, 以后的每一行为 v 拼接成字典，并且保存到readlines_list_map 之中
    for item in readlines_list[1:]:
        readlines_list_map.append(dict(map(lambda x, y: [x, y], \
                                           readlines_list[0].split("\t"), item.split("\t"))))
    for u in readlines_list_map:  # old
        data = {
            "appId": "debug",
            "token": "debug",
            "requestId": "666666",
            "userId": u.get("user_id"),
            "accountId": u.get("account_id"),
            "courseId": u.get("course_id"),
            "sectionId": u.get("section_id"),
            "subjectId": "2",
            "grade": u.get("grade"),
            "stage": u.get("stage")
        }
        response = requests.post(url=get_studentlevel_url_old, data=json.dumps(data), headers=request_header)
        re = json.loads(response.text)
        assert re.get("code") == 200

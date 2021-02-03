import json
import random
from pprint import pprint

import requests

from dataCenter.config.conf import studentLevelOfCourse_url

def test_studentLevelOfCourse(studentLevelOfCourse_file,request_header):
    datas = random.sample(studentLevelOfCourse_file.get("data"),5)
    studentLevelOfCourse_file.update({
        "data": datas
    })
    results = {}
    for i in studentLevelOfCourse_file.get("data"):
        if i.get("_source") !={}:
            results.update({
                i.get("_source").get("user_id"):i.get("_source").get("course_id")
            })

    for k, v in results.items():
        data = {
            "userId": k,
            "courseId": v
        }
        response = requests.get(studentLevelOfCourse_url
                         , params=data,
                         headers = request_header
                         )
        res = json.loads(response.text)
        strout = []
        strout.append({
            "request_data": data,
            "request_response": res
        })
        pprint(strout)
        assert res.get("code") == 200

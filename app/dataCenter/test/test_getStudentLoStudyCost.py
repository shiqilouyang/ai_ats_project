import json
import re
from pprint import pprint
import random

import requests

from dataCenter.config.conf import getStudentLoStudyCost_url


def test_getStudentLoStudyCost(getStudentLoStudyCost_file,request_header):
    readlines_list = []
    readlines_list_map = {}
    for i in getStudentLoStudyCost_file:
        readlines_list.append(i.replace("\n", ""))
    readlines_lists = random.sample(readlines_list,5)
    for i in readlines_lists:
        l_end_his_stu_time = []
        for k,v in json.loads(i.split("\t")[1]).items():

            if k.endswith("#his_stu_time"):
                l_end_his_stu_time.append(k[:-13])
        readlines_list_map.update({
            i.split("\t")[0]:l_end_his_stu_time
        })

    def ch(a):
        re_map = {}
        for i in a:
            re_set = []
            k = re.findall(r"\d+#.*#", i)[0]
            for i1 in a:
                if i1.startswith(k):
                    re_set.append(i1.split("#")[-1])
            re_map.update({k:re_set})
        return re_map

    for k,v in readlines_list_map.items():
        change = ch(v)
        readlines_list_map.update({
            k:change
        })

    for k, v in readlines_list_map.items():
        for k1, v1 in v.items():
            for i in range(1,9):
                data = {
                    "appId": "debug",
                    "token": "debug",
                    "requestId": k,
                    "accountId": "66666",
                    "subjectId": k1.split("#")[0],
                    "stage": k1.split("#")[1],
                    "textbook": k1.split("#")[2],
                    "courseId": "11111",
                    "loCodes": v1[:i]
                }
                response = requests.post(url=getStudentLoStudyCost_url, data=json.dumps(data), headers=request_header)
                res = json.loads(response.text)
                strout = []
                strout.append({
                    "request_data": data,
                    "request_response": res
                })
                pprint(strout)
                assert res.get("code") == 200

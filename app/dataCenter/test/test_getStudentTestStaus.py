import json
import re
import random
from pprint import pprint

import requests

from dataCenter.config.conf import getStudentTestStaus_url


def test_getStudentTestStaus(getStudentTestStaus_file,request_header):
    getStudentTestStaus_files = random.sample(getStudentTestStaus_file, 5)
    irs_account_locode_tag = {}
    for i in getStudentTestStaus_files:
        accoundid = re.match(r" \d+", i).group().strip()
        results =json.loads(re.sub(" .*value=","",i))
        irs_account_locode_tag.update({
            accoundid[::-1]:results
        })
    for k,v in irs_account_locode_tag.items():
        for u in range(1,10):
            data ={
                "appId": "debug",
                "token": "debug",
                "requestId": "666666",
                "accountId":k,
                "loCodes":list(v.keys())[:u]
            }
            response = requests.post(url=getStudentTestStaus_url, data=json.dumps(data), headers=request_header)
            res = json.loads(response.text)
            strout = []
            strout.append({
                "request_data": data,
                "request_response": res
            })
            pprint(strout)
            assert res.get("code") == 200

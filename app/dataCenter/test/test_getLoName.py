import random
import json
import requests
from dataCenter.config.conf import getloname_url


def test_getloname(getLoName_file,request_header):
    list_ = []
    for i in getLoName_file:
        getLoName_res = i.split("|")[2].strip()
        list_.append(getLoName_res)
    # 把 list_ 分成 len(list_) 份 ,并 append 一个列表里面, 每一份长度为 10
    a = [list_[i:i + 10] for i in range(0, len(list_), 10)]
    random.seed(10)
    # a list 里面取出任意 五个
    a1 = random.sample(a, 5)
    for i in a1:
        for u in range(1,len(i)):
            data = {
                "requestId":"666666",
                "loCodes": list_[:u] #list_[:u]
            }

            response = requests.post(url=getloname_url, data=json.dumps(data), headers=request_header)
            re = json.loads(response.text)
            assert re.get("code") == 200

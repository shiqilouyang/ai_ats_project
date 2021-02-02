import json

import pytest

from dataCenter.config.conf import *

#  pytest 先加载 fixture 装饰的函数, 返回值可以被使用
@pytest.fixture(scope="module")
def getLoName_file():
    with open(getLoName_path, 'r', encoding="utf-8")as f:
        getLoName_re = f.readlines()
        yield getLoName_re


@pytest.fixture(scope="module")
def getStudentLevel_math_file():
    with open(getStudentLevel_math_path, 'r', encoding="utf-8")as f:
        getStudentLevel = f.readlines()
        yield getStudentLevel


@pytest.fixture(scope="module")
def getStudentLoStudyCost_file():
    with open(getStudentLoStudyCost_path, 'r', encoding="utf-8")as f:
        getStudentLoStudyCost = f.readlines()
        yield getStudentLoStudyCost


@pytest.fixture(scope="module")
def getStudentQuestionList_file():
    with open(getStudentQuestionList_path, 'r', encoding="utf-8")as f:
        getStudentQuestionList = f.readlines()
        yield getStudentQuestionList


@pytest.fixture(scope="module")
def getStudentTestStaus_file():
    with open(getStudentTestStaus_path, 'r', encoding="utf-8")as f:
        getStudentTestStaus = f.readlines()
        yield getStudentTestStaus


@pytest.fixture(scope="module")
def studentLevelOfCourse_file():
    with open(studentLevelOfCourse_path, 'r', encoding="utf-8")as f:
        studentLevelOfCourse = json.load(f)
        yield studentLevelOfCourse


#  包装请求 header
@pytest.fixture(scope="module")
def request_header():
    return {
       'Content-Type': 'application/json',
        'x-ale-key': 'key',
        "x-ale-sign": "秘钥".encode("utf-8"),
        "x-ale-timestamp": "当前时间戳(毫秒)".encode("utf-8")
    }
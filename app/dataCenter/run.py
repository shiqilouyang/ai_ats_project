'''
allure 使用文档
https://cloud.tencent.com/developer/article/1516907

运行命令:
    pytest
    copy environment.xml allure-results
    allure generate allure-results -o allure-reports/ --clean
    allure open -h 127.0.0.1 -p 8883 ./allure-reports


pytest.ini 配置了 pytest 启动参数 --clean-alluredir 表示每次启动都会清除历史运行记录

environment.xml  保存了 allure 配置参数, 但是需要在 allure-results 目录之中才能生效,所以linux/win每次启动都要 cp/copy

'''

import os
import subprocess

if __name__ == '__main__':
    ''' 测试实例启动脚本  '''
    dataCents_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    environment_path = os.path.join(dataCents_path, "environment.xml")
    allure_results_path = os.path.join(dataCents_path, "allure-results")
    allure_reports_path = os.path.join(dataCents_path, "allure-reports")
    cmds = [
        "cd {} & pytest".format(dataCents_path),
        'copy {} {}'.format(environment_path,allure_results_path),
        'allure generate {} -o {} --clean'.format(allure_results_path,allure_reports_path),
        'allure open -h 127.0.0.1 -p 8883 {}'.format(allure_reports_path)
    ]
    for i in cmds:
        child = subprocess.Popen(i,shell=True)
        child.wait()

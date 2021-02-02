from conf.Setting import userId, html_path
import pandas as pd


class HtmlMake():
    def __init__(self):
        self.d = {}

    def primarySchoolHtmlMake(self,data):
        testmodulerule = data.get("testmodeRule")
        studymodulerule = data.get("studymodeRule")
        restartmodulerule = data.get("restudymodeRule")
        testcheckModeNum = data.get("testcheckModeNum")
        studycheckModeNum = data.get("studycheckModeNum")
        rate = data.get("rate")
        ik_t = data.get("ik_t"),
        ik_s = data.get("ik_s"),
        ik_r = data.get("ik_r"),
        ik_tc = data.get("ik_tc"),
        ik_sc = data.get("ik_sc"),
        # result 按照列
        result = [
            [u'测试模块', u'学习模块', u'重学习模块',u'补漏测模块',u'补漏学模块'],
            [rate, rate, rate, rate, rate],
            [testmodulerule, studymodulerule, restartmodulerule,testcheckModeNum,studycheckModeNum],
            [ik_t, ik_s, ik_r,ik_tc,ik_sc]
        ]
        # title 按照行
        title = [u'模块', u'正答率', u'{}规则'.format(data.get("mesaage")), '是否测试通过']
        with open(html_path.format(data.get("u")), "a+", encoding="UTF-8") as f:
            f.write(self.convertToHtml(result, title))

    def convertToHtml(self,result, title):
        self.d = {}
        index = 0
        for t in title:
            self.d[t] = result[index]
            index = index + 1
        pd.set_option('max_colwidth', 20)
        df = pd.DataFrame(self.d)
        df = df[title]
        h = df.to_html(index=False)
        return h

# if __name__ == '__main__':
#     HtmlMake().primarySchoolHtmlMake()
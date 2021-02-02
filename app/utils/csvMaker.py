import csv
from pprint import pprint

from TestPoolModel.model import  models_
from conf.Setting import execl_path



class CsvMaker():
    def __init__(self, userId, session_id,d=None):
        self.userId = userId
        # self.d 课程中文名称
        self.d = d
        self.session_id = session_id
        self.outfile = \
            open(execl_path.format(self.userId), "a+", encoding="utf-8", newline="")
    def make(self):

        outcsv = csv.writer(self.outfile)
        headers = ["loCode", 'ability', "curPoolCode", 'usage', 'score', 'rate', 'itemId',self.d]
        header = ["loCode", 'ability', "curPoolCode", 'usage', 'score','rate','itemId']
        ends = ["", "", "","","",'','','']
        records = models_[self.userId[-1]].query.with_entities(
            models_[self.userId[-1]].score,
            models_[self.userId[-1]].ability,
            models_[self.userId[-1]].curPoolCode,
            models_[self.userId[-1]].loCode,
            models_[self.userId[-1]].usage,
            models_[self.userId[-1]].rate,
            models_[self.userId[-1]].itemId
        ).filter(models_[self.userId[-1]].user_id == self.userId)\
        .filter(models_[self.userId[-1]].session_id == self.session_id) \
        .all()

        # [getattr(record, c) for c in header]
        outcsv.writerow(headers)
        for record in records:
            outcsv.writerow([getattr(record, c) for c in header])
        #     生成三行
        outcsv.writerow(ends)
        outcsv.writerow(ends)
        outcsv.writerow(ends)
        self.outfile.close()


# userId = 'xfl-4684-1608255799'
# sessionId = '334937013644986368'
# CsvMaker(userId,sessionId).make()


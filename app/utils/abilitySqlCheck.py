'''
engine = create_engine('presto://emr-header-1:9090/hive')
df = pd.read_sql(
     "select  question_id, lo_code, ans, abilitys
      from default.testrecord where  length(ans) % 100 =  " + sys.argv[1] ,engine
  )

select distinct user_id from dwb.k_ale_result where dt = '20210226'


'''

import pandas as pd
from sqlalchemy.engine import create_engine
import asyncio
import aiomysql

from utils.loger_ import SetLog

loger = SetLog("abilitySqlCheck")

# 准备语句
sql = "select distinct user_id from dwb.k_ale_result where dt = '20210226'"

engine1 = create_engine('presto://10.30.28.108:9090/hive')

# 获取数据
df = pd.read_sql(sql, engine1)

user_id_list = []
for i in df["user_id"]:
    user_id_list.append(i)


async def check_data_from_prod(u):
    conn = await aiomysql.connect(host="10.30.31.245", port=3306,
                                  user='db_read', password='Yixuedb@2018',
                                  db='sc_normal_math', charset='utf8')
    cursor = await conn.cursor()

    for i in range(16):
        table_name = 'ale_lo_status_{}'.format(i)
        sql = '''select module_code,user_id,session_id,
                lo_code,lo_status,lo_reason,finally_ability,create_time from
              {} where  user_id like "{}%" and module_code = 'TEST_MODULE'
              and DATEDIFF(create_time,NOW())=0  and
              ((lo_status = "PASSED" and finally_ability < 0.7)
              or (lo_status = "FAILED" and finally_ability >= 0.7));'''.format(
            table_name, u)
        try:
            s = await cursor.execute(sql)
            result = await cursor.fetchall()
            if len(result) != 0:
                loger.error(result)
                assert len(result) == 0
        except Exception as e:
            print('执行Mysql: %s 时出错：%s' % (sql, e))
    await cursor.close()
    conn.close()


if __name__ == '__main__':
    split_list = [user_id_list[i:i + 100] for i in range(0, len(user_id_list), 100)]
    for user_id_list1 in split_list:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*(check_data_from_prod(str(g)) for g in user_id_list1)))





'''
  mysql ---> section_id 
  mongo ----> groupId()  db.getCollection("ALE_SECTION").find({"sectionId":"10000709"},{"ruleGroupId":1,'_id':0})
        ----> subGroupId() 列表   db.getCollection("ALE_GROUP_GROUP").find({"groupId":"40101"},{"subGroupId":1,'_id':0})
        ----> defaultTargetType   db.getCollection("ALE_GOAL").find({"groupId":"40101_06"},{"defaultTargetType":1,'_id':0})
             正答率:  RIGHTRATE_04 
'''

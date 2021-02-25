'''

   userId 在 operationtableTester 之中, 当前时间的前12小时

'''


import asyncio
import aiomysql
import time
import datetime


# "autoTest-xfl-4684-" + str(int(round(time.time())))
from TestPoolModel.model import OperationtableTester
operationtableTester_query_all_userId_list = []
operationtableTester_query_all = OperationtableTester.query.all()
for i in operationtableTester_query_all:
	operationtableTester_query_all_userId_list.append(i.user_id)

operationtableTester_query_all_userId_list = list(set(operationtableTester_query_all_userId_list))

t=datetime.datetime.now()
#12小时前
t2=(t-datetime.timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")
#12 小时之前的时间戳
ts2=time.mktime(time.strptime(t2, '%Y-%m-%d %H:%M:%S'))


operationtableTester_query_all_userId_list_ = []
for i in operationtableTester_query_all_userId_list:
	if ts2 < float(i[18:28] + '0'):
		operationtableTester_query_all_userId_list_.append(i)


async def basic_test(user_id):
	conn = await aiomysql.connect(host="106.14.214.32", port=3306,
								  user='db_admin', password='hello@2017',
								  db='sc_normal_math', charset='utf8')
	cursor = await conn.cursor()

	for i in range(16):
		table_name = 'ale_lo_status_{}'.format(i)
		sql = '''select * from  {} where  user_id like "{}%" and module_code = 'TEST_MODULE'  and ((lo_status = "PASSED" and finally_ability < 0.7) or (lo_status = "FAILED" and finally_ability >= 0.7));'''.format(
			table_name, user_id[:28] + '0')
		try:
			s = await cursor.execute(sql)
			print("OK")
			result = await cursor.fetchall()
			assert len(result) == 0
		except Exception as e:
			print('执行Mysql: %s 时出错：%s' % (sql, e))
	await cursor.close()
	conn.close()

while 1:
	time.sleep(1)
	loop = asyncio.get_event_loop()
	if operationtableTester_query_all_userId_list_ != []:
		loop.run_until_complete(asyncio.gather(*(basic_test(str(g)) for g in operationtableTester_query_all_userId_list_)))
	else:
		print("没有找到 userID")

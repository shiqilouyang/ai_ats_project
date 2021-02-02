import asyncio
import aiomysql
import time
import MySQLdb

from utils.loger_ import SetLog


loger = SetLog("abilitySqlCheck")

def get_data_from_test( ):

	sql = '''select distinct user_id from operation_table_tester ;'''

	# 打开数据库连接
	# 测试数据库
	db = MySQLdb.connect("10.31.210.18", "db_admin", "Projectx@2017", "sc_normal_center", charset='utf8')

	cursor = db.cursor()

	cursor.execute(sql)

	data = cursor.fetchall()
	list_user = []
	for i in data:
		list_user += list(i)
	db.close()
	list_user_ = []
	for i in list_user:
		a = i[0:28]
		list_user_.append(a)
	list_user_ = list(set(list_user_))
	return list_user_


async def check_data_from_prod():

	user_id = get_data_from_test()
	# 生产数据库
	conn = await aiomysql.connect(host="10.30.31.245", port=3306,
								  user='db_read', password='Yixuedb@2018',
								  db='sc_normal_math', charset='utf8')
	cursor = await conn.cursor()

	#  TODO 每次使用 检查 userId 根据 user_id 进行调整 u[0:28]
	for i in range(16):
		table_name = 'ale_lo_status_{}'.format(i)
		for u in user_id:
			sql = '''select module_code,user_id,session_id,
				lo_code,lo_status,lo_reason,finally_ability,create_time from
			  {} where  user_id like "{}%" and module_code = 'TEST_MODULE' 
			  and DATEDIFF(create_time,NOW())=0  and 
			  ((lo_status = "PASSED" and finally_ability < 0.7) 
			  or (lo_status = "FAILED" and finally_ability >= 0.7));'''.format(
				table_name, u[0:28])
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



num = 1
while 1:
	time.sleep(2)
	print("------------开始全局扫描第{}次---------".format(num))
	loop = asyncio.get_event_loop()
	loop.run_until_complete(check_data_from_prod())
	print("--------------全局扫描第{}次over---------".format(num))
	num +=1



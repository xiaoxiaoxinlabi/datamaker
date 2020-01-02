#coding:utf-8

import mysql.connector
import collections
import sys
sys.path.append("..")
from entity.columns import ColumnName 

class SqlJdbc:



	def __init__(self, database, table, cloumn, number):

		self.databaseName = database
		self.tableName = table
		self.cloumn = cloumn
		self.number = number

		config = {

		'user':'root',
		'password':'root',
		'host':'localhost'
		}

		self.conn = mysql.connector.connect(**config)
		self.cur = self.conn.cursor()

	




	def insert_data(self):

		self.create_table()


		for i in range(self.number):

			vals = []

			for clo in range(len(self.cloumn)):


				if isinstance(ColumnName(self.cloumn[clo]).getfile(),collections.Iterable):

					val = ''.join(ColumnName(self.cloumn[clo]).getfile())

				else:

					val = ColumnName(self.cloumn[clo]).getfile()

				
				vals.append(val)


			sql5 = "insert into %s  values %s;" %(self.tableName ,tuple(vals))
			print(sql5)

			self.cur.execute(sql5)
			self.conn.commit()

		
		



	def create_database(self):

		sql1 = "create database if not exists %s " %self.databaseName
		sql2 = "use %s" %self.databaseName
		
		self.cur.execute(sql1)
		self.cur.execute(sql2)
	
	



	def create_table(self):

		self.create_database()

		fileds = ''
		filed_type = ['int(11)', 'datatime','varchar(255)']

		for filed in self.cloumn:

			if filed == 'id':

				fileds = fileds + ' ' + filed + ' ' + filed_type[0] + ','

			elif filed == 'ymd':

				fileds = fileds + ' ' + filed + ' ' + filed_type[1] + ','

			else:

				fileds = fileds + ' ' + filed +' '+ filed_type[2] + ','

	
		sql3 = "create table if not exists %s (%s)" %(self.tableName , fileds[:-1])

		self.cur.execute(sql3)


		







if __name__ == '__main__':
	cloumn = ['id','name','gender']

	SqlJdbc('ggs22','test1',cloumn, 5).insert_data()

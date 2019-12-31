#coding:utf-8

import sys
import mysql.connector
sys.path.append('..')


class SqlJdbc:



	def __init__(self, database, table, cloumn):

		self.databaseName = database
		self.tableName = table
		self.cloumn = cloumn
		config = {'user':'root','password':'root','host':'localhost'}
		self.conn = mysql.connector.connect(**config)
		self.cur = self.conn.cursor()

	

	def create_database(self):

		sql1 = "create database %s " %self.databaseName
		sql2 = "use %s" %self.databaseName
		
		self.cur.execute(sql1)
		self.cur.execute(sql2)
	
	




	def create_table(self):
		self.create_database()

		fileds = ''
		filed_type = 'varchar(255)'
		for key in self.cloumn:
			fileds = fileds + ' ' + key +' '+ filed_type + ','
	
		sql3 = "create table %s (%s)" %(self.tableName , fileds[:-1])
		self.cur.execute(sql3)



	def insert_data(self):
		pass



if __name__ == '__main__':
	cloumn = ['id','name','gender']
	SqlJdbc('ggs22','test1',cloumn).create_table()
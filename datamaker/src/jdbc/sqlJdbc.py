#coding:utf-8

import mysql.connector
import collections
import sys
sys.path.append("..")
from src.entity.columns import ColumnName 
from utils import util

import random



class SqlJdbc:




	def __init__(self, number, cloumn, name='test', **config ):

		self.database_name = name
		self.table_name = name+str(util.get_time()) 
		self.cloumn = cloumn
		self.number = number

		dbinfo = {

		'user':'root',
		'password':'root',
		'host':'localhost'}

		self.conn = mysql.connector.connect(**config if config else dbinfo)
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


			sql5 = "insert into %s values %s;" %(self.table_name ,tuple(vals))
			print(sql5)

			self.cur.execute(sql5)
			self.conn.commit()

		self.cur.close()
		self.conn.close()

	

		
		



	def create_database(self):

		sql1 = "create database if not exists %s " %self.database_name
		sql2 = "use %s" %self.database_name
		
		self.cur.execute(sql1)
		self.cur.execute(sql2)


	



	def create_table(self):

		self.create_database()

		fileds = ''
		filed_type = ['int(11)', 'datetime','varchar(255)']

		for filed in self.cloumn:

			if filed == 'id':

				fileds = fileds + ' ' + filed + ' ' + filed_type[0] + ','

			elif filed == 'ymd':

				fileds = fileds + ' ' + filed + ' ' + filed_type[1] + ','

			else:

				fileds = fileds + ' ' + filed +' '+ filed_type[2] + ','

	
		sql3 = "create table if not exists %s (%s)" %(self.table_name , fileds[:-1])

		self.cur.execute(sql3)

		




	

		





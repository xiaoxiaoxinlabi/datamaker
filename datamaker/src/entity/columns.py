#coding:utf8

import sys
sys.path.append("..")
from randoms import datas as r 

class ColumnName(object):



	def __init__(self, fieldname):

	   self.fieldname = fieldname



	def getfile(self):


		if self.fieldname == 'name':

			return r.random_chinese()

		elif self.fieldname == 'email':

			return r.random_email()

		elif self.fieldname == 'phone':

			return r.random_phone()

		elif self.fieldname == 'id':
			return r.randomint()

		elif self.fieldname == 'gender':

			return r.random_gender()
		elif self.fieldname == 'marriage':
			return r.random_marr()

		elif self.fieldname == 'ymd':
			return r.random_ymd()

		elif self.fieldname == 'ip':
			return r.random_ipv4()

		elif self.fieldname == 'perId':
			return r.random_id_number()

		elif self.fieldname == 'age':

			return r.random_age()

		elif self.fieldname == 'industries':
			return r.random_industries()

		elif self.fieldname == 'politics':
			return r.random_politics()

		elif self.fieldname == 'schoolName':
			return r.random_schoolName()

		elif self.fieldname == 'degree':
			return r.random_degree()
		elif self.fieldname == 'field':
			return r.random_filed_of_study()

		else:
			return 'unknow fieldname'



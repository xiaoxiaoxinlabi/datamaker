#coding:utf8

import sys
sys.path.append("..")
import src.randoms.datas as r

class ColumnName(object):



	def __init__(self, filename):

	   self.filename = filename



	def getfile(self):


		if self.filename == 'name':

			return r.random_chinese()

		elif self.filename == 'email':

			return r.random_email()

		elif self.filename == 'phone':

			return r.random_phone()

		elif self.filename == 'id':
			return r.randomint()

		elif self.filename == 'gender':

			return r.random_gender()
		elif self.filename == 'marriage':
			return r.random_marr()

		elif self.filename == 'ymd':
			return r.random_ymd()

		elif self.filename == 'ip':
			return r.random_ipv4()

		elif self.filename == 'perId':
			return r.random_id_number()

		elif self.filename == 'age':

			return r.random_age()

		elif self.filename == 'industries':
			return r.random_industries()

		elif self.filename == 'politics':
			return r.random_politics()

		elif self.filename == 'schoolName':
			return r.random_schoolName()

		elif self.filename == 'degree':
			return r.random_degree()
		elif self.filename == 'field':
			return r.random_filed_of_study()

		else:
			return 'unknow filename'



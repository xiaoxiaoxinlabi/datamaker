#coding:utf-8
import os
import sys
sys.path.append("..")
from src.jdbc.excelJdbc import ExcelJdbc
from src.jdbc.csvJdbc import CsvJdbc

from configparser import ConfigParser 


def do_main():

	cf = ConfigParser()
	cf.read(os.path.pardir + '/config/properties')
	number = int(cf.get('configs', 'number'))
	path = cf.get('configs', 'path')
	columns = (cf.get('configs','column').replace(' ','').split(','))
	ext  = (os.path.splitext(path)[1]).replace('.','')



	if ext == 'xls':
		ex = ExcelJdbc(number, path, columns)
		ex.writer_excel()
	elif ext == 'csv':
		cs = CsvJdbc(number, path, columns)
		cs.create_data()
	else:
		print('does not math file') 



if __name__ == '__main__':
    do_main()

 
#coding:utf-8

import sys
sys.path.append("..")

from src.jdbc.excelJdbc import ExcelJdbc
import time
import datetime

def fun():
    number = 100
    path = 'D://1234.xls'
    column = [ 'ymd']
    #column = ['id', 'perId', 'name', 'gender', 'email', 'phone']
    start_time = int(time.mktime(datetime.datetime.now().timetuple()))
    ex = ExcelJdbc(number, path, column)
    ex.writer_excel()
    end_time = int(time.mktime(datetime.datetime.now().timetuple()))

    d = (end_time - start_time)

    print(d)



if __name__ == '__main__':

    fun()



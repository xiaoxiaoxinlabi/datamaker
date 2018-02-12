#coding:utf-8

import sys,os
sys.path.append("..")

from src.jdbc.excelJdbc import ExcelJdbc
from src.jdbc.csvJdbc import CsvJdbc

import time
import datetime

def fun():
    number = 100
    path = 'D://1234.csv'
    #column = [ 'ymd']
    column = ['id', 'perId', 'name', 'gender', 'email', 'phone', 'ymd']
    start_time = int(time.mktime(datetime.datetime.now().timetuple()))
    #ex = ExcelJdbc(number, path, column)
    #ex.writer_excel()


    csv = CsvJdbc(number, path, column)
    csv.create_data()
    end_time = int(time.mktime(datetime.datetime.now().timetuple()))

    d = (end_time - start_time)

    print(d)



if __name__ == '__main__':

    fun()



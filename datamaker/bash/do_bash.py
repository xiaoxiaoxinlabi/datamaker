#coding:utf-8
import os
import sys
#sys.path.append("..")
sys.path.append('..')
from src.jdbc.excelJdbc import ExcelJdbc
from src.jdbc.csvJdbc import CsvJdbc
from src.jdbc.jsonJdbc import JsonJdbc

from configparser import ConfigParser 




def do_main():


    try:

        cf = ConfigParser()
        cf.read(os.path.pardir + '/config/properties', encoding='utf-8')
        number = cf.get('configs', 'number')
        path = cf.get('configs', 'path')
        columns = (cf.get('configs','column').replace(' ','').split(','))
        ext  = (os.path.splitext(path)[1]).replace('.','')
  

        if number != '' and  path != '' and columns != '':

            number = int(number)

            if ext == 'xls':
                ex = ExcelJdbc(number, path, columns)
                ex.writer_excel()
            elif ext == 'csv':
                cs = CsvJdbc(number, path, columns)
                cs.create_data()

            elif ext == 'json':
                
                cs = JsonJdbc(number, path, columns)
                cs.create_data()

            else:

            	print('only supported formats are：(csv，xls)')

        else:


            print('please input the value of the parameter in the properties')
        
      

    except Exception as e:

        print("Unexpected Error: {}".format(e))


  


if __name__ == '__main__':
    do_main()

 
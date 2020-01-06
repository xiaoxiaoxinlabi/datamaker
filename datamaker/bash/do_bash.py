#coding:utf-8
import os
import sys

sys.path.append('..')
from src.jdbc.excelJdbc import ExcelJdbc
from src.jdbc.csvJdbc import CsvJdbc
from src.jdbc.jsonJdbc import JsonJdbc
from src.jdbc.sqlJdbc import SqlJdbc

from configparser import ConfigParser 
import datetime



def do_main():

 

    try:

        cf = ConfigParser()
        cf.read(os.path.pardir + '/config/properties', encoding='utf-8')


        types = cf.get('formats', 'types')

        number = cf.get('configs', 'number')
        path = cf.get('configs', 'path')
        columns = (cf.get('configs','column').replace(' ','').split(','))

        ext  = (os.path.splitext(path)[1]).replace('.','')
        name = cf.get('formats','name')

        dbinfo = dict(cf.items('dbinfo'))

   
    

  

        if number != '' and  path != '' and columns != '' and types != '':

            number = int(number)

            if types == 'file':
 

                if ext == 'xls':
                    ex = ExcelJdbc(number, path, columns)
                    ex.writer_excel()
                elif ext == 'csv' or ext == '' or ext == 'txt':
                    cs = CsvJdbc(number, path, columns)
                    cs.create_data()

                elif ext == 'json':
                    
                    cs = JsonJdbc(number, path, columns)
                    cs.create_data()

                else:

                	print('only supported formats are：(csv,xls,json,txt)')

            elif types == 'mysql':

                    

                db = SqlJdbc(number, columns, name,  **dbinfo)
                db.insert_data()

        else:


            print('please input the value of the parameter in the properties')
        
      

    except Exception as e:

        print("Unexpected Error: {}".format(e))


  


if __name__ == '__main__':
    do_main()
   

 
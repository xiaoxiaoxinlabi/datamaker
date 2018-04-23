#coding:utf8
import sys

import collections

sys.path.append("..")


from src.entity.columns import ColumnName 
import random
import csv

class CsvJdbc:

    def __init__(self, number, path, column):
        self.number = number
        self.path = path
        self.column = column


    def create_data(self):
         
        columns = self.column

        m = self.number

        with open(self.path, 'w', newline = '') as csv_file:
        

            # todo csv.DictWriter()

            writer = csv.writer(csv_file)

            writer.writerow(self.column)

            while m > 0:

                datas = []

                for i in range(len(columns)):


                    if isinstance(ColumnName(columns[i]).getfile(), collections.Iterable):
                        
                        rows = ''.join(ColumnName(columns[i]).getfile())
                    else:
                        rows = ColumnName(columns[i]).getfile()

                    datas.append(rows)
                
                writer.writerow(datas)

                print('number = ',self.number - m + 1)

                m = m - 1

        csv_file.close()





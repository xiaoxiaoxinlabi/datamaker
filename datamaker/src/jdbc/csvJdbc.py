#coding:utf8
import sys

sys.path.append("..")
import random

from src.entity.columns import ColumnName 

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

                    datas.append(ColumnName(columns[i]).getfile())
                
                writer.writerow(datas)

                m = m - 1

        csv_file.close()





if __name__ == '__main__':
    clo = ['id', 'perId', 'name']

    c = CsvJdbc(100, 'D://1.csv', clo )

    c.create_data()



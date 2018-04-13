#coding:utf-8
import sys
sys.path.append("..")
from src.entity.columns import ColumnName 


import json

import collections



class JsonJdbc:

    def __init__(self, number, path , cloumn):

        self.number = number
        self.path = path
        self.cloumn = cloumn



    def create_data(self):

        cloumns = self.cloumn

        m = self.number

        arrayDatas = []



        with open(self.path, 'w') as json_file:

            while m > 0:

                datas = {}


                for i in range(len(cloumns)):

                   
                    if isinstance(ColumnName(cloumns[i]).getfile(), collections.Iterable):

                    	datas[cloumns[i]] = ''.join(ColumnName(cloumns[i]).getfile())

                    else:

                    	datas[cloumns[i]] = ColumnName(cloumns[i]).getfile()

          

                arrayDatas.append(datas)


                m = m - 1

            json.dump(arrayDatas, json_file, ensure_ascii = False, indent = 0)

            json_file.close()




          


           





            

            

                






        
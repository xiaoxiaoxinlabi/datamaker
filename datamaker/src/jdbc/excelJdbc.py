#coding:utf8
import sys

sys.path.append("..")
import random
import xlrd
import xlwt
from src.entity.columns import ColumnName 


class ExcelJdbc:



    def __init__(self, number, path, column):

        self.number = number
        self.path = path
        self.column = column
        self.cols = len(self.column)
        self.suffix = 0
        self.excel = xlwt.Workbook()
        self.sheet = self.create_sheet()
        self.rows = 1



    def create_sheet(self):

        self.suffix = self.suffix + 1
        sheet =  self.excel.add_sheet('Sheet' + str(self.suffix))  
        return sheet

        

    def create_title(self):

        sheet = self.sheet

        for i in range(self.cols):

            sheet.write(0, i ,self.column[i])

        return sheet


    def create_data(self, rows, isNewSheet = False, isNewTitle = False):

        if isNewSheet:
            if isNewTitle:

                self.sheet = self.create_sheet()
                self.create_title()

        elif isNewTitle:
            self.create_title()

        ex = self.excel
        columns = self.column

        datas = []
        for i in range(len(columns)):
            datas.append(ColumnName(columns[i]).getfile())


        for j in range(len(datas)):

            print('rows =', rows)
                
            self.sheet.write(rows, j, datas[j])



    def writer_excel(self):

       
        m = self.number
        while m > 0:

            if  self.rows <= 1:
            
                self.create_data(self.rows, False, True)

            elif self.rows > 65535:
                self.rows = 1

                self.create_data(self.rows, True, True)
            else:

                self.create_data(self.rows)

            self.rows = self.rows + 1

           
            m = m - 1

        self.create_save()

     

    def create_save(self):

        self.excel.save(self.path)










        



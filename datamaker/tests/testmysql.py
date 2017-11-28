#coding:utf8

from source.jdbc.mysqlJdbc import MysqlJdbc
import random_data  as r
import random
import time


class Test1(MysqlJdbc):

    def insert(self, sql):
        
        start_time = time.strftime('%H:%M:%S')
        for i in range(5000):
 
            #self.execute(sql2, (i,  r.random_chinese(),  r.random_email()))
            values =[(i, r.random_chinese(),  r.random_email(), r.random_phone())]
            self.executemany(sql2, values)
            #self.commit()

        end_time = time.strftime('%H:%M:%S')

        print(start_time + "," + end_time)
       
        self.close()


    

    def insert_executemany(self, sql):
        start_time = time.strftime('%H:%M:%S')
        for i in range(1, 1000):
            datas = []
            #datas.append((i, r.random_chinese(),  r.random_email(), r.random_phone(), r.random_gender(), r.random_marr(), r.random_id_number(), r.random_age(), r.random_ymd()))
            datas.append((i, r.random_chinese(),  r.random_email()))

        
            if i % 100 == 0:
                print(i)
                self.executemany(sql2, datas)
                self.commit()

            self.executemany(sql2, datas)
            self.commit()

         
        self.close()

        end_time = time.strftime('%H:%M:%S')
        print(end_time +", "+ start_time)








    def insert_execute(self, sql):
        start_time = time.strftime('%H:%M:%S')
        for i in range(10000):
            
            self.execute(sql2, (i, r.random_chinese(),  r.random_email(), r.random_phone(), r.random_gender(), r.random_marr(), r.random_id_number(), r.random_age(), r.random_ymd()))

        self.commit()
        self.close()
        end_time = time.strftime('%H:%M:%S')

        print(end_time +","+ start_time)








if __name__ == '__main__':
    t = Test1('172.24.8.134', 3306, 'datamaster', 'datA123!@#', 'data_for_test')
    #t = Test1('127.0.0.1', 3306, 'root', 'root', 'testdata')

    #sql = "insert into test1(id, name, class) values(%s, %s, %s)"
    #sql2 = "insert into test2(id, name, age, salary, gender) values(%s, %s, %s, %s, %s)"
    #sql2 = "insert into 07181446_innodb(id, name, email, phone, gender, marriage, perid, age, perbirthday) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql2 = "insert into test_5000(id, name, email, phone) values(%s, %s, %s, %s)"
   
    #t.insert(sql2)
    t.insert(sql2)
    #t.insert_execute(sql2)






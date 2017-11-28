#coding:utf-8

import sys
sys.path.append("..")
from  parserfiles.parsers  import Parsers

import pymysql



class MysqlJdbc(Parsers):


    
    def __init__(self, configs):

        
        super(MysqlJdbc, self).__init__(configs)
        #Parsers.__init__(self, configs)
        self.host = self.get('server', 'host') or 'localhost'
        self.port = int(self.get('server', 'port')) or 3306
        self.user = self.get('server', 'user')
        self.passwd = self.get('server', 'password')
        self.db = self.get('server', 'dbname')
        
        self.conn = pymysql.connect(host = self.host, port = self.port, user = self.user, passwd = self.passwd, db = self.db, charset = 'utf8')
                            
    def connection(self):
   
        return self.conn.cursor()

    def execute(self, sql, args = None, multi = True):
  
         self.connection().execute(sql, args)
       
    def executemany(self, sql, args = None):
        self.connection().executemany(sql, args)

    def commit(self):
        
        return self.conn.commit()


    def close(self):

        cur = self.connection()

        if self.conn != None:
            if cur != None:
                cur.close()

            self.conn.close()






if __name__ == '__main__':
    p = 'E:\ssgongproject\ssgongGit\datamaker\src\config\mysql.conf'
    m = MysqlJdbc(p)
    print(m.host)






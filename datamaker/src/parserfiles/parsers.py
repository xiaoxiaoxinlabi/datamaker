#coding:utf8

import ConfigParser


class Parsers(object):
    def __init__(self, file):
        self.conf = ConfigParser.ConfigParser()
        self.file = file


    def file_read(self):
        config = self.conf
        with open(self.file, 'r', encoding = 'utf8') as f:
            config.readfp(f)

        return config


    def get(self, item, propertry):
        c = self.file_read()
        return c.get(item, propertry)




if __name__== '__main__':
    c = Parsers('E:\ssgongproject\ssgongGit\datamaker\src\config\mysql.conf')

    host = c.get('server', 'host')
    port = c.get('server', 'port')
    print(host, port)
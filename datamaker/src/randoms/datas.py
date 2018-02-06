#coding:utf8
import sys,os
sys.path.append("..")
import random

from datetime import datetime, timedelta
import socket
import struct
import time
import os



#随机产生一个整数
def randomint(start = 0, end = 100):

  return random.randint(start, end)


#产生一个浮点数
def random_unint(start = 0, end = 100):

  return random.uniform(start, end)

#姓名
def random_chinese():

    firstnames = []

    with open(os.path.dirname(__file__)+ '/firstname.txt', 'r', encoding = 'utf-8') as f:
      data = f.read()
      firstname_list = data.replace('\n', ',' ).split(',')

    for x in firstname_list:
      firstnames.append(x)


    lastnames = []

    with open(os.path.dirname(__file__) +'/lastname.txt', 'r', encoding = 'utf-8') as f:
      data = f.read()
      lastname_list = data.split(',')

    for x in lastname_list:
      lastnames.append(x)


    full_name = ''.join(random.sample(firstnames, 1) + random.sample(lastnames, 2))

    return full_name


def random_char():
    
    newchars = ''
    for i in range(ord('a'), ord('z') + 1):
        newchars = newchars + chr(i) 

    return newchars



def random_int():

    return random.randrange(1,100)

def random_gender():
    gender_list = ('男', '女', '未知')
    return random.sample(gender_list, 1)


def random_phone():
    phone_pre = ["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188","182"]
    return random.choice(phone_pre) +''.join(random.choice("0123456789") for i in range(8))
    


def random_marr():
    marr_list = ('已婚', '未婚', '未知')
    return random.sample(marr_list, 1)


def random_email():
    
    email_suff = []

    with open(os.path.dirname(__file__) +'/email_suff.txt') as f:
      data = f.read()
      email_suff = data.lower().split(',')


    email_pre = "0123456789" + random_char() + '_'

    email =  ''.join(random.sample(email_pre, 8)  + random.sample(email_suff, 1))


    return email



def random_ipv4():
 
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))



def random_id_number():
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18), random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
    y = 0

    for i in range(17):
        y = y + int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])


#行业
def random_industries():
    industries_list = ('保险业', '电讯业', '公益组织', '电讯业', '航空航天', '化学', '造纸', '因特网', '银行', '金融', '邮政快递', '设计', '医疗服务', '学术研究', '体育运动', '司机', '游业', '律师', '媒体', '美容', '计算机', '大数据', '房地产')
    return random.sample(industries_list, 1)


#涉华因素
def random_politics():
    politics_list = ('是','否', '未知')
    return random.sample(politics_list, 1)


#学校名称
def random_schoolName():
    schoolname_list = (
     'University of Cambridge','University of Oxford',
     'Durham University', 'University of St Andrews',
     'Imperial College London', 'University College London',
     'University of Warwick', 'University of Leeds', 
     'University of East Anglia', 'University of Birmingham',
     'University of Bristol', 'University of Sheffield', 'HarvardUniversity')
    return random.sample(schoolname_list, 1)

#学位
def random_degree():
    degree_list = ('博士后','博士','硕士', '本科', '大专', '高中', '初中', '小学' , '其他', '未知')
    return random.sample(degree_list, 1)

#行业领域
def random_filed_of_study():
    filed_list = ('sociology ', 'economics ', 'civil and environmental engineering ', 'management ', 'industrial and labor relations', 'applied economics and management', 'policy analysis and management', 'IT')
    return random.sample(filed_list, 1)



#todo 时间效率
def random_ymd( start = "1900-01-01", end = "2017-01-01", format="%Y-%m-%d"):


    end_time = datetime.strptime(end, format)
    start_time = datetime.strptime(start, format)

    days = (end_time - start_time).days


    return random.sample([datetime.strftime(start_time + timedelta(i), format) for i in range(0, days)], 1)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/24 14:57
# @Author : LiangJiangHao
# @Software: PyCharm
import pymysql
import datetime

class biliTable(object):
    def __init__(self):
        self.client =pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='bili',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor

        )
        self.cur = self.client.cursor()
    def selectStr(self):
        sql='select * from bili limit 10000 '
        self.cur.execute(sql)
        dataArr=self.cur.fetchall()
        # print(dataArr)
        return dataArr

now_time = datetime.datetime.now()
print(now_time)

bili=biliTable()
dataArr=bili.selectStr()
#
print(len(dataArr))

new_time = datetime.datetime.now()
print(new_time-now_time)
# n_1kw=0
# n_2kw=0
# n_3kw=0
# n_4kw=0
# n_error=0
# for video in dataArr:
#     url=video['videoUrl']
#     aid=url.split('aid=')[1]
#     print(aid)
#     if int(aid)<10000000:
#         n_1kw+=1
#     elif int(aid)<20000000:
#         n_2kw+=1
#     elif int(aid)<30000000:
#         n_3kw+=1
#     elif int(aid)<40000000:
#         n_4kw+=1
#     else:
#         n_error+=1
# resultStr='n_1kw=%s,n_2kw=%s,n_3kw=%s,n_4kw=%s,n_error=%s'%(n_1kw,n_2kw,n_3kw,n_4kw,n_error)
# print(resultStr)
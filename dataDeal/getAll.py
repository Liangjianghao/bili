#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/25 16:51
# @Author : LiangJiangHao
# @Software: PyCharm

import pymysql
import datetime
from dateutil import parser
import time

createTableStr="CREATE TABLE `biliR` (" \
               "`Id` int(11) NOT NULL AUTO_INCREMENT," \
               "`video_title` varchar(255) DEFAULT NULL COMMENT '视频标题'," \
               "`video_author` varchar(255) DEFAULT NULL COMMENT '视频作者'," \
               "`video_uploadtime` date DEFAULT NULL COMMENT'更新时间'," \
               "`playNum` int(11) DEFAULT NULL COMMENT '播放'," \
               "`allPlayNum` int(11) DEFAULT NULL COMMENT '总播放'," \
               "PRIMARY KEY (`Id`)" \
               ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='b站结果表';"

baseTable='bili'
baseTime='2009-7-1'
baseTime='2010-8-27'

tableName='biliR'
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='bili',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)
cursor = connect.cursor()

def createMomentTable():
    print('createMomentTable')

def getinfor(timeStr):

    datetime_oneDay = timeStr + datetime.timedelta(days=1)
    # sql='SELECT * FROM bili WHERE uploadTime<"%s" ORDER BY playNum DESC LIMIT 20'%timeStr
    sql='SELECT * FROM (SELECT * FROM (SELECT * FROM bili WHERE uploadTime<"%s" ORDER BY playNum DESC LIMIT 20)t UNION SELECT * FROM (SELECT * FROM bili WHERE uploadTime BETWEEN "%s" AND "%s" ORDER BY playNum DESC LIMIT 20)t2)t3 ORDER BY playNum DESC LIMIT 20'%(timeStr,timeStr,datetime_oneDay)
    print(sql)
    cursor.execute(sql)
    connect.commit()
    data = cursor.fetchall()
    return data

def getTodata(timeStr):
    datetime_oneDay = timeStr + datetime.timedelta(days=1)
    sql='SELECT * FROM bili WHERE uploadTime BETWEEN "%s" AND "%s" ORDER BY playNum DESC LIMIT 20'%(timeStr,datetime_oneDay)
    print(sql)
    cursor.execute(sql)
    connect.commit()
    data = cursor.fetchall()
    return data

def changeArr(baseArr,newArr):
    print('changeArr')

datetime_start = parser.parse(baseTime)
nowTime = datetime.datetime.now()  # 现在
while datetime_start<nowTime:
    datetime_start = datetime_start + datetime.timedelta(days=1)
    print('处理时间段%s'%(datetime_start))
    videoArr=getinfor(datetime_start)
    todayVideoArr=getTodata(datetime_start)
    changeArr(videoArr,todayVideoArr)
    time.sleep(100)

    # print(len(videoArr))
    # print(videoArr)
    # for index,video in enumerate(videoArr):
    #     video_title = video['videoTitle']
    #     video_author = video['userName']
    #     video_uploadtime = str(video['uploadTime'])[0:10]
    #     playNum = video['playNum']
    #     allPlayNum = video['playNum']
        # sql = "insert into %s(video_title,video_author,video_uploadtime,playNum,allPlayNum)values ('%s','%s', '%s','%s','%s')" % (tableName,video_title, video_author, datetime_start, playNum, allPlayNum)
        # cursor.execute(sql)
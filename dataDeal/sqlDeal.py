#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/25 22:12
# @Author : LiangJiangHao
# @Software: PyCharm


import pymysql
import datetime
from dateutil import parser
import time
from openpyxl import Workbook

start=time.clock()
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
baseTime='2007-7-5'
# baseTime='2009-7-14'
theKey='playNum'
theKey='saveNum'

keyWord='b收藏'


# tableName='biliR'
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

def getbeforeToday(timeStr):
    # print('getbeforeToday')

    # sql='SELECT * FROM (SELECT * FROM (SELECT * FROM bili WHERE uploadTime<"%s" ORDER BY playNum DESC LIMIT 20)t UNION SELECT * FROM (SELECT * FROM bili WHERE uploadTime BETWEEN "%s" AND "%s" ORDER BY playNum DESC LIMIT 20)t2)t3 ORDER BY playNum DESC LIMIT 20'%(timeStr,timeStr,datetime_oneDay)
    sql='insert into  newTable SELECT * FROM (SELECT * FROM bili WHERE uploadTime<"%s" ORDER BY %s DESC LIMIT 50)t'%(timeStr,theKey)
    # print(sql)
    cursor.execute(sql)
    connect.commit()
    # data = cursor.fetchall()
    # return data

def getTodata(timeStr):
    datetime_oneDay = timeStr + datetime.timedelta(days=1)
    # sql='INSERT INTO newTable SELECT * FROM(SELECT * FROM bili WHERE uploadTime BETWEEN "%s" AND "%s" ORDER BY playNum DESC LIMIT 1000)t2'%(timeStr,datetime_oneDay)
    # print(sql)
    sql='INSERT INTO newTable SELECT * FROM bili WHERE id IN (SELECT id FROM (SELECT id FROM bili WHERE uploadTime BETWEEN "%s" AND "%s" ORDER BY %s DESC LIMIT 1000) t ) LIMIT 20'%(timeStr,datetime_oneDay,theKey)
    cursor.execute(sql)
    connect.commit()
    data = cursor.fetchall()
    return data

def getNewTable(timeStr):
    deleteSql='DELETE FROM newTable WHERE id NOT IN (SELECT id FROM (SELECT id FROM newTable ORDER BY %s DESC LIMIT 20) t)'%theKey
    cursor.execute(deleteSql)
    sql='SELECT * FROM newTable ORDER BY %s DESC '%theKey
    # print(sql)
    cursor.execute(sql)
    connect.commit()
    data = cursor.fetchall()
    return data

def deleteTableData():
    print(deleteTableData)

def changeArr(baseArr,newArr):
    print('changeArr')

datetime_start = parser.parse(baseTime)
nowTime = datetime.datetime.now()  # 现在

testTime=parser.parse('2007-7-10')


firstTime=0

wb = Workbook()
sheet = wb.active
sheet.title = 'Sheet1'
sheet['A1'] = 'name'
sheet['B1'] = 'type'
sheet['C1'] = 'value'
sheet['D1'] = 'date'
allNumber = 0


while datetime_start<nowTime:
    datetime_start = datetime_start + datetime.timedelta(days=1)
    print('处理时间段%s'%(datetime_start))
    # print(firstTime)
    videoArr=[]
    if firstTime==0:
        getbeforeToday(datetime_start)
        firstTime+=1
    else:
        getTodata(datetime_start)
        videoArr=getNewTable(datetime_start)

    # changeArr(videoArr,todayVideoArr)
    # time.sleep(5)

    # print(len(videoArr))
    # print(videoArr)

    for index,video in enumerate(videoArr):
        theVideoId='av%s'%(video['videoUrl'].split('aid=')[1])
        video_title = video['videoTitle']
        video_author = video['userName']
        video_uploadtime = str(video['uploadTime'])[0:10]
        playNum = video['%s'%theKey]
        allPlayNum = video['playNum']
        # sql = "insert into %s(video_title,video_author,video_uploadtime,playNum,allPlayNum)values ('%s','%s', '%s','%s','%s')" % (tableName,video_title, theVideoId, datetime_start, playNum, allPlayNum)
        # cursor.execute(sql)

        sheet["A%d" % (allNumber + index+1 )].value = video_title
        sheet["B%d" % (allNumber + index+1)].value = video_author
        sheet["C%d" % (allNumber + index+1)].value = playNum
        sheet["D%d" % (allNumber + index+1)].value = datetime_start
    allNumber+=len(videoArr)


wb.save('%s_排行榜.csv'%keyWord)
end=time.clock()

print(end-start)

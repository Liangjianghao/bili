# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# CREATE TABLE `bili` (
#   `Id` int(11) NOT NULL AUTO_INCREMENT,
#   `videoTitle` varchar(255) DEFAULT NULL COMMENT '视频标题',
#   `videoUrl` varchar(255) DEFAULT NULL COMMENT '视频地址',
#   `videoCover` varchar(255) DEFAULT NULL COMMENT '封面地址',
#   `userName` varchar(255) DEFAULT NULL COMMENT '视频作者',
#   `uploadTime` datetime DEFAULT NULL COMMENT'视频上传时间',
#   `playNum` int(11) DEFAULT NULL COMMENT '播放',
#   `danmuNum` int(11) DEFAULT NULL COMMENT '弹幕数',
#   `contenNum` int(11) DEFAULT NULL COMMENT '评论数',
#   `saveNum` int(11) DEFAULT NULL COMMENT '收藏数',
#   `coinNum` int(11) DEFAULT NULL COMMENT '硬币数',
#   `likeNum` int(11) DEFAULT NULL COMMENT '喜欢数',
#   `dislikeNum` int(11) DEFAULT NULL COMMENT '不喜欢数',
#   `shareNum` int(11) DEFAULT NULL COMMENT '分享数',
#   `danmuID` int(11) DEFAULT NULL COMMENT '弹幕id',
#   PRIMARY KEY (`Id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='bili';

class BiliPipeline(object):
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
        self.item_list = []
    def process_item(self, item, spider):

        # insertStr = "insert into ac2018 (video_title,video_cover,video_url,video_author,video_uploadtime,playNum,danmuNum,comments,saveNum,xjNum,video_type,danmu_id,score)  values ('%s','%s', '%s','%s','%s','%s','%s','%s', '%s','%s','%s','%s','%s')"\
        #     %(item['title'],item['video_cover'],item['videoUrl'],item['video_author'],item['video_uploadtime'],item['playNum'],item['danmuNum'],item['comments'],item['saveNum'],item['xjNum'],item['video_type'],item['danmu_id'],item['score'])
        # self.cur.execute(insertStr)
        # self.client.commit()
        #
        self.item_list.append(item)
        # print('len is %s'%len(self.item_list))
        if len(self.item_list) >=10000:
            self.insert_item_list(spider)

    # videoTitle, videoUrl, videoCover, userName, uploadTime, playNum, danmuNum, contenNum, saveNum, coinNum, likeNum, dislikeNum, shareNum, danmuID
    def insert_item_list(self,spider):
        try:
            insertStr = 'replace into bili (videoTitle,videoUrl,videoCover,userName,uploadTime,playNum,danmuNum,contenNum,saveNum,coinNum,likeNum,dislikeNum,shareNum,danmuID)  values'
            for index,item in enumerate(self.item_list):
                print('%s--%s'%(index+1,item['videoTitle']))
                itemtr="('%s','%s', '%s','%s','%s','%s','%s', '%s','%s','%s','%s','%s', '%s','%s')"% \
                       (item['videoTitle'],item['videoUrl'],item['videoCover'],item['userName'],item['uploadTime'],item['playNum'],
                        item['danmuNum'],item['contenNum'],item['saveNum'],item['coinNum'],item['likeNum'],item['dislikeNum'],item['shareNum'],item['danmuID'])
                if index==len(self.item_list)-1:
                    insertStr+=itemtr+';'
                else:
                    insertStr+=itemtr+','
            # print('*****************************')
            # print(insertStr)
            if len(insertStr)>170:
                self.cur.execute(insertStr)
                self.client.commit()
            self.item_list=[]
        except Exception as e:
            print('insert_itemList:%s'%e)
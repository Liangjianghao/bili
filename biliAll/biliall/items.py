# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BiliItem(scrapy.Item):
    videoTitle = scrapy.Field()
    videoUrl = scrapy.Field()
    videoCover = scrapy.Field()
    userName = scrapy.Field()
    uploadTime = scrapy.Field()
    playNum = scrapy.Field()
    danmuNum = scrapy.Field()
    contenNum = scrapy.Field()
    saveNum = scrapy.Field()
    coinNum = scrapy.Field()
    likeNum = scrapy.Field()
    dislikeNum = scrapy.Field()
    shareNum = scrapy.Field()
    danmuID = scrapy.Field()
    videos = scrapy.Field()
    tid = scrapy.Field()
    tname = scrapy.Field()
    copyright = scrapy.Field()
    duration = scrapy.Field()

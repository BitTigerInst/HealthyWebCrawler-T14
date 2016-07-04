# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HealthyItem(scrapy.Item):
    # define the fields for your item here like:
    appurl = scrapy.Field()
    title = scrapy.Field()
    appid = scrapy.Field()
    category = scrapy.Field()
    cateid = scrapy.Field()
    developer = scrapy.Field()
    rating = scrapy.Field()
    ratingct = scrapy.Field()
    ver = scrapy.Field()
    updatetm = scrapy.Field()
    developerrec = scrapy.Field()
    relatedrec = scrapy.Field()


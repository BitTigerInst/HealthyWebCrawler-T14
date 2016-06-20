# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HealthyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    appid = scrapy.Field()
    app_name = scrapy.Field()
    recommended_d = scrapy.Field()
    recommended_r = scrapy.Field()
    developer = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    update_tm = scrapy.Field()
    category = scrapy.Field()
    version = scrapy.Field()

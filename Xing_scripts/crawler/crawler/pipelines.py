# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy import log

class XiaomiappPipeline(object):
    def process_item(self, item, spider):
        return item
        
class XiaomiAppstoreCrawlerPipeline(object):
    def __init__(self):
        #self.file = open('appstore.data', 'wb')
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.key = settings['MONGODB_UNIQUE_KEY']


    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            query = {}
            query[self.key] = item[self.key]
            search_result = self.collection.find_one(query)
            if not search_result:
                self.collection.insert(dict(item))
                log.msg("new app added to MongoDB database!",
                        level=log.DEBUG, spider=spider)
            else:
                self.collection.update(query, dict(item))

        return item
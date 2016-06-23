import pymongo
from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging

class HealthyPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            result = {}
            result[self.key] = item[self.key]
            search_result = self.collection.find_one(result)

            if search_result:
              logging.info("Skip duplicates")
              return item
            else:
              self.collection.insert(dict(item))
              log.msg("Item added to MongoDB database!",
                  level=log.DEBUG, spider=spider)
              return item 


    def __get_itemvalue__(self, item, value):
        if type(value) is str:
            return item[value] if value in item else None
        elif type(value) is list:
            return [item[key] if key in item else None for key in value]
        else:
            raise TypeError('Only string and list are valid sources')

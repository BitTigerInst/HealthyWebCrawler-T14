# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from elasticsearch import Elasticsearch, helpers
# from elasticsearch import Elasticsearch, RequestsHttpConnection, serializer, compat, exceptions, helpers
from scrapy.utils.project import get_project_settings

# from scrapy.conf import settings
from scrapy.exceptions import DropItem
# from scrapy import log

from datetime import datetime
import types

import pysolr
import logging


class XiaomiappPipeline(object):
    def process_item(self, item, spider):
        return item



class XiaomiElasticSearchPipeline(object):
    items_buffer = []

    def __init__(self):
        self.settings = get_project_settings()
        # settings = get_project_settings()
        # self.settings = settings
        uri = "{}:{}".format(self.settings['ELASTICSEARCH_SERVER'], self.settings['ELASTICSEARCH_PORT'])
        self.es = Elasticsearch([uri])

        # uri = "%s:%d" % (self.settings['ELASTICSEARCH_SERVER'], self.settings['ELASTICSEARCH_PORT'])
        # self.es = Elasticsearch(, serializer=JSONSerializerPython2())
        # print uri

        # print type(settings)

    def index_item(self, item):
        index_name = self.settings['ELASTICSEARCH_INDEX']
        index_suffix_format = self.settings.get('ELASTICSEARCH_INDEX_DATE_FORMAT', None)

        if index_suffix_format:
            index_name += "-" + datetime.strftime(datetime.now(), index_suffix_format)

        index_action = {
            '_index': index_name,
            '_type': self.settings['ELASTICSEARCH_TYPE'],
            '_source': dict(item)
        }

        self.items_buffer.append(index_action)

        # index_name = self.settings['ELASTICSEARCH_INDEX']
        # self.es.index(index_name, doc_type="test-type", body=dict(item), id=item['appid'], op_type='create')

        if len(self.items_buffer) == self.settings.get('ELASTICSEARCH_BUFFER_LENGTH', 500):
            self.send_items()
            self.items_buffer = []

    def send_items(self):
        helpers.bulk(self.es, self.items_buffer)

    def process_item(self, item, spider):
        if isinstance(item, types.GeneratorType) or isinstance(item, types.ListType):
            for each in item:
                self.process_item(each, spider)
        else:
            self.index_item(item)
        # index_name = self.settings['ELASTICSEARCH_INDEX']
        # self.es.index(dict(item), index_name, self.settings['ELASTICSEARCH_TYPE'], op_type='create')
        logging.info("Remove old values in Elasticsearch if exit")
        self.es.delete(self.settings['ELASTICSEARCH_INDEX'], self.settings['ELASTICSEARCH_TYPE'], id=item['appid'], ignore=[400, 404])
        self.es.index(self.settings['ELASTICSEARCH_INDEX'], self.settings['ELASTICSEARCH_TYPE'], dict(item), id=item['appid'], op_type='create', )
        # self.es.index()
        return item

    def close_spider(self, spider):
        if not self.items_buffer:
            self.send_items()

class XiaomiSolrPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.mapping = settings['SOLR_MAPPING'].items()
        self.ignore = settings['SOLR_IGNORE_DUPLICATES'] or False
        self.keys = settings['SOLR_DUPLICATES_KEY_FIELDS']
        if self.ignore and not self.keys:
            raise RuntimeError('SOLR_DUPLICATES_KEY_FIELDS has to be defined')
        self.solr = pysolr.Solr(settings['SOLR_URL'], timeout=10)

        # self.solr.delete(q='*:*')

        # print settings['SOLR_MAPPING']

    def process_item(self, item, spider):
        if self.ignore:
            duplicates = [str(name) + ':' + '"' + self.get_value(item, value) + '"' for name, value in self.mapping if name in self.keys]
            query = " ".join(duplicates)
            result = self.solr.search(query)
            print query
            print result
            # result = None
            if result:
                # logging.info("Skip duplicates in Solr")
                # return item
                logging.info("Remove old values in Solr")
                self.solr.delete(q=query)
                # self.solr.delete(q='*:*')
                # print type(self.keys)
        results = {}
        for name, value in self.mapping:
            results[name] = self.get_value(item, value)

        # self.solr.delete()
        self.solr.add([results])
        # print self.solr.search(q=query)
        # print self.solr.add([{'bananas': '1'}])
        # print duplicates
        # print query
        # print results
        # flag = 'appid' in item
        # print flag
        # print type(item)
        return item

    def get_value(self, item, value):
        if type(value) is str:
            return item[value] if value in item else None
        elif type(value) is list:
            return [item[key] if key in item else None for key in value]
        else:
            raise TypeError('Only string and list are valid sources')

class XiaomiMongoDBPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.key = settings['MONGODB_UNIQUE_KEY']
        # self.collection.drop()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # duplicate = str(self.key) + ':' + '"' + item[self.key] + '"'
            # print duplicate
            result = {}
            result[self.key] = item[self.key]
            # print result
            search_result = self.collection.find_one(result)
            # print search_result
            if search_result:
            #    logging.info("Skip duplicates")
            #    return item
            # else:
            # if True:
                logging.info("Remove old values in MongoDB")
                self.collection.delete_one(result)

            self.collection.insert(dict(item))
            # logging.info("Item added to MongoDB database!")
            # log.msg("Item added to MongoDB database!",
            #        level=log.DEBUG, spider=spider)
            logging.debug("Item added to MongoDB database!")
            return item

    def __get_itemvalue__(self, item, value):
        if type(value) is str:
            return item[value] if value in item else None
        elif type(value) is list:
            return [item[key] if key in item else None for key in value]
        else:
            raise TypeError('Only string and list are valid sources')



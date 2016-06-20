
# -*- coding: utf-8 -*-

# Scrapy settings for xiaomiapp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaomi'
SPIDER_MODULES = ['healthy.spiders']
NEWSPIDER_MODULE = 'healthy.spiders'
DOWNLOAD_DELAY=1
ITEM_PIPELINES = {
    'healthy.pipelines.XiaomiMongoDBPipeline': 300,
}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "scrapy"
MONGODB_COLLECTION = "xiaomiapp"
MONGODB_UNIQUE_KEY = "appid"
LOG_FILE = 'scrapy.log'

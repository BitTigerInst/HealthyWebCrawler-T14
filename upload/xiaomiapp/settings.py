# -*- coding: utf-8 -*-

# Scrapy settings for xiaomiapp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaomiapp'

SPIDER_MODULES = ['xiaomiapp.spiders']
NEWSPIDER_MODULE = 'xiaomiapp.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'xiaomiapp (+http://www.yourdomain.com)'
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiaomiapp.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xiaomiapp.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xiaomiapp.pipelines.XiaomiMongoDBPipeline': 300,
    'xiaomiapp.pipelines.XiaomiSolrPipeline': 200,
    'xiaomiapp.pipelines.XiaomiElasticSearchPipeline': 100,
}

# MONGODB settings
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
# MONGODB_DB = "xiaomiapp"
# MONGODB_COLLECTION = "applists"
MONGODB_DB = "scrapy"
MONGODB_COLLECTION = "xiaomiapp"
MONGODB_UNIQUE_KEY = "appid"

# ELASTICSEARCH settings
# ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_SERVER = 'localhost'
ELASTICSEARCH_PORT = 9200
# ELASTICSEARCH_USERNAME = ''
# ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'scrapy'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'
ELASTICSEARCH_TYPE = 'items'
# ELASTICSEARCH_BUFFER_LENGTH = 500
# ELASTICSEARCH_UNIQ_KEY = 'appid' # Custom uniqe key

# SOLR settings
# SOLR_URL = 'http://localhost:8983/solr/scrapy'
SOLR_URL = 'http://localhost:8983/solr/sample'
# SOLR_MAPPING = {
#   'appurl': 'appurl',
#   'title': 'title',
#   'appid': 'appid',
#   'category': 'category',
#   'groupid': 'groupid',
#   'developer': 'developer',
#   'rating': 'rating',
#   'count': 'count',
#   'version': 'version',
#   'update_time': 'update_time',
#   'developer_recommended': 'developer_recommended',
#   'related_recommended': 'related_recommended'
# }
SOLR_MAPPING = {
  'appurl': 'appurl',
  'title': 'title',
  'appid': 'appid',
  'category': 'category',
  'cateid': 'cateid',
  'developer': 'developer',
  'rating': 'rating',
  'ratingct': 'ratingct',
  'version': 'version',
  'updatetm': 'updatetm',
  'developerrec': 'developerrec',
  'relatedrec': 'relatedrec'
}
SOLR_IGNORE_DUPLICATES = True
SOLR_DUPLICATES_KEY_FIELDS = ['appid']

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_FILE = 'scrapy.log'
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import scrapy
from scrapy.spiders import Spider
from scrapy import Request
import re
from scrapy.selector import Selector
from healthy.items import HealthyItem

class HealthySpider(Spider):
    name = "xiaomi"
    allowed_domains = ["app.mi.com"]

    start_urls = [
        "http://app.mi.com/topList?page=1"
    ]

    def parse(self, response):
        #import pudb; pu.db
        page = Selector(response)

        page_nexts = page.xpath('//div[@class="pages"]/a')
        page_max = int(page_nexts[-2].xpath('text()').extract_first())

        for page_id in xrange(1, page_max + 1):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id))#{0} argument 0, {1} argument 1, advanced string formatting
            yield scrapy.Request(url, callback=self.parse_page)# scrapy.http.Request, callback: the function that will be called with the response of this request


    def parse_page(self, response):
        page = Selector(response)
        lis = page.xpath('//ul[@class="applist"]/li')
        if lis == None:
            return

        url_common = 'http://app.mi.com'

        for li in lis:
            item = HealthyItem()
            item['title'] = li.xpath('./h5/a/text()').extract_first()
            url = li.xpath('./h5/a/@href').extract_first()
            appid = re.match(r'/detail/(.*)', url).group(1) # r' indicates that the string is "raw string" --you want an unescapted string; group(1)http://www.tutorialspoint.com/python/python_reg_expressions.htm
            item['appid'] = appid
            # import pudb; pu.db
            req = scrapy.Request(url_common + url, callback=self.parse_details)
            req.meta["item"]=item
            yield req

    def parse_details(self, response):
            item = response.meta["item"]
            page = Selector(response)

            #extract relevent apps first

#           lis_d = page.xpath(u"//h3[text()='开发者应用']/following-sibling::div[@class='second-imgbox'][1]/ul/li")
#           lis_r = page.xpath(u"//h3[text()='相关应用']/following-sibling::div[@class='second-imgbox'][1]/ul/li")
            recommended_d = []
            recommended_r = []

#            for li in lis_r:
#                url = li.xpath('./a/@href').extract_first()
#                appid_r = re.match(r'/detail/(.*)', url).group(1) #relevant apps by function
#                recommended_r.append(appid_r)
                
#            for li in lis_d: 
#                url = li.xpath('./a/@href').extract_first()
#                appid_d = re.match(r'/detail/(.*)', url).group(1) #relevant apps by the same developer
#                recommended_r.append(appid_d) 
            app_name = page.xpath('//div[@class="bread-crumb"]/ul/li[position()=3]/text()').extract_first()
            developer = page.xpath('//div[@class="intro-titles"]/p/text()').extract_first()
            rating_url = page.xpath('//div[contains(@class, "star1-hover")]/@class').extract_first()
            rating = re.match(r'star1-hover star1-(.*)',rating_url).group(1)
            rating_count_url = page.xpath('//span[@class="app-intro-comment"]/text()').extract_first()
            rating_count = re.findall(r'\d+', rating_count_url)[0]
            version = page.xpath('//ul[@class=" cf"]/li[position()=4]/text()').extract_first()
            update_tm = page.xpath('//ul[@class=" cf"]/li[position()=6]/text()').extract_first()
            category_url = page.xpath('//a[contains(@href,"category")]/@href').extract_first()
            category = re.match(r'/category/(.*)', category_url).group(1)

            print "url:"+response.url
            print "app_name:"+app_name
            print "developer:"+developer
            print "version:"+version
            print "update date:"+update_tm
            print "category:"+category
            print "rating:"+rating
            print "rating_count:"+rating_count

            item['url'] = response.url
            item['app_name'] = app_name
            item['recommended_d'] = recommended_d
            item['recommended_r'] = recommended_r
            item['developer'] = developer
            item['rating'] = rating 
            item['rating_count'] = rating_count 
            item['version'] = version
            item['update_tm'] = update_tm
            item['category'] = category

            #import pudb; pu.db
            yield item


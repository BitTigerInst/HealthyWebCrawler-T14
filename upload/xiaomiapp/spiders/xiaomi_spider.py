#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy import Request
import re
from scrapy.selector import Selector
from xiaomiapp.items import XiaomiAppItem

# from scrapy.shell import inspect_response
# from scrapy.utils.response import open_in_browser

class XiaomiSpider(Spider):
    name = "xiaomi"
    allowed_domain = ["app.mi.com"]
    start_urls = [
        "http://app.mi.com/topList?page=1"
    ]


    def parse(self, response):
        page = Selector(response)
        page_list = page.xpath('//div[@class="pages"]/a')
        page_max = int(page_list[-2].xpath('text()').extract_first())

        for page_id in xrange(1, 2):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id))
            yield scrapy.Request(url, callback=self.parse_page)

        # print page_list[-2]
        # print type(page_list[-2].xpath('text()').extract_first())

        # inspect_response(response, self)
        # open_in_browser(response)

    def parse_page(self, response):
        page = Selector(response)
        page_list = page.xpath('//ul[@class="applist"]/li')

        if page_list == None:
            return

        url_base = 'http://app.mi.com'

        for l in page_list:
            item = XiaomiAppItem()
            item['title'] = l.xpath('./h5/a/text()').extract_first()#.encode('utf-8')
            url = l.xpath('./h5/a/@href').extract_first()
            appid = re.match(r'/detail/(\d+)', url).group(1)
            item['appid'] = appid

            item['category'] = l.xpath('./p/a/text()').extract_first()#.encode('utf-8')
            url_c = l.xpath('./p/a/@href').extract_first()
            groupid = re.match(r'/category/(.*)', url_c).group(1)
            # item['groupid'] = groupid
            item['cateid'] = groupid

            req = scrapy.Request(url_base + url, callback=self.parse_details)
            appurl = url_base + url
            item['appurl'] = appurl
            # print appurl
            req.meta["item"] = item
            yield req

            # print url
            # print appid
            # print groupid
            
    def parse_details(self, response):
        item = response.meta["item"]
        page = Selector(response)
        # page_list = page.xpath('//div[@class="second-imgbox"]/ul/li')

        page_list = page.xpath('//div[@class="second-imgbox"]')
        app_text = page.xpath('//div[@class="app-text"]/h3/text()').extract()
        # recommended_type = app_text[2].encode('utf-8')
        # print type(recommended_type)


        developer_recommended = []
        related_recommended = []
        # print page_list.__len__()

        if page_list.__len__() == 2:
            # pass
            page_list_1 = page_list[0].xpath('./ul/li')
            for l in page_list_1:
                url = l.xpath('./a/@href').extract_first()
                appid = re.match(r'/detail/(\d+)', url).group(1)
                developer_recommended.append(appid)
            page_list_2 = page_list[1].xpath('./ul/li')
            for l in page_list_2:
                url = l.xpath('./a/@href').extract_first()
                appid = re.match(r'/detail/(\d+)', url).group(1)
                related_recommended.append(appid)
        elif app_text.__len__() < 3: # recommended_type ==
            pass
        else:
            recommended_type = app_text[2].encode('utf-8')
            sd = '开发者应用'
            sd.decode('utf-8').encode('gb18030')
            sr = '相关应用'
            sr.decode('utf-8').encode('gb18030')
            page_list_1 = page_list[0].xpath('./ul/li')
            if recommended_type == sd:
                for l in page_list_1:
                    url = l.xpath('./a/@href').extract_first()
                    appid = re.match(r'/detail/(\d+)', url).group(1)
                    developer_recommended.append(appid)
            elif recommended_type == sr:
                for l in page_list_1:
                    url = l.xpath('./a/@href').extract_first()
                    appid = re.match(r'/detail/(\d+)', url).group(1)
                    related_recommended.append(appid)


        # recommended = []
        # for l in page_list:
            # url = l.xpath('./a/@href').extract_first()
            # appid = re.match(r'/detail/(\d+)', url).group(1)
            # recommended.append(appid)
            # print appid


        page_list = page.xpath('//div[@class="intro-titles"]')
        # for l in page_list:
        item['developer'] = page_list.xpath('./p/text()').extract_first()#.encode('utf-8')
            # print item['developer']

        rating_list = page.xpath('//div[@class="star1-empty"]')
        rating_link = rating_list[0].xpath('./div/@class').extract_first()
        item['rating'] = re.match(r'star1-hover star1-(\d+)', rating_link).group(1)
        # print item['rating']

        rating_count_link = page.xpath('//span[@class="app-intro-comment"]/text()').extract_first().encode('utf-8')
        # item['count'] = re.findall(r'\d+', rating_count_link)[0]
        item['ratingct'] = re.findall(r'\d+', rating_count_link)[0]
        # print type(item['rating'])
        # print rating_count_link
        # print item['count']

        page_list = page.xpath('//ul[@class=" cf"]')
        version_list = page_list.xpath('./li/text()').extract()
        item['version'] = version_list[3]
        # item['update_time'] = version_list[5]
        item['updatetm'] = version_list[5]
        # print item['version']
        # print item['update_time']

        # item['developerrec'] = developer_recommended
        # item['relatedrec'] = related_recommended
        item['developerrec'] = " ".join(developer_recommended)
        item['relatedrec'] = " ".join(related_recommended)

        print type(item['developerrec'])

        # item["recommended"] = recommended
        # item['developer_recommended'] = developer_recommended
        # item['related_recommended'] = related_recommended
        # print item['developer_recommended']
        # print item['related_recommended']
        # print item['title']

        yield item

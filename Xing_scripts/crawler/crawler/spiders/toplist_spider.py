# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import Spider
from scrapy import Request
from bs4 import BeautifulSoup
from crawler.items import CrawlerItem

class TopListSpider(scrapy.Spider):
    name = "toplist"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList?page=1"]


    def parse(self, response):
        for page_id in range(1,43):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id)) 
            yield scrapy.Request(url, callback=self.parse_page)
        
            
    def parse_page(self, response):
        common_url = 'http://app.mi.com'
        item = CrawlerItem()

        html_doc = BeautifulSoup(response.body, "lxml")
        
        for link in html_doc.find_all('h5'):
            a_tag = link.a
            if not a_tag:
                continue

            app_name = re.match(r'.*', a_tag.string).group()
            url = a_tag["href"]
            app_id = (re.match(r'/detail/(\d+)', url)).group(1)
            current = html_doc.find("span", "current").string

            req = scrapy.Request(common_url + url, callback=self.parse_details)
            req.meta["item"] = item
            yield req


    def parse_details(self, response):
        item = response.meta["item"]
        common_url = 'http://app.mi.com/detail/'
        detail_doc = BeautifulSoup(response.body, "lxml")

        ret = detail_doc.find("div", "app-info")
        imgurl = ret.find("img")["src"]
        item['imgurl'] = imgurl
        
        # get name, developer, category, rating, number of scores
        ret = detail_doc.find("div", "intro-titles")
        p_tag_list = ret.find_all("p")
        div_tag_list = ret.find_all("div")
        app_name = ret.find("h3").contents[0]
        app_id = ret.find("a", "download")["href"]
        app_id = (re.search(r'/download/(\d+)', app_id)).group(1)
        app_developer = p_tag_list[0].string
        app_category = p_tag_list[1].contents[1]
        app_rating_count = (re.search(r'\d+', ret.find("span", "app-intro-comment").contents[0])).group()
        app_rating = div_tag_list[1]["class"][1]
        app_rating = re.match(r'star1-(\d+)', app_rating).group(1)
        
        item['title'] = app_name
        item['appid'] = app_id
        item['appurl'] = common_url + app_id
        item['category'] = app_category
        item['developer'] = app_developer
        item['ratingct'] = str(app_rating_count)
        item['rating'] = app_rating

        #  get categoryid
        ret = detail_doc.find("div", "bread-crumb")
        categoryid = ret.find_all("a")
        categoryid = categoryid[1]["href"]
        categoryid = (re.search(r'/category/(\d+)', categoryid)).group(1)
        item['cateid'] = categoryid

        #  get version and update time
        ret = detail_doc.find("ul", " cf")
        li_tag_list = ret.find_all("li")
        app_version = li_tag_list[3].contents[0]
        app_update_time = li_tag_list[5].contents[0]
        item['version'] = str(app_version)
        item['updatetm'] = str(app_update_time)

        #get recommend app and developers application
        ret = detail_doc.find_all("div", "second-imgbox")

        recommended_app = []
        recommended_dev_app = []
            
        if len(ret) == 2:
            for i in xrange(len(ret)):
                li_list = ret[i].find_all("li")
                for j in li_list:
                    link = j.find("a")["href"]
                    app_id = (re.match(r'/detail/(\d+)', link)).group(1)

                    if i == 0:           
                        recommended_app.append(app_id)
                    else:
                        recommended_dev_app.append(app_id)

        elif len(ret) == 1:
                li_list = ret[0].find_all("li")
                for j in li_list:
                    link = j.find("a")["href"]
                    app_id = (re.match(r'/detail/(\d+)', link)).group(1)

                    if len(ret[0].previous_sibling.string) == 5:
                        recommended_dev_app.append(app_id)
                    else:
                        recommended_app.append(app_id)

        item['developerrec'] = recommended_dev_app
        item['relatedrec'] = recommended_app
        
        print imgurl, app_name, app_id, app_developer, app_category, app_rating_count, app_rating, app_version, app_update_time, \
              recommended_app, recommended_dev_app, categoryid
        yield item  
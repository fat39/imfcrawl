# -*- coding: utf-8 -*-
import scrapy
from imfcrawl import items
from scrapy.http import Request
from scrapy.http import Response
from scrapy.settings import default_settings
import requests
import os
from imfcrawl.utils import commons


class TaiyingshiSpider(scrapy.Spider):
    name = 'taiyingshi'
    allowed_domains = ['taiyingshi.com',"127.0.0.1"]
    start_urls = ['http://www.taiyingshi.com/last/']
    # start_urls = ['http://www.taiyingshi.com/people/xj25.html']
    custom_settings = {
        "ITEM_PIPELINES":{
            # "imfcrawl.pipelines.Taiyingshi_toapi_Pipeline":333,
            "imfcrawl.pipelines.Taiyingshi_tofile_Pipeline":343,
        },
        "DOWNLOAD_DELAY": 0,
        "RANDOM_DELAY" : 3,
        'CONCURRENT_REQUESTS':100,
        'CONCURRENT_REQUESTS_PER_DOMAIN':100,
        'CONCURRENT_REQUESTS_PER_IP':100,
        "API_URL": "http://127.0.0.1:8000/taiyingshi/api/movie/",
        "DUMP_FILE_DIR":os.path.join(r"D:\临时\爬虫\scrapy\taiyingshi"),
        "DOWNLOADER_MIDDLEWARES":{
            # "imfcrawl.middlewares.ProxyMiddleware":543,
            'imfcrawl.middlewares.RandomDelayMiddleware':550
        },
    }
    next_page_flag = True  # 是否抓取下一页的flag，判断依据是只要该页遇到已经爬过的movie，则判断上一次是爬到这，就不用爬后面的
    # next_page_flag目的是为了以后继续爬但不想爬所有的页面

    def parse(self, response):
        movie_list = response.xpath("//div[@class='pic-extra']")
        # movie_list = response.xpath("//div[@class='works'][1]/div[@class='pic-extra']")  # people页面
        for movie in movie_list:
            movie_url = movie.xpath("./div[@class='pic']/a/@href").extract_first()
            request_obj =  Request(url=movie_url, method="GET", callback=self.movie_page_parse)
            yield request_obj
            # break

        if self.next_page_flag:  # 是否抓取下一页的flag，判断依据是只要该页遇到已经爬过的movie，则判断上一次是爬到这，就不用爬后面的
            next_page_url = response.xpath("//a[@class='down near']/@href").extract_first()
            yield Request(url=next_page_url,method="GET",callback=self.parse)


    def movie_page_parse(self,response):
        if self.check_exist(response.url):  # 本item如果已dump，则无需继续处理本item
            self.next_page_flag = False  # 本url已爬，无需爬后面的page了
        else:
            obj = items.Taiyingshi_movie_Item()
            # obj = dict()
            movie_name = response.xpath("//div[@id='title']/h1/text()").extract_first()
            movie_director_list = response.xpath("//div[@id='director']/em//a/text()").extract() or ""
            movie_actor_list = response.xpath("//div[@id='actor']/em//a/text()").extract() or []
            movie_type = response.xpath("//div[@id='genre']/em/text()").extract_first()
            movie_type_list = [] if not movie_type else movie_type.split()
            movie_district = response.xpath("//div[@id='area']/em/text()").extract_first() or ""
            movie_year = response.xpath("//div[@id='year']/em/text()").extract_first() or ""
            movie_language = response.xpath("//div[@id='language']/em/text()").extract_first()
            movie_language_list = [] if not movie_language else movie_language.split()
            movie_length = response.xpath("//div[@id='length']/em/text()").extract_first() or ""
            movie_rate_douban = response.xpath("//span[@id='douban']/parent::a/following-sibling::span/text()").extract_first() or ""
            movie_douban_link = response.xpath("//span[@id='douban']/parent::a/@href").extract_first() or ""
            movie_rate_imdb = response.xpath("//span[@id='imdb']/parent::a/following-sibling::span/text()").extract_first() or ""
            movie_imdb_link = response.xpath("//span[@id='imdb']/parent::a/@href").extract_first() or ""
            movie_download_list = []
            movie_download_baidu_box = response.xpath("//div[@class='res']")[0]
            for item in movie_download_baidu_box.xpath(".//td[@class='link']"):
                link = item.xpath("./a/@href").extract_first()
                password = item.xpath("text()").extract()[-1].strip()
                movie_download_list.append("百度网盘 {} {}".format(link,password))

            movie_download_others_box = response.xpath("//div[@class='res']")[1]
            for item in movie_download_others_box.xpath(".//li[not(@class='fres')]"):
                movie_download_list.append("\n")
                item_title = item.xpath(".//span[@class='type-show']/text()").extract_first()
                item_link = item.xpath(".//td[@class='link']/a/@href").extract_first()
                xunlei_link = item.xpath(".//td[@class='btn xl-down']/a/@href").extract_first()
                xiaomi_link = item.xpath(".//td[@class='btn miwifi-down']/a/@href").extract_first()
                movie_download_list.append("{} {}".format(item_title,item_link))
                movie_download_list.append("迅雷 {}".format(xunlei_link))
                movie_download_list.append("小米 {}".format(xiaomi_link))

            obj["movie_name"] = movie_name
            obj["movie_url"] = response.url
            obj["movie_director_list"] = movie_director_list
            obj["movie_actor_list"] = movie_actor_list
            obj["movie_type_list"] = movie_type_list
            obj["movie_district"] = movie_district
            obj["movie_year"] = movie_year
            obj["movie_language_list"] = movie_language_list
            obj["movie_length"] = movie_length
            obj["movie_rate_douban"] = movie_rate_douban
            obj["movie_douban_link"] = movie_douban_link
            obj["movie_rate_imdb"] = movie_rate_imdb
            obj["movie_imdb_link"] = movie_imdb_link
            obj["movie_download_list"] = movie_download_list

            yield obj
            

        recommend_movie_url_list = response.xpath("//div[@id='recommends']/div[@class='b-content']//a/@href").extract()
        for recommend_movie_url in recommend_movie_url_list:
            if not self.check_exist(recommend_movie_url):
                request_obj = Request(url=recommend_movie_url,method="GET",callback=self.movie_page_parse)
                yield request_obj


    @property
    def has_post_set(self):
        if not hasattr(self, "_has_post_set"):
            api_url = self.settings.get("API_URL")
            try:
                self._has_post_set = eval(requests.get(api_url).text)
            except:
                self._has_post_set = set()
        return self._has_post_set


    def check_exist(self,url):
        url_hash = commons.hash_sha1(url)
        file_path = os.path.join(self.settings.get("DUMP_FILE_DIR"),url_hash)
        if os.path.exists(file_path):
            return True
        return False


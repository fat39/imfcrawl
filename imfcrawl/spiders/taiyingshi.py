# -*- coding: utf-8 -*-
import scrapy
from imfcrawl import items
from scrapy.http import Request

class TaiyingshiSpider(scrapy.Spider):
    name = 'taiyingshi'
    allowed_domains = ['taiyingshi.com']
    start_urls = ['http://www.taiyingshi.com/last/']
    custom_settings = {
        "ITEM_PIPELINES":{
            "imfcrawl.pipelines.Taiyingshi_toapi_Pipeline":333,
        },
        "DOWNLOAD_DELAY": 3,
        "API_URL": "http://127.0.0.1:8000/taiyingshi/api/taiyingshi/",
    }


    def parse(self, response):
        movie_list = response.xpath("//div[@class='pic-extra']")
        n = 1
        for movie in movie_list:
            # obj = items.TaiyingshiItem()
            # movie_name = movie.xpath("./div[@class='extra']/a/text()").extract_first()
            # movie_rating = movie.xpath("./div[@class='pic']/a/div[@class='rating']/text()").extract_first()
            movie_index_url = movie.xpath("./div[@class='pic']/a/@href").extract_first()
            # obj['name'] = movie_name
            # obj['rate'] = movie_rating
            # obj['index_url'] = movie_index_url
            # print(movie_name,movie_rating,movie_index_url)
            # yield obj
            if n == 5:
                yield Request(url=movie_index_url,method="GET",callback=self.movie_page_parse)
                break
            n += 1

        # next_page_url = response.xpath("//a[@class='down near']/@href").extract_first()
        # yield Request(url=next_page_url,method="GET",callback=self.parse)

    def movie_page_parse(self,response):
        obj = items.Taiyingshi_movie_Item()
        movie_name = response.xpath("//div[@id='title']/h1/text()").extract_first()
        movie_director_list = response.xpath("//div[@id='director']/em//a/text()").extract() or []
        movie_actor_list = response.xpath("//div[@id='actor']/em//a/text()").extract() or []
        movie_type = response.xpath("//div[@id='genre']/em/text()").extract_first()
        movie_type_list = [] if not movie_type else movie_type.split()
        movie_district = response.xpath("//div[@id='area']/em/text()").extract_first() or None
        movie_year = response.xpath("//div[@id='year']/em/text()").extract_first() or None
        movie_language = response.xpath("//div[@id='language']/em/text()").extract_first()
        movie_language_list = [] if not movie_language else movie_language.split()
        movie_length = response.xpath("//div[@id='length']/em/text()").extract_first() or None
        movie_rate_douban = response.xpath("//span[@id='douban']/parent::a/following-sibling::span/text()").extract_first() or None
        movie_douban_link = response.xpath("//span[@id='douban']/parent::a/@href").extract_first() or None
        movie_rate_imdb = response.xpath("//span[@id='imdb']/parent::a/following-sibling::span/text()").extract_first() or None
        movie_imdb_link = response.xpath("//span[@id='imdb']/parent::a/@href").extract_first() or None
        movie_download_list = []
        movie_download_baidu_box = response.xpath("//div[@class='res']")[0]
        for item in movie_download_baidu_box.xpath(".//td[@class='link']"):
            link = item.xpath("./a/@href").extract_first()
            password = item.xpath("text()").extract()[-1].strip()
            movie_download_list.append("百度网盘 {} {}".format(link,password))

        movie_download_others_box = response.xpath("//div[@class='res']")[1]
        for item in movie_download_others_box.xpath(".//li"):
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

        # recommend_movie_url_list = response.xpath("//div[@id='recommends']/div[@class='b-content']//a/@href").extract()
        # for recommend_movie_url in recommend_movie_url_list:
        #     yield Request(url=recommend_movie_url,method="GET",callback=self.movie_page_parse)
        #     break



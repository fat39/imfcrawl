# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImfcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Taiyingshi_movie_Item(scrapy.Item):
    movie_name = scrapy.Field()
    mivie_url = scrapy.Field()
    movie_director_list = scrapy.Field()
    movie_actor_list = scrapy.Field()
    movie_type_list = scrapy.Field()
    movie_district = scrapy.Field()
    movie_year = scrapy.Field()
    movie_language_list = scrapy.Field()
    movie_length = scrapy.Field()
    movie_rate_douban = scrapy.Field()
    movie_douban_link = scrapy.Field()
    movie_rate_imdb = scrapy.Field()
    movie_imdb_link = scrapy.Field()
    movie_download_list = scrapy.Field()



# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class ImfcrawlPipeline(object):
    def process_item(self, item, spider):
        return item


class Taiyingshi_toapi_Pipeline():
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    def process_item(self, item, spider):
        movie_name = item["movie_name"]
        # requests.post(url=self.api_url, data={"name": name, "rate": rate, "index_url": index_url})
        requests.post(url=self.api_url, data=dict(item.items()))
        return item

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        api_url = crawler.settings.get("API_URL")
        return cls(api_url=api_url)
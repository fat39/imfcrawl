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
    # 貌似太慢了，如果想要速度的话，可以下dump到file，再放到数据库
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    def process_item(self, item, spider):
        if item["movie_url"] not in spider.has_post_set:
            print(dict(item.items()))
            requests.post(url=self.api_url, data=dict(item.items()))
        else:
            print(item["movie_name"])
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

import hashlib
import json
import os
from imfcrawl.utils import commons
class Taiyingshi_tofile_Pipeline():
    def __init__(self,crawler):
        self.dump_file_dir = crawler.spider.settings.get("DUMP_FILE_DIR")

    def process_item(self, item, spider):
        file_name = commons.hash_sha1(item["movie_url"])
        # file_name = hashlib.sha1(bytes(item["movie_url"],encoding="utf-8")).hexdigest()
        file_path = os.path.join(self.dump_file_dir,file_name)
        print(file_path)
        if not os.path.isfile(file_path):
            with open(file_path,"w") as f:
                f.write(json.dumps(dict(item.items())))
        return item

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """

        return cls(crawler=crawler)



# -*- coding:utf-8 -*-

from scrapy.cmdline import execute

import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "jiandan"])
# execute(["scrapy", "crawl", "jiandan","--nolog"])
# execute(["scrapy", "crawl", "cl_txt","--nolog"])
# execute(["scrapy", "crawl", "taiyingshi","--nolog"])
execute(["scrapy", "crawl", "taiyingshi"])
# # -*- coding:utf-8 -*-
# #
# movie_name ['摘金奇缘']
# movie_url
# movie_district ['美国']
# movie_year ['2018']
# movie_length ['121分钟']
#
#
# movie_rate_douban ['6.8']
# movie_douban_link ['http://movie.douban.com/subject/26786642']
# movie_rate_imdb ['7.5']
# movie_imdb_link ['http://www.imdb.com/title/tt3104988']
# movie_download_list ['百度网盘 https://pan.baidu.com/s/1GNNcHoMBlvzTkDDg4O8Weg mk3y', '\n', '磁力 magnet:?xt=urn:btih:9df02ec43d8661676eb164de71f18279da91c2da&&dn=[钛影视taiyingshi.com]', '迅雷 thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjlkZjAyZWM0M2Q4NjYxNjc2ZWIxNjRkZTcxZjE4Mjc5ZGE5MWMyZGEmJmRuPVvpkpvlvbHop4Z0YWl5aW5nc2hpLmNvbV1aWg==', '小米 http://d.miwifi.com/d2r/?url=bWFnbmV0Oj94dD11cm46YnRpaDo5ZGYwMmVjNDNkODY2MTY3NmViMTY0ZGU3MWYxODI3OWRhOTFjMmRhJiZkbj1b6ZKb5b2x6KeGdGFpeWluZ3NoaS5jb21d', '\n', '电驴 ed2k://|file|[钛影视taiyingshi.com]摘金奇缘.Crazy.Rich.Asians.2018.中英字幕.WEBrip.AAC.1080p.x264-远鉴&弯弯字幕组.mp4|1779801322|434435befdaffc45613d8d65d7570b78|h=n6mkopjcmz2alc6a32v7heafholie4xv|/', '迅雷 thunder://QUFlZDJrOi8vfGZpbGV8W+mSm+W9seinhnRhaXlpbmdzaGkuY29tXeaRmOmHkeWlh+e8mC5DcmF6eS5SaWNoLkFzaWFucy4yMDE4LuS4reiLseWtl+W5lS5XRUJyaXAuQUFDLjEwODBwLngyNjQt6L+c6Ym0JuW8r+W8r+Wtl+W5lee7hC5tcDR8MTc3OTgwMTMyMnw0MzQ0MzViZWZkYWZmYzQ1NjEzZDhkNjVkNzU3MGI3OHxoPW42bWtvcGpjbXoyYWxjNmEzMnY3aGVhZmhvbGllNHh2fC9aWg==', '小米 http://d.miwifi.com/d2r/?url=ZWQyazovL3xmaWxlfFvpkpvlvbHop4Z0YWl5aW5nc2hpLmNvbV3mkZjph5HlpYfnvJguQ3JhenkuUmljaC5Bc2lhbnMuMjAxOC7kuK3oi7HlrZfluZUuV0VCcmlwLkFBQy4xMDgwcC54MjY0Lei/nOmJtCblvK/lvK/lrZfluZXnu4QubXA0fDE3Nzk4MDEzMjJ8NDM0NDM1YmVmZGFmZmM0NTYxM2Q4ZDY1ZDc1NzBiNzh8aD1uNm1rb3BqY216MmFsYzZhMzJ2N2hlYWZob2xpZTR4dnwv', '\n', 'HTTP http://vip.zuiku8.com/1811/摘金奇缘.BD1280高清中英双字版.mp4', '迅雷 thunder://QUFodHRwOi8vdmlwLnp1aWt1OC5jb20vMTgxMS/mkZjph5HlpYfnvJguQkQxMjgw6auY5riF5Lit6Iux5Y+M5a2X54mILm1wNFpa', '小米 http://d.miwifi.com/d2r/?url=aHR0cDovL3ZpcC56dWlrdTguY29tLzE4MTEv5pGY6YeR5aWH57yYLkJEMTI4MOmrmOa4heS4reiLseWPjOWtl+eJiC5tcDQ=']
#
#
#
# movie_type_list ['喜剧', '爱情']
# movie_language_list ['英语', '汉语普通话', '粤语']
# movie_director_list ['朱浩伟']
# movie_actor_list ['康斯坦斯·吴', '亨利·戈尔丁', '杨紫琼', '嘉玛·陈', '卢燕', '奥卡菲娜', '岑勇康', '郑肯', '水野索诺娅', '吴育刚', '欧阳万成', '钱信伊', '瑞米·海依', '尼科·桑托斯', '陆思敬', '苏慧敏', '方展发', '谢宛谕', '维多利亚·洛克', '许优美', '郑花如', '许静雯', '陈琼华', '刘佳镁', '陈美廪', '丹尼尔·詹金斯', '彼得·卡罗尔', '查尔斯·格朗斯', '陈胤希', '姬丝·阿奎诺', '木下众平', '吉娜·格莱尼斯', '凯文·关']
# #
# #
# import requests
# url = "http://127.0.0.1:8000/taiyingshi/api/movie/"
# # data = {'movie_name': '摘金奇缘', 'movie_url': 'http://www.taiyingshi.com/movie/zj137108.html', 'movie_director_list': ['朱浩伟'], 'movie_actor_list': ['康斯坦斯·吴', '亨利·戈尔丁', '杨紫琼', '嘉玛·陈', '卢燕', '奥卡菲娜', '岑勇康', '郑肯', '水野索诺娅', '吴育刚', '欧阳万成', '钱信伊', '瑞米·海依', '尼科·桑托斯', '陆思敬', '苏慧敏', '方展发', '谢宛谕', '维多利亚·洛克', '许优美', '郑花如', '许静雯', '陈琼华', '刘佳镁', '陈美廪', '丹尼尔·詹金斯', '彼得·卡罗尔', '查尔斯·格朗斯', '陈胤希', '姬丝·阿奎诺', '木下众平', '吉娜·格莱尼斯', '凯文·关'], 'movie_type_list': ['喜剧', '爱情'], 'movie_district': '美国', 'movie_year': '2018', 'movie_language_list': ['英语', '汉语普通话', '粤语'], 'movie_length': '121分钟', 'movie_rate_douban': '6.8', 'movie_douban_link': 'http://movie.douban.com/subject/26786642', 'movie_rate_imdb': '7.5', 'movie_imdb_link': 'http://www.imdb.com/title/tt3104988', 'movie_download_list': ['百度网盘 https://pan.baidu.com/s/1GNNcHoMBlvzTkDDg4O8Weg mk3y', '\n', '磁力 magnet:?xt=urn:btih:9df02ec43d8661676eb164de71f18279da91c2da&&dn=[钛影视taiyingshi.com]', '迅雷 thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjlkZjAyZWM0M2Q4NjYxNjc2ZWIxNjRkZTcxZjE4Mjc5ZGE5MWMyZGEmJmRuPVvpkpvlvbHop4Z0YWl5aW5nc2hpLmNvbV1aWg==', '小米 http://d.miwifi.com/d2r/?url=bWFnbmV0Oj94dD11cm46YnRpaDo5ZGYwMmVjNDNkODY2MTY3NmViMTY0ZGU3MWYxODI3OWRhOTFjMmRhJiZkbj1b6ZKb5b2x6KeGdGFpeWluZ3NoaS5jb21d', '\n', '电驴 ed2k://|file|[钛影视taiyingshi.com]摘金奇缘.Crazy.Rich.Asians.2018.中英字幕.WEBrip.AAC.1080p.x264-远鉴&弯弯字幕组.mp4|1779801322|434435befdaffc45613d8d65d7570b78|h=n6mkopjcmz2alc6a32v7heafholie4xv|/', '迅雷 thunder://QUFlZDJrOi8vfGZpbGV8W+mSm+W9seinhnRhaXlpbmdzaGkuY29tXeaRmOmHkeWlh+e8mC5DcmF6eS5SaWNoLkFzaWFucy4yMDE4LuS4reiLseWtl+W5lS5XRUJyaXAuQUFDLjEwODBwLngyNjQt6L+c6Ym0JuW8r+W8r+Wtl+W5lee7hC5tcDR8MTc3OTgwMTMyMnw0MzQ0MzViZWZkYWZmYzQ1NjEzZDhkNjVkNzU3MGI3OHxoPW42bWtvcGpjbXoyYWxjNmEzMnY3aGVhZmhvbGllNHh2fC9aWg==', '小米 http://d.miwifi.com/d2r/?url=ZWQyazovL3xmaWxlfFvpkpvlvbHop4Z0YWl5aW5nc2hpLmNvbV3mkZjph5HlpYfnvJguQ3JhenkuUmljaC5Bc2lhbnMuMjAxOC7kuK3oi7HlrZfluZUuV0VCcmlwLkFBQy4xMDgwcC54MjY0Lei/nOmJtCblvK/lvK/lrZfluZXnu4QubXA0fDE3Nzk4MDEzMjJ8NDM0NDM1YmVmZGFmZmM0NTYxM2Q4ZDY1ZDc1NzBiNzh8aD1uNm1rb3BqY216MmFsYzZhMzJ2N2hlYWZob2xpZTR4dnwv', '\n', 'HTTP http://vip.zuiku8.com/1811/摘金奇缘.BD1280高清中英双字版.mp4', '迅雷 thunder://QUFodHRwOi8vdmlwLnp1aWt1OC5jb20vMTgxMS/mkZjph5HlpYfnvJguQkQxMjgw6auY5riF5Lit6Iux5Y+M5a2X54mILm1wNFpa', '小米 http://d.miwifi.com/d2r/?url=aHR0cDovL3ZpcC56dWlrdTguY29tLzE4MTEv5pGY6YeR5aWH57yYLkJEMTI4MOmrmOa4heS4reiLseWPjOWtl+eJiC5tcDQ=']}
# data ={'movie_name': '重金属囧途', 'movie_url': 'http://www.taiyingshi.com/movie/zj159481.html', 'movie_director_list': ['Juuso Laatio', 'Jukka Vidgren'], 'movie_actor_list': ['Torstein Bjørklund', 'Johannes Holopainen', 'Rune Temte', 'Antti Heikkinen', 'Ville Hilska', 'Samuli Jaskio', 'Minka Kuustonen', 'Kai Lehtinen', 'Pirjo Lonka', 'Sinikka Mokkila', 'Anssi Niemi', 'Chike Ohanwe', '麦克斯·奥瓦斯卡', 'Pertti Sveholm', 'Martti Syrjä', 'Ville Tiihonen', 'Helén Vikstvedt'], 'movie_type_list': ['喜剧', '音乐'], 'movie_district': '芬兰', 'movie_year': '2018', 'movie_language_list': ['芬兰语', '英语', '挪威语'], 'movie_length': '92分钟', 'movie_rate_douban': '8.1', 'movie_douban_link': 'http://movie.douban.com/subject/27596249', 'movie_rate_imdb': '7.1', 'movie_imdb_link': 'http://www.imdb.com/title/tt7220754', 'movie_download_list': ['百度网盘 https://pan.baidu.com/s/1gayDSl_u3wbHjpB2PTB9_A sr4j']}
#
# requests.post(url,data=data)
# import re
# def duration(t):
#     h = re.findall("(\d+)小时",t)
#     h = 0 if not h else h[0]
#     M = re.findall("(\d+)分钟",t)
#     M = 0 if not M else M[0]
#     print(int(h) * 60 + int(M))
#     return int(h) * 60 + int(M)
# #
# duration("abc")
# {'movie_name': '每天回家都会看到老婆在装死', 'movie_url': 'http://www.taiyingshi.com/movie/mt152770.html', 'movie_director_list': ['李斗士男'], 'movie_actor_list': ['荣仓奈奈', '安田显', '小出惠介', '野々すみ花'], 'movie_type_list': ['喜剧'], 'movie_district': '日本', 'movie_year': '2018', 'movie_language_list': ['日语'], 'movie_length': None, 'movie_rate_douban': '6.6', 'movie_douban_link': 'http://movie.douban.com/subject/27054613', 'movie_rate_imdb': '6.8', 'movie_imdb_link': 'http://www.imdb.com/title/tt6939372', 'movie_download_list': ['百度网盘 https://pan.baidu.com/s/1Ddspf8A3vHTh_opinAOZzw f8qw', '\n', '磁力 magnet:?xt=urn:btih:29211634a147c748ef0ae8d9aeb8b997&dn=[钛影视taiyingshi.com]', '迅雷 thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjI5MjExNjM0YTE0N2M3NDhlZjBhZThkOWFlYjhiOTk3JmRuPVvpkpvlvbHop4Z0YWl5aW5nc2hpLmNvbV1aWg==', '小米 http://d.miwifi.com/d2r/?url=bWFnbmV0Oj94dD11cm46YnRpaDoyOTIxMTYzNGExNDdjNzQ4ZWYwYWU4ZDlhZWI4Yjk5NyZkbj1b6ZKb5b2x6KeGdGFpeWluZ3NoaS5jb21d']}

# import os
# import json
# dir = r"D:\临时\爬虫\scrapy\taiyingshi"
# dir_walk = os.walk(dir)
#
# file_name_list = next(dir_walk)[2]
# for file_name in next(dir_walk)[2]:
#     file_path = os.path.join(dir,file_name)
#     res = json.load(open(file_path))
#     print(type(res),res)




url = "http://www.taiyingshi.com/movie/xz151497.html"

import requests
from scrapy.selector import Selector

htm = requests.get(url)

from scrapy.settings import default_settings
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
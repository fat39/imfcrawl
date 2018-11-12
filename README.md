# imfcrawl
scrapy爬取一些东西

爬取taiyingshi网的电影列表

参数说明：
    allowed_domains = ['taiyingshi.com',"127.0.0.1"]  # 127.0.0.1是db的api地址，该api是用django写的
    start_urls = ['http://www.taiyingshi.com/last/']
    # start_urls = ['http://www.taiyingshi.com/people/xj25.html']
    custom_settings = {
        "ITEM_PIPELINES":{
            # "imfcrawl.pipelines.Taiyingshi_toapi_Pipeline":333,
            "imfcrawl.pipelines.Taiyingshi_tofile_Pipeline":343,
        },
        "DOWNLOAD_DELAY": 0,
        "RANDOM_DELAY" : 3,  # RandomDelayMiddleware的参数，随机最大的delay
        'CONCURRENT_REQUESTS':100,
        'CONCURRENT_REQUESTS_PER_DOMAIN':100,
        'CONCURRENT_REQUESTS_PER_IP':100,
        "API_URL": "http://127.0.0.1:8000/taiyingshi/api/movie/",  # api地址
        "DUMP_FILE_DIR":os.path.join(r"D:\临时\爬虫\scrapy\taiyingshi"),  # 本地的文件夹，存放movie的file，一个movie一个file
        "DOWNLOADER_MIDDLEWARES":{
            # "imfcrawl.middlewares.ProxyMiddleware":543,  # 代理
            'imfcrawl.middlewares.RandomDelayMiddleware':550  # 随机delay，该delay只针对api地址的post request，不过没多大用，貌似这些request会占用后台的队列。而且，api链接还是过多（不知道是不是db读取过频繁）
        },
    }

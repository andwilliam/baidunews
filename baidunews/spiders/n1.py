import scrapy
from baidunews.items import BaidunewsItem


class N1Spider(scrapy.Spider):
    name = "n1"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass

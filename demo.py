import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        pass

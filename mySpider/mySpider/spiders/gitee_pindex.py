import scrapy

from mySpider.items import GiteePIndex


class GiteePindexSpider(scrapy.Spider):

    name = "gitee-pindex"
    allowed_domains = "https://gitee.com"
    start_urls = ["https://gitee.com/explore/all?lang=cpp"]

    def parse(self, response):
        elements = response.xpath('//div[@class="ui relaxed divided items explore-repo__list"]//div[@class="item"]')
        for element in elements:
            link = self.allowed_domains + element.xpath('.//h3/a/@href').get()
            item = GiteePIndex()
            item['link'] = link
            yield item
        # 检查有没有下一页
        next_href__get = response.xpath(
            '//div[@class="ui tiny pagination menu"]//a[@class="icon item" and @rel="next"]/@href'
        ).get()
        if next_href__get is not None:
            yield scrapy.Request("https://gitee.com" + next_href__get, callback=self.parse, dont_filter=True)

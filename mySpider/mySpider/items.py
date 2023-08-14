# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class GiteePIndex(scrapy.Item):
    link = scrapy.Field()


class GiteePInfo(scrapy.Item):
    _extra = scrapy.Field()
    summary = scrapy.Field()
    license = scrapy.Field()
    package_manager = scrapy.Field()
    project_url = scrapy.Field()
    _source = scrapy.Field()
    language = scrapy.Field()
    name = scrapy.Field()
    releases = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NormalSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BankCrawlResultItem(scrapy.Item):
    crawl_time = scrapy.Field()
    bank_name = scrapy.Field()
    source_url = scrapy.Field()
    response = scrapy.Field()

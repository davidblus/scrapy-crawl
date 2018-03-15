# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawAppsItem(scrapy.Item):
    # define the fields for your item here like:
    crawl_time = scrapy.Field()
    tag = scrapy.Field()
    source_url = scrapy.Field()
    sha256 = scrapy.Field()
    detail = scrapy.Field()

class CrawlAppsDownloadItem(scrapy.Item):
    crawl_time = scrapy.Field()
    tag = scrapy.Field()
    source_url = scrapy.Field()
    sha256 = scrapy.Field()
    detail = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
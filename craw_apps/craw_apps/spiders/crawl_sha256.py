# -*- coding: utf-8 -*-

import datetime
import json
import scrapy

from craw_apps.items import CrawAppsItem

#KEY_LIST = ['trojan', 'sms-fraud', 'malware']
KEY_LIST = ['sms-fraud']

class CrawlSha256(scrapy.Spider):
    name = "crawl_sha256"
    allowed_domains = ["koodous.com"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'craw_apps.pipelines.CrawAppsPipeline': 300,
        },
    }
    base_url = 'https://api.koodous.com/apks?'
    
    
    def start_requests(self):
        for key in KEY_LIST:
            url = self.base_url + '&search=tag:' + key
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['item'] = {'tag': key}
            yield request

    def parse(self, response):
        api_result = json.loads(response.text)
        
        now = str(datetime.datetime.now())
        tag = response.meta['item']['tag']
        source_url = response.url
        
        for app_info in api_result['results']:
            item = CrawAppsItem()
            item['crawl_time'] = now
            item['tag'] = tag
            item['source_url'] = source_url
            item['sha256'] = app_info['sha256']
            item['detail'] = str(app_info)
            yield item
        
        url = api_result['next']
        request = scrapy.Request(url=url, callback=self.parse)
        request.meta['item'] = response.meta['item']
        yield request
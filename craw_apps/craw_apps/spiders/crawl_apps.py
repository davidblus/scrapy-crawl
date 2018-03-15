# -*- coding: utf-8 -*-

import datetime
import json
import random
import scrapy

import craw_apps.db as db
from craw_apps.items import CrawlAppsDownloadItem

LOG_TAG = 'davidblus:'
DEBUGING = False

#KEY_LIST = ['trojan', 'sms-fraud', 'malware']
KEY_LIST = ['sms-fraud']
AUTHORIZATION = ['2017ff69674805fa53d6c9905e5be28c4b786fd7', ]
DAY_NUMBER = 60 # 每日爬取数量

class CrawlApps(scrapy.Spider):
    name = "crawl_apps"
    allowed_domains = ["koodous.com"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy.pipelines.files.FilesPipeline': 1, 
            'craw_apps.pipelines.CrawAppsPipeline': 300, 
        }, 
        'FILES_STORE': 'downloads', 
    }
    base_url = 'https://api.koodous.com/apks/'
    
    def get_app_infos(self, tag):
        session = db.DBSession()
        app_infos = session.query(db.Koodous).filter_by(tag=tag).filter_by(done=False).all()
        session.close()
        if DEBUGING:
            return app_infos[:2]
        return app_infos[:DAY_NUMBER]
    
    def start_requests(self):
        for key in KEY_LIST:
            appinfos = self.get_app_infos(key)
            for appinfo in appinfos:
                sha256 = appinfo.sha256
                url = self.base_url + sha256 + '/download'
                authorization = random.choice(AUTHORIZATION)
                self.logger.info('%s authorization:%s', LOG_TAG, authorization)
                authorization = 'Token ' + authorization
                yield scrapy.Request(url=url, headers={'Authorization': authorization}, meta={'appinfo': appinfo.__dict__}, callback=self.parse)

    def parse(self, response):
        api_result = json.loads(response.text)
        self.logger.info('%s api_result:%s', LOG_TAG, api_result)
        download_url = api_result['download_url']
        appinfo = response.meta['appinfo']
        
        item = CrawlAppsDownloadItem()
        item['crawl_time'] = str(datetime.datetime.now())
        item['tag'] = appinfo['tag']
        item['source_url'] = appinfo['source_url']
        item['sha256'] = appinfo['sha256']
        item['detail'] = str(appinfo)
        item['file_urls'] = [download_url]
        yield item

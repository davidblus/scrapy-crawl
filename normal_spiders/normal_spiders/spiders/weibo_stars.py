# -*- coding: utf-8 -*-

# 使用示例：
# scrapy crawl weibo_stars --output=temp_result.json --logfile logs/spider/weibo_stars/{time}.log --loglevel DEBUG

import json

import scrapy

import db
from normal_spiders.items import WeiboStarsInfoItem

CONCURRENCE = 16


class WeiboStarsSpider(scrapy.Spider):
    custom_settings = {
        # "DOWNLOAD_DELAY": 1,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "normal_spiders.middlewares.RotateUserAgentMiddleware": 400,
            # "normal_spiders.middlewares.ProxyMiddleware": 500,
        },
        "ITEM_PIPELINES": {
            # "normal_spiders.pipelines.FundInfoCrawlPipeline": 300,
        },
        "DUPEFILTER_DEBUG": True,
        "CONCURRENT_ITEMS": CONCURRENCE,
        "CONCURRENT_REQUESTS": CONCURRENCE,
        "CONCURRENT_REQUESTS_PER_IP": CONCURRENCE,
        # "DEFAULT_REQUEST_HEADERS": {
        #     'Accept': '*/*',
        #     'Accept-Language': 'en',
        # },
    }

    name = 'weibo_stars'
    allowed_domains = ['weibo.cn']

    weibo_user_home_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={weibo_id}'
    weibo_user_mblog_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={weibo_id}' \
                           '&containerid={containerid}&page=1'

    def start_requests(self):
        session = db.DBSession()
        weibo_stars_info_list = session.query(db.WeiboStarsInfo).filter(db.WeiboStarsInfo.weibo_id != 0).all()
        # Todo: Testing
        for weibo_stars_info in weibo_stars_info_list[:200]:
        # for weibo_stars_info in weibo_stars_info_list:
            weibo_id = weibo_stars_info.weibo_id
            url = self.weibo_user_home_url.format(weibo_id=weibo_id)
            yield scrapy.Request(url=url, callback=self.parse_home)

        session.close()

    def parse_home(self, response):
        result_json = json.loads(response.text)
        weibo_id = result_json['data']['userInfo']['id']
        containerid = result_json['data']['tabsInfo']['tabs'][1]['containerid']
        url = self.weibo_user_mblog_url.format(weibo_id=weibo_id, containerid=containerid)
        yield scrapy.Request(url=url, callback=self.parse_mblog)

    def parse_mblog(self, response):
        result_json = json.loads(response.text)
        item = WeiboStarsInfoItem()
        item['result'] = json.dumps(result_json)
        yield item

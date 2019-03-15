# -*- coding: utf-8 -*-

# 使用示例：
# scrapy crawl abchina --logfile logs/spider/abchina/{time}.log --loglevel DEBUG

from datetime import datetime, timedelta, timezone
import json
import scrapy

from normal_spiders.items import BankCrawlResultItem

CONCURRENCE = 16


class AbchinaSpider(scrapy.Spider):
    custom_settings = {
        # "DOWNLOAD_DELAY": 1,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "normal_spiders.middlewares.RotateUserAgentMiddleware": 400,
            # "normal_spiders.middlewares.ProxyMiddleware": 500,
        },
        "ITEM_PIPELINES": {
            "normal_spiders.pipelines.BankCrawlResultPipeline": 300,
        },
        "DUPEFILTER_DEBUG": True,
        "CONCURRENT_ITEMS": CONCURRENCE,
        "CONCURRENT_REQUESTS": CONCURRENCE,
        "CONCURRENT_REQUESTS_PER_IP": CONCURRENCE,
        "DEFAULT_REQUEST_HEADERS": {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept': '*/*',
            'Accept-Language': 'en',
        },
    }

    name = 'abchina'
    allowed_domains = ['abchina.com']
    start_urls = ['http://ewealth.abchina.com/app/data/api/DataService/GoldInfoV2']

    def parse(self, response):
        result_json = json.loads(response.text)
        data_json = result_json["Data"]
        beijing_datetime_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))

        item = BankCrawlResultItem()
        item["crawl_time"] = beijing_datetime_now
        item["bank_name"] = "abchina"
        item["source_url"] = self.start_urls[0]
        item["response"] = json.dumps(data_json)
        yield item

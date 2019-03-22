# -*- coding: utf-8 -*-

# 使用示例：
# scrapy crawl cmfchina -a startTime=20010221 -a endTime=20190321 -a fundId=217011 --logfile logs/spider/cmfchina/{time}.log --loglevel DEBUG

from datetime import datetime

import scrapy

from normal_spiders.items import FundInfoItem

CONCURRENCE = 16


class CmfchinaSpider(scrapy.Spider):
    custom_settings = {
        # "DOWNLOAD_DELAY": 1,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "normal_spiders.middlewares.RotateUserAgentMiddleware": 400,
        },
        "ITEM_PIPELINES": {
            "normal_spiders.pipelines.FundInfoCrawlPipeline": 300,
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

    name = 'cmfchina'
    allowed_domains = ['cmfchina.com']
    start_url = 'http://www.cmfchina.com/servlet/fund/FundNavPageAction?' \
                'fundId={fundId}&startTime={startTime}&endTime={endTime}&numPerPage=7300'

    def __init__(self, startTime=None, endTime=None, fundId=None, *args, **kwargs):
        super(CmfchinaSpider, self).__init__(*args, **kwargs)
        self.startTime = startTime
        self.endTime = endTime
        self.fundId = fundId

    def start_requests(self):
        url = self.start_url.format(startTime=self.startTime, endTime=self.endTime, fundId=self.fundId)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tr_list = response.xpath('//tr')[1:]
        for tr in reversed(tr_list):
            time = datetime.strptime(tr.xpath('td/text()')[0].extract().strip(), '%Y-%m-%d').date()
            IOPV = tr.xpath('td/text()')[1].extract().strip()
            LJJZ = tr.xpath('td/text()')[2].extract().strip()

            item = FundInfoItem()
            item['fund_name'] = 'cmfchina'
            item['fund_code'] = self.fundId
            item['time'] = time
            item['IOPV'] = IOPV
            item['LJJZ'] = LJJZ
            yield item

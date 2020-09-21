#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 8:52 下午
# @Author  : daipengfei
# @Site    : davidblus.top/wordpress
# @File    : gyrx.py
# @Software: PyCharm
"""
工银瑞信债券基金抓取
"""

# 使用示例：
# scrapy crawl gyrx -a startTime=20200917 -a endTime=20200921 -a fundId=485111 --logfile logs/spider/gyrx/{time}.log --loglevel DEBUG

from datetime import datetime

import scrapy

from normal_spiders.items import FundInfoItem

CONCURRENCE = 16


class GyrxSpider(scrapy.Spider):
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

    name = 'gyrx'
    start_url = 'http://www.icbccs.com.cn/cif/MainCtrl'

    def __init__(self, startTime=None, endTime=None, fundId=None, *args, **kwargs):
        super(GyrxSpider, self).__init__(*args, **kwargs)
        self.startTime = startTime
        self.endTime = endTime
        self.fundId = fundId

    def start_requests(self):
        post_data = {
            'page': 'GetJJJZAJAX',
            'sel_fund': self.fundId,
            'f_date1': self.startTime,
            'f_date2': self.endTime
        }
        form_request = scrapy.FormRequest(url=self.start_url,
                                          formdata=post_data, callback=self.parse)
        yield form_request

    def parse(self, response):
        tr_list = response.xpath('//tr')[1:]
        for tr in reversed(tr_list):
            time = datetime.strptime(tr.xpath('td/text()')[1].extract().strip(), '%Y-%m-%d').date()
            IOPV = tr.xpath('td/text()')[2].extract().strip()
            LJJZ = tr.xpath('td/text()')[3].extract().strip()

            item = FundInfoItem()
            item['fund_name'] = 'gyrx'
            item['fund_code'] = self.fundId
            item['time'] = time
            item['IOPV'] = IOPV
            item['LJJZ'] = LJJZ
            yield item

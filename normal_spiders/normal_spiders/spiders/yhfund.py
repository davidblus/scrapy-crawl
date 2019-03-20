# -*- coding: utf-8 -*-

# 使用示例：
# scrapy crawl yhfund -a start_date=2013-09-13 -a end_date=2023-09-13 -a fund_code=000286 --logfile logs/spider/yhfund/{time}.log --loglevel DEBUG

from datetime import datetime

import scrapy

from normal_spiders.items import FundInfoItem

CONCURRENCE = 16


class YhfundSpider(scrapy.Spider):
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

    name = 'yhfund'
    allowed_domains = ['yhfund.com.cn']
    start_url = 'http://www.yhfund.com.cn/servlet/fund/FundAction?function=fundNetPage' \
                '&startdate={start_date}&enddate={end_date}&fundcode={fund_code}&numPerPage=3650'

    def __init__(self, start_date=None, end_date=None, fund_code=None, *args, **kwargs):
        super(YhfundSpider, self).__init__(*args, **kwargs)
        self.start_date = start_date
        self.end_date = end_date
        self.fund_code = fund_code

    def start_requests(self):
        url = self.start_url.format(start_date=self.start_date, end_date=self.end_date, fund_code=self.fund_code)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tr_list = response.xpath('//tr')[1:]
        for tr in reversed(tr_list):
            time = datetime.strptime(tr.xpath('td/text()')[0].extract(), '%Y-%m-%d').date()
            IOPV = tr.xpath('td/text()')[1].extract()
            LJJZ = tr.xpath('td/text()')[2].extract().strip()
            if LJJZ == '--':
                LJJZ = IOPV

            item = FundInfoItem()
            item['fund_name'] = 'yhfund'
            item['fund_code'] = self.fund_code
            item['time'] = time
            item['IOPV'] = IOPV
            item['LJJZ'] = LJJZ
            yield item

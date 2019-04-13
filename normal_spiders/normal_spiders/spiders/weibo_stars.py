# # -*- coding: utf-8 -*-
#
# # 使用示例：
# # scrapy crawl yhfund --logfile logs/spider/weibo_stars/{time}.log --loglevel DEBUG
#
# from datetime import datetime
#
# import scrapy
#
# from normal_spiders.items import FundInfoItem
#
# CONCURRENCE = 16
#
#
# class WeiboStarsSpider(scrapy.Spider):
#     custom_settings = {
#         # "DOWNLOAD_DELAY": 1,
#         "DOWNLOADER_MIDDLEWARES": {
#             "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
#             "normal_spiders.middlewares.RotateUserAgentMiddleware": 400,
#         },
#         "ITEM_PIPELINES": {
#             "normal_spiders.pipelines.FundInfoCrawlPipeline": 300,
#         },
#         "DUPEFILTER_DEBUG": True,
#         "CONCURRENT_ITEMS": CONCURRENCE,
#         "CONCURRENT_REQUESTS": CONCURRENCE,
#         "CONCURRENT_REQUESTS_PER_IP": CONCURRENCE,
#         # "DEFAULT_REQUEST_HEADERS": {
#         #     'Accept': '*/*',
#         #     'Accept-Language': 'en',
#         # },
#     }
#
#     name = 'weibo_stars'
#     allowed_domains = ['weibo.cn']
#
#     weibo_user_home_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={weibo_id}'
#     weibo_user_mblog_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={weibo_id}' \
#                            '&containerid={containerid}&page=1'
#
#     def start_requests(self):
#
#
#         url = self.start_url.format(start_date=self.start_date, end_date=self.end_date, fund_code=self.fund_code)
#         yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         tr_list = response.xpath('//tr')[1:]
#         for tr in reversed(tr_list):
#             time = datetime.strptime(tr.xpath('td/text()')[0].extract(), '%Y-%m-%d').date()
#             IOPV = tr.xpath('td/text()')[1].extract()
#             LJJZ = tr.xpath('td/text()')[2].extract().strip()
#             if LJJZ == '--':
#                 LJJZ = IOPV
#
#             item = FundInfoItem()
#             item['fund_name'] = 'yhfund'
#             item['fund_code'] = self.fund_code
#             item['time'] = time
#             item['IOPV'] = IOPV
#             item['LJJZ'] = LJJZ
#             yield item

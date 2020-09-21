#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 9:14 下午
# @Author  : daipengfei
# @Site    : davidblus.top/wordpress
# @File    : gyrx_crawl.py
# @Software: PyCharm
"""
工银瑞信债券基金定时抓取任务
"""

from datetime import datetime, timedelta, timezone

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.gyrx import GyrxSpider


@celery_app.task
def scrapy_crawl_gyrx():
    logger.info('scrapy_crawl_gyrx()')
    beijing_datetime_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    beijing_yesterday_str = (beijing_datetime_now.date() - timedelta(days=1)).strftime('%Y%m%d')
    kwargs = {
        'startTime': beijing_yesterday_str,
        'endTime': beijing_yesterday_str,
        'fundId': '485111',
    }
    run_spider(GyrxSpider, {}, kwargs)


if __name__ == '__main__':
    kwargs = {
        'startTime': '20200917',
        'endTime': '20200920',
        'fundId': '485111',
    }
    run_spider(GyrxSpider, {}, kwargs)

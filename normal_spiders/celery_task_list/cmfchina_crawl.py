# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.cmfchina import CmfchinaSpider


# 从银华基金网站上爬取数据
@celery_app.task
def scrapy_crawl_cmfchina():
    logger.info('scrapy_crawl_cmfchina()')
    date_str = str(datetime.now().date())
    settings = {
        'LOG_FILE': 'logs/spider/cmfchina/{date}.log'.format(date=date_str),
        'LOG_LEVEL': 'DEBUG',
    }
    beijing_datetime_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    beijing_yesterday_str = (beijing_datetime_now.date() - timedelta(days=1)).strftime('%Y%m%d')
    kwargs = {
        'startTime': beijing_yesterday_str,
        # 'startTime': '20010221',
        'endTime': beijing_yesterday_str,
        # 'endTime': '20190321',
        'fundId': '217011',
    }
    run_spider(CmfchinaSpider, settings, kwargs)

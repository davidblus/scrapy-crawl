# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.cmfchina import CmfchinaSpider


# 从招商基金网站上爬取数据
@celery_app.task
def scrapy_crawl_cmfchina():
    logger.info('scrapy_crawl_cmfchina()')
    beijing_datetime_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    beijing_yesterday_str = (beijing_datetime_now.date() - timedelta(days=1)).strftime('%Y%m%d')

    # 抓取招商安心收益
    kwargs = {
        'startTime': beijing_yesterday_str,
        'endTime': beijing_yesterday_str,
        'fundId': '217011',
    }
    run_spider(CmfchinaSpider, {}, kwargs)

    # 抓取招商双债增强LOF
    kwargs['fundId'] = '161716'
    run_spider(CmfchinaSpider, {}, kwargs)

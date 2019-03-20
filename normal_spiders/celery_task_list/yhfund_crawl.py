# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.yhfund import YhfundSpider


# 从银华基金网站上爬取数据
@celery_app.task
def scrapy_crawl_yhfund():
    logger.info('scrapy_crawl_yhfund()')
    date_str = str(datetime.now().date())
    settings = {
        'LOG_FILE': 'logs/spider/yhfund/{date}.log'.format(date=date_str),
        'LOG_LEVEL': 'DEBUG',
    }
    beijing_datetime_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    beijing_yesterday_str = (beijing_datetime_now.date() - timedelta(days=1)).strftime('%Y-%m-%d')
    kwargs = {
        'start_date': beijing_yesterday_str,
        'end_date': beijing_yesterday_str,
        'fund_code': '000286',
    }
    run_spider(YhfundSpider, settings, kwargs)

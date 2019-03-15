# -*- coding: utf-8 -*-

from datetime import datetime

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.abchina import AbchinaSpider


# 从中国农业银行网站上爬取数据
@celery_app.task
def scrapy_crawl_abchina():
    logger.info('scrapy_crawl_abchina()')
    date_str = str(datetime.now().date())
    settings = {
        'LOG_FILE': 'logs/spider/abchina/{date}.log'.format(date=date_str),
        'LOG_LEVEL': 'DEBUG',
    }
    run_spider(AbchinaSpider, settings)

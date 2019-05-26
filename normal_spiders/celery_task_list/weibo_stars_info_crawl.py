#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-14 00:11
# @Author  : daipengfei
# @Site    : davidblus.top/wordpress
# @File    : weibo_stars_info_crawl.py
# @Software: PyCharm
"""
微博爬取任务
"""
from datetime import datetime

from celery_config import celery_app, logger
from normal_spiders.celery_run_spider import run_spider
from normal_spiders.spiders.weibo_stars import WeiboStarsSpider


# 从微博爬取微博
@celery_app.task
def scrapy_crawl_weibo_stars_info():
    logger.info('scrapy_crawl_weibo_stars_info()')
    date_str = str(datetime.now().date())
    settings = {
        'LOG_FILE': 'logs/spider/weibo_stars/{date}.log'.format(date=date_str),
        'LOG_LEVEL': 'DEBUG',
    }
    run_spider(WeiboStarsSpider, settings, None)

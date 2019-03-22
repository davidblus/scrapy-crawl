# -*- coding: utf-8 -*-

# 测试环境启动与关闭
# celery -A celery_tasks worker -D -l info -f logs/celery/worker.log -B
# celery -A celery_tasks control shutdown

# 正式环境启动与关闭
# celery -A celery_tasks worker -D -l info -f logs/celery/worker.log
# celery -A celery_tasks beat --detach -l info -f logs/celery/beat.log
# kill {beat.PID}
# celery -A celery_tasks control shutdown

from celery.schedules import crontab
from datetime import timedelta

from celery_config import celery_app

celery_app.conf.beat_schedule = {
    # 'add-every-30-seconds1': {
    #     'task': 'celery_task_list.test.add',
    #     'schedule': timedelta(seconds=10),
    #     'args': (16, 16)
    # },
    'scrapy-crawl-abchina-crontab': {
        'task': 'celery_task_list.abchina_crawl.scrapy_crawl_abchina',
        'schedule': crontab(minute='3', hour='8-22', day_of_week='mon-fri'),
        # 'schedule': crontab(minute='10', hour='8-22', day_of_week='mon-fri'),
        'args': ()
    },
    'bank-response-to-info-crontab': {
        'task': 'celery_task_list.bank_response_to_info.bank_response_to_info',
        'schedule': crontab(minute='5', hour='8-22', day_of_week='mon-fri'),
        # 'schedule': crontab(minute='13', hour='8-22', day_of_week='mon-fri'),
        'args': ()
    },
    'scrapy-crawl-yhfund-crontab': {
        'task': 'celery_task_list.yhfund_crawl.scrapy_crawl_yhfund',
        'schedule': crontab(minute='1', hour='9', day_of_week='2-6'),
        # 'schedule': crontab(minute='11', hour='8-22', day_of_week='2-6'),
        'args': ()
    },
    'scrapy-crawl-cmfchina-crontab': {
        'task': 'celery_task_list.cmfchina_crawl.scrapy_crawl_cmfchina',
        'schedule': crontab(minute='10', hour='9', day_of_week='2-6'),
        # 'schedule': crontab(minute='44', hour='8-22', day_of_week='2-6'),
        'args': ()
    },
}

# from celery_task_list.test import add
from celery_task_list.abchina_crawl import scrapy_crawl_abchina
from celery_task_list.bank_response_to_info import bank_response_to_info
from celery_task_list.yhfund_crawl import scrapy_crawl_yhfund
from celery_task_list.cmfchina_crawl import scrapy_crawl_cmfchina

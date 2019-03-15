# -*- coding: utf-8 -*-

from celery_config import celery_app, logger


# 返回值会被 职程服务器 celery worker server 执行 print() 语句
@celery_app.task
def add(x, y):
    logger.info('add(%s, %s)', x, y)
    result = x + y
    return result

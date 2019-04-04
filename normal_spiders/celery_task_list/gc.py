# -*- coding: utf-8 -*-

from celery_config import celery_app, logger
import gc


# 垃圾回收
@celery_app.task
def collect():
    logger.info('collect()')
    unreachable_count = gc.collect()
    logger.info('gc.collect()=' + str(unreachable_count))

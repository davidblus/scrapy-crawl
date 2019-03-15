# -*- coding: utf-8 -*-

from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('celery_tasks_main', backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')
celery_app.conf.update(
    timezone='Asia/Shanghai',
)

logger = get_task_logger(__name__)

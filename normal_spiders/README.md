# normal_spiders
本工程目的在于构建一个较为通用的基于scrapy的爬虫工程，利用celery进行爬虫爬取调度。

## interest.sql
MySQL作为数据库，数据库名为interest，表结构见此文件。

## celery_tasks.py
爬虫调度入口文件，该文件中注释说明了如何启动与关闭，主要调度celery_task_list模块中的任务。

## celery_task_list
该模块中每个文件实现了一种celery任务，爬虫任务或者其他任务都可以。

## normal_spiders
爬虫工程具体实现部分。

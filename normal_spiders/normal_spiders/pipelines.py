# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import db as db


class NormalSpidersPipeline(object):
    def process_item(self, item, spider):
        return item


class BankCrawlResultPipeline(object):
    def insert_bank_crawl_result(self, item):
        session = db.DBSession()

        new_bank_crawl_result = db.BankCrawlResult()
        new_bank_crawl_result.crawl_time = item['crawl_time']
        new_bank_crawl_result.bank_name = item['bank_name']
        new_bank_crawl_result.source_url = item['source_url']
        new_bank_crawl_result.response = item['response']

        session.add(new_bank_crawl_result)
        session.commit()
        session.close()
        return

    def process_item(self, item, spider):
        self.insert_bank_crawl_result(item)
        return item

# -*- coding: utf-8 -*-

from datetime import datetime
import decimal
import json

from celery_config import celery_app, logger
import db


# 从爬取得到的银行数据中提取感兴趣的数据到另一个表中
# bank_crawl_result -> bank_info
@celery_app.task
def bank_response_to_info():
    logger.info('bank_response_to_info()')

    session = db.DBSession()

    last_bank_crawl_result_id = 1
    last_bank_crawl_result = session.query(db.BankInfo).order_by(db.BankInfo.bank_crawl_result_id.desc()).first()
    if last_bank_crawl_result is not None:
        last_bank_crawl_result_id = last_bank_crawl_result.bank_crawl_result_id

    deal_bank_crawl_result_list = session.query(db.BankCrawlResult)\
        .filter(db.BankCrawlResult.id > last_bank_crawl_result_id).all()

    for deal_bank_crawl_result in deal_bank_crawl_result_list:
        bank_crawl_response = deal_bank_crawl_result.response
        bank_crawl_response_json = json.loads(bank_crawl_response)
        table1_item_list = bank_crawl_response_json['Table1']

        rmb_gold_customer_sell = None
        rmb_gold_update_beijing_time = None
        for table1_item in table1_item_list:
            if table1_item['ProdName'] == '人民币账户黄金':
                rmb_gold_customer_sell = table1_item['CustomerSell']
                rmb_gold_update_beijing_time = table1_item['UpdateTime']
                break
        if rmb_gold_customer_sell is None or rmb_gold_update_beijing_time is None:
            logger.error('Can not find 人民币账户黄金 from bank_crawl_result.response where bank_crawl_result.id = '
                         + deal_bank_crawl_result.id)
            continue

        new_bank_info = db.BankInfo()
        new_bank_info.bank_crawl_result_id = deal_bank_crawl_result.id
        new_bank_info.bank_name = deal_bank_crawl_result.bank_name
        new_bank_info.rmb_gold_customer_sell = decimal.Decimal(rmb_gold_customer_sell)
        new_bank_info.rmb_gold_update_beijing_time = datetime.strptime(rmb_gold_update_beijing_time, '%Y-%m-%d %H:%M:%S')

        session.add(new_bank_info)

    session.commit()
    session.close()
    return

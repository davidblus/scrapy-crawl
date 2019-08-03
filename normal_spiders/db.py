# -*- coding: utf-8 -*-

# 导入:import db
# 取带有中文数据的字段时，需注意是否需要对unicode进行编码，可选参数encode('palmos')

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import DECIMAL
from sqlalchemy import desc
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from db_config import MYSQL_URL

# 创建对象的基类:
Base = declarative_base()


# 定义 BankCrawlResult 对象：
class BankCrawlResult(Base):
    __tablename__ = 'bank_crawl_result'

    id = Column(BigInteger, primary_key=True)
    crawl_time = Column(DateTime)
    bank_name = Column(String)
    source_url = Column(String)
    response = Column(Text)


# 定义 BankInfo 对象：
class BankInfo(Base):
    __tablename__ = 'bank_info'

    id = Column(BigInteger, primary_key=True)
    bank_crawl_result_id = Column(BigInteger)
    bank_name = Column(String)
    rmb_gold_customer_sell = Column(DECIMAL)
    rmb_gold_update_beijing_time = Column(DateTime)


# 定义 FundInfo 对象：
class FundInfo(Base):
    __tablename__ = 'fund_info'

    id = Column(BigInteger, primary_key=True)
    fund_name = Column(String)
    fund_code = Column(String)
    time = Column(Date)
    IOPV = Column(DECIMAL)
    LJJZ = Column(DECIMAL)


# 定义 WeiboStarsInfo 对象：
class WeiboStarsInfo(Base):
    __tablename__ = 'weibo_stars_info'

    id = Column(BigInteger, primary_key=True)
    star_name = Column(String)
    att_name = Column(String)
    UID = Column(BigInteger)
    CMSid = Column(Integer)
    add_V_type = Column(Integer)
    star_level = Column(Integer)
    weibo_id = Column(BigInteger)
    toutiao_id = Column(Integer)
    identify_type = Column(Integer)
    field = Column(Integer)


# 初始化数据库连接:
engine = create_engine(MYSQL_URL, encoding='utf-8', pool_recycle=3600)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 从此处开始调试，和gdb调试方法类似
# import pdb
# pdb.set_trace()

# -*- coding: utf-8 -*-

# 导入:import db
# 取带有中文数据的字段时，需注意是否需要对unicode进行编码，可选参数encode('palmos')

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Date
from sqlalchemy import DateTime
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

# 创建对象的基类:
Base = declarative_base()

# 定义Koodous对象：
class Koodous(Base):
    __tablename__ = 'koodous'

    id = Column(BigInteger, primary_key=True)
    crawl_time = Column(TIMESTAMP)
    tag = Column(String)
    source_url = Column(String)
    sha256 = Column(String)
    detail = Column(Text)
    done = Column(Boolean)

# 定义KoodousApps对象：
class KoodousApps(Base):
    __tablename__ = 'koodous_apps'

    id = Column(BigInteger, primary_key=True)
    crawl_time = Column(TIMESTAMP)
    tag = Column(String)
    source_url = Column(String)
    sha256 = Column(String)
    detail = Column(Text)
    file_url = Column(String)
    file_result = Column(String)


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://davidblus:davidblus@database-1.c7qylssqavie.ap-northeast-1.rds.amazonaws.com:3306/spider_result?charset=utf8', encoding='utf-8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 从此处开始调试，和gdb调试方法类似
# import pdb
# pdb.set_trace()



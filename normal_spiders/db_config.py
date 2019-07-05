#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 15:46
# @Author  : daipengfei
# @Site    : 
# @File    : db_config.py
# @Software: PyCharm
"""
数据库连接配置
"""

MYSQL_HOST = 'database-1.c7qylssqavie.ap-northeast-1.rds.amazonaws.com'
MYSQL_PORT = '3306'
MYSQL_USER = 'davidblus'
MYSQL_PASSWORD = 'davidblus'
MYSQL_DATABASE = 'interest'

MYSQL_URL = 'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8'\
    .format(MYSQL_USER=MYSQL_USER, MYSQL_PASSWORD=MYSQL_PASSWORD, MYSQL_HOST=MYSQL_HOST, MYSQL_PORT=MYSQL_PORT,
            MYSQL_DATABASE=MYSQL_DATABASE)

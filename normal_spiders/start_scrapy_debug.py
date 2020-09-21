#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 17:01
# @Author  : daipengfei
# @Site    : davidblus.top/wordpress
# @File    : start_scrapy_debug.py
# @Software: PyCharm
"""
debug scrapy
"""

from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute('scrapy crawl weibo_stars_high'.split())
    cmdline.execute('scrapy crawl gyrx -a startTime=20200917 -a endTime=20200921 -a fundId=485111'.split())

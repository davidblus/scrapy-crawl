# -*- coding: utf-8 -*-

from billiard.context import Process
from multiprocessing import Queue
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor


# the wrapper to make it run more times
def run_spider(spider, settings, kwargs=None):
    def f(q):
        try:
            configure_logging(settings)
            runner = CrawlerRunner()
            if kwargs is not None:
                deferred = runner.crawl(spider, **kwargs)
            else:
                deferred = runner.crawl(spider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result

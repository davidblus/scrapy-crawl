# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import craw_apps.db as db
import craw_apps.items as items

class CrawAppsPipeline(object):
    def in_koodous(self, item):
        session = db.DBSession()
        
        new_koodous = db.Koodous()
        new_koodous.crawl_time = item['crawl_time']
        new_koodous.tag = item['tag']
        new_koodous.source_url = item['source_url']
        new_koodous.sha256 = item['sha256']
        new_koodous.detail = item['detail']
        new_koodous.done = False
        
        session.add(new_koodous)
        session.commit()
        session.close()
        return
    
    def set_koodous_done(self, item):
        session = db.DBSession()
        
        koodous_info = session.query(db.Koodous).filter_by(tag=item['tag']).filter_by(sha256=item['sha256']).filter_by(done=False).one()
        koodous_info.done = True
        
        session.commit()
        session.close()
        return
    
    def in_koodous_apps(self, item):
        session = db.DBSession()
        
        new_koodous_apps = db.KoodousApps()
        new_koodous_apps.crawl_time = item['crawl_time']
        new_koodous_apps.tag = item['tag']
        new_koodous_apps.source_url = item['source_url']
        new_koodous_apps.sha256 = item['sha256']
        new_koodous_apps.detail = item['detail']
        new_koodous_apps.file_url = item['file_urls'][0]
        new_koodous_apps.file_result = str(item['files'][0])
        
        session.add(new_koodous_apps)
        session.commit()
        session.close()
        return
    
    def process_item(self, item, spider):
        if isinstance(item, items.CrawAppsItem):
            self.in_koodous(item)
        elif isinstance(item, items.CrawlAppsDownloadItem):
            self.set_koodous_done(item)
            self.in_koodous_apps(item)
        return item

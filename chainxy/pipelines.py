# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import time

import datetime

from scrapy import signals

from scrapy.exporters import CsvItemExporter


class ChainxyPipeline(object):

    def __init__(self):

        self.files = {}


    @classmethod
    def from_crawler(cls, crawler):

        pipeline = cls()

        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)

        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)

        return pipeline


    def spider_opened(self, spider):

        file = open('%s_%s.csv' % (spider.name, datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')), 'w+b')
        
        self.files[spider] = file
        
        self.exporter = CsvItemExporter(file)
        # self.exporter.fields_to_export = ['company_name','contact','phone1','phone2','email','average','reviews','address','member_for','based_in']
        
        self.exporter.fields_to_export = ['property_address', 'propert_zip', 'owner_name', 'mailing_address', 'mailing_city',  'mailing_zip', 'mailing_state', 'phone_number', 'phone_number2']
        
        self.exporter.start_exporting()        


    def spider_closed(self, spider):
        
        self.exporter.finish_exporting()
        
        file = self.files.pop(spider)
        
        file.close()


    def process_item(self, item, spider):

        self.exporter.export_item(item)
        
        return item
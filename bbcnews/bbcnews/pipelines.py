# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class CsvWriterPipeline(object):
    def __init__(self):
        self.csvwriter = None
        self.headers_written = False
    def open_spider(self):

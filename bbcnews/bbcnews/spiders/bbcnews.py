# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:33:16 2020

@author: HO Zhen Wai Olivier
"""

import scrapy


class BBCSpider(scrapy.Spider):
    name = 'bbcnews'
    allowed_domains = ['bbc.com/news']
    def start_requests(self):
        url = "http://bbc.com/news/"
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag
        yield scrapy.Request(url, self.parse)
    def parse(self, response):
        for article in response.css(''):
            yield {
                    'title' : 
                    
                    
                    }

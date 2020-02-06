# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:33:16 2020

@author: HO Zhen Wai Olivier
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from bbcsnews.items import BbcnewsArticle

class BBCSpider(CrawlSpider):
    '''
    Inherit from CrawlSpider class from Scrapy.
    '''
    name = 'BBCSpider' # Crawler Nale
    allowed_domains = ['bbc.com/news'] # Allowed domain
    start_urls = "https://bbc.com/news/"
    def __init__(self, region = None, category = None,  count_max = 1000, time_max = None, *args, **kwargs):
        count = 0

        #define the starting_urls


    def start:
    rules = (
        #Extract links matching '' (but not matching '')
        #and follow kinks from them (since no callback means follow=True by default)

        #Extract links matching '' and parse them with the spider's method parse_item

    )
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        BBCArticle = BbcnewsArticle()
        BBCArticle['title'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "story-body__h1", " " ))]").extract()
        BBCArticle['url'] = hxs.select().extract()

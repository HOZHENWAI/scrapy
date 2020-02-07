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
    limit = 1000
    inner_count = 0
    rules = (
        #Extract links matching '' (but not matching '')
        #and follow kinks from them (since no callback means follow=True by default)
        Rule(callback = parse_item, process_request = process_request, follow=True)
        #Extract links matching '' and parse them with the spider's method parse_item

    )
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        BBCArticle = BbcnewsArticle()
        BBCArticle['title'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "story-body__h1", " " ))]").extract()
        BBCArticle['url'] = response.request.url
        BBCArticle['body'] = hxs.select(//p).extract()
        BBCArticle['topics'] = hxs.select(//*[contains(concat( " ", @class, " " ), concat( " ", "tags-list__tags", " " ))]).extract()
        BBCArticle['subtitles'] = hxs.select(//*[contains(concat( " ", @class, " " ), concat( " ", "story-body__crosshead", " " ))]).extract()
        yield BBCArticle
    def process_request(self, request):
        self.inner_count = self.inner_count+1
        if self.inner_count < self.limit:
            return request
        else:
            print('Limit reached.')

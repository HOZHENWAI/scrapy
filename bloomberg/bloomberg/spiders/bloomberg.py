# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:25:50 2020

@author: HO Zhen Wai Olivier
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from bloomberg.items import BloombergArticle

class BloombergSpider(CrawlSpider):
    '''
    Inherit from CrawlSpider class from Scrapy.
    '''
    name = 'BloombergSpider' # Crawler Name
    allowed_domains = ['bbc.com/news'] # Allowed domain
    start_urls = "https://www.bloomberg.com/"
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
        Bloomberg= BloombergArticle()
        Bloomberg['title'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "lede-text-v2__hed", " " ))]").extract()
        Bloomberg['url'] = response.request.url
        Bloomberg['summary'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "abstract-v2__item-text", " " ))]").extract()
        Bloomberg['body'] = hxs.select("//p").extract()
        Bloomberg['authors'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "author-v2__byline", " " ))]").extract()
        Bloomberg['timestamp'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "article-timestamp", " " ))]").extract()
        yield Bloomberg
    def process_request(self, request):
        self.inner_count = self.inner_count+1
        if self.inner_count < self.limit:
            return request
        else:
            print('Limit reached.')

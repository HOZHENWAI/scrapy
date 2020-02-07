# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:25:50 2020

@author: HO Zhen Wai Olivier
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from cnbc.items import CnbcArticle

class CnbcSpider(CrawlSpider):
    '''
    Inherit from CrawlSpider class from Scrapy.
    '''
    name = 'BloombergSpider' # Crawler Name
    allowed_domains = ['bbc.com/news'] # Allowed domain
    start_urls = "https://www.cnbc.com/"
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
        CNBC= CnbcArticle()
        CNBC['title'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "ArticleHeader-headline", " " ))]").extract()
        CNBC['url'] = response.request.url
        CNBC['summary'] = hxs.select("//li | //*[contains(concat( " ", @class, " " ), concat( " ", "RenderKeyPoints-wrapper", " " ))]").extract()
        CNBC['body'] = hxs.select("//p").extract()
        CNBC['authors'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "Author-authorName", " " ))]").extract()
        CNBC['timestamp'] = hxs.select("//time").extract()
        yield CNBC
    def process_request(self, request):
        self.inner_count = self.inner_count+1
        if self.inner_count < self.limit:
            return request
        else:
            print('Limit reached.')

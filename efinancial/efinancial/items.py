# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from efinancial.items import JobPostingefin

class CnbcSpider(CrawlSpider):
    '''
    Inherit from CrawlSpider class from Scrapy.
    '''
    name = 'efinancialSpider' # Crawler Name
    allowed_domains = ['bbc.com/news'] # Allowed domain
    start_urls = "https://www.efinancialcareers.com/"
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
        JOB= JobPostingefin()
        JOB['PostTitle'] = hxs.select("//*[(@id = "efcJobHeaderTitleFull")]").extract()
        JOB['url'] = response.request.url
        JOB['Company'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "col", " " ))] | //strong").extract()
        JOB['Location'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "col", " " ))]").extract()
        JOB['PostDate'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "text-md-right", " " ))]").extract()
        JOB['text'] = hxs.select("//*[contains(concat( " ", @class, " " ), concat( " ", "jobContentFrame", " " ))]").extract()
        JOB['RequirementResponsibilities'] = hxs.select("//li").extract()
        yield JOB
    def process_request(self, request):
        self.inner_count = self.inner_count+1
        if self.inner_count < self.limit:
            return request
        else:
            print('Limit reached.')

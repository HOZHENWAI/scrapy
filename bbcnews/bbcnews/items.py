# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BbcnewsArticle(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    body = Field()
    topic_main = Field()
    topic_similar = Field()
    subtitles = Field()
    date = Field()
    region = Field()
    url = Field()
    author = Field()
    

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:25:50 2020

@author: HO Zhen Wai Olivier
"""

from scrapy.item import Item, Field

class JobPostingefin(Item):
    PostTitle = Field()
    Company = Field()
    Location = Field()
    PostDate = Field()
    url = Field()
    text = Field()
    RequirementResponsibilities = Field()

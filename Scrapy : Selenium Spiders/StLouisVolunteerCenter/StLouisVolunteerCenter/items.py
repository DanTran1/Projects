# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StlouisvolunteercenterItem(scrapy.Item):
    # define the fields for your item here like:
    NPO_Name = scrapy.Field()
    POC_Email = scrapy.Field()
    About_Us = scrapy.Field()
    Address = scrapy.Field()
    POC = scrapy.Field()
    Website = scrapy.Field()
    Tags = scrapy.Field()
    Opportunity = scrapy.Field()
    Facebook = scrapy.Field()
    Twitter = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PayitforwardItem(scrapy.Item):
    # define the fields for your item here like:
    NPO_Name = scrapy.Field()
    Tags = scrapy.Field()
    Phone_Number = scrapy.Field()
    Email = scrapy.Field()
    About_Us = scrapy.Field()
    Website = scrapy.Field()
    Address = scrapy.Field()
    POC = scrapy.Field()
    

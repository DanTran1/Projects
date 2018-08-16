# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OtherWebsitesItem(scrapy.Item):
    # define the fields for your item here like:
    NPO_Name = scrapy.Field()
    Address = scrapy.Field()
    Website = scrapy.Field()
    POC = scrapy.Field()
    About_Us = scrapy.Field()
    POC = scrapy.Field()
    Email = scrapy.Field()
    Phone_Number = scrapy.Field()
    Facebook = scrapy.Field()
    Twitter = scrapy.Field()
    

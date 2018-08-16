# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RiceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    NPO_Name = scrapy.Field()
    Website = scrapy.Field()
    Twitter = scrapy.Field()
    Facebook = scrapy.Field()

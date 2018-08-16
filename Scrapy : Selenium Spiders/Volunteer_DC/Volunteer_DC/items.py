# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VolunteerDcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    NPO_Name = scrapy.Field()
    Website = scrapy.Field()
    POC_Title = scrapy.Field()
    Description = scrapy.Field()
    Facebook = scrapy.Field()
    Twitter = scrapy.Field()
    Address = scrapy.Field()
    POC = scrapy.Field()
    Email = scrapy.Field()

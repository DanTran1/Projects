# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Calstate2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    NPO_name = scrapy.Field()
    Address = scrapy.Field()
    Website = scrapy.Field()
    POC = scrapy.Field()
    Main_Phone = scrapy.Field()
    General_Email = scrapy.Field()
    Description = scrapy.Field()
    Program_Info = scrapy.Field()
    First_name = scrapy.Field()
    Last_name = scrapy.Field()
    POC_Title = scrapy.Field()
    POC_Email = scrapy.Field()
    POC_Phone_Number = scrapy.Field()

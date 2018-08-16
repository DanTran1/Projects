# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OrgsyncItem(scrapy.Item):
    # define the fields for your item here like:
   
   Website = scrapy.Field()
   POC = scrapy.Field()
   Phone = scrapy.Field()
   NPO_Name = scrapy.Field()
   Email = scrapy.Field()
   Tags = scrapy.Field()
   About_Us = scrapy.Field()
   Facebook = scrapy.Field()
   Twitter = scrapy.Field()
   Address = scrapy.Field()
 

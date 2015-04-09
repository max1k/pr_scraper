# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SSDItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    usual_price = scrapy.Field()
    club_price = scrapy.Field()
    img_url = scrapy.Field()

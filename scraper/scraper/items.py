# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrTech2017Exhibitor(scrapy.Item):
    website_url = scrapy.Field()
    exhibitor_name = scrapy.Field()
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TradeShowExhibitor(scrapy.Item):
    website_url = scrapy.Field()
    exhibitor_name = scrapy.Field()


class NRFTradeShowExhibitor(scrapy.Item):
    website_url = scrapy.Field()
    exhibitor_name = scrapy.Field()
    contact_first_name = scrapy.Field()
    contact_last_name = scrapy.Field()
    contact_address1 = scrapy.Field()
    contact_address2 = scrapy.Field()
    contact_city = scrapy.Field()
    contact_state = scrapy.Field()
    contact_country = scrapy.Field()
    contact_zip = scrapy.Field()
    contact_phone = scrapy.Field()
    contact_email = scrapy.Field()
    sponsored_item = scrapy.Field()
    sponsor_level = scrapy.Field()

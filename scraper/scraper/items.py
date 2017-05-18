# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from bs4 import BeautifulSoup


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HrTech2017Exhibitor(scrapy.Item):
    website_url = scrapy.Field()
    exhibitor_name = scrapy.Field()

    def process(self, response):
        html = BeautifulSoup(response.body, "html.parser")
        self['exhibitor_name'] = html.find('div', {'id': 'eboothContainer'}).find('h1').text
        contact_url_obj = html.find('a', {'id': 'BoothContactUrl'})
        if contact_url_obj:
            self['website_url'] = contact_url_obj.text

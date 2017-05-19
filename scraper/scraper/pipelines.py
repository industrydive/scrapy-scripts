# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class TradeShowCompanyAndWebsitePipeline(object):
    ''' Generic pipeline for handling a tradeshow item that requires a
        an exhibitor name and website URL
    '''

    def open_spider(self, spider):
        print "HELLO WORLD"

    def close_spider(self, spider):
        print "GOODBYE WORLD"

    def process_item(self, item, spider):
        """ If I did anything fancy like clean or modify HTML in the properties
            of item, I would do it here

            But for now, just drop the item if it doesn't have the info I want
        """
        if not item['website_url'] or not item['exhibitor_name']:
            raise DropItem
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class HRTech2017Pipeline(object):

    def open_spider(self, spider):
        print "HELLO WORLD"

    def close_spider(self, spider):
        print "GOODBYE WORLD"

    def process_item(self, item, spider):
        """ If I did anything fancy like clean or modify HTML in the properties
            of item, I would do it here
        """
        if not item['website_url'] or not item['exhibitor_name']:
            raise DropItem
        return item

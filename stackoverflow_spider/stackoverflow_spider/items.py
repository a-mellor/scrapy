# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowSpiderItem(scrapy.Item):
    title = scrapy.Field()
    votes = scrapy.Field()
    body = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()

    # pass

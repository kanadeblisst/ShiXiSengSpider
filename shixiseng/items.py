# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    place = scrapy.Field()
    work_day = scrapy.Field()
    least_month = scrapy.Field()
    company = scrapy.Field()
    category = scrapy.Field()
    scale = scrapy.Field()
    _id = scrapy.Field()
    mongo_set = scrapy.Field()

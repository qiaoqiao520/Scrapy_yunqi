# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunqiprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImgItem(scrapy.Item):
    novel_name = scrapy.Field()
    introduce = scrapy.Field()
    src = scrapy.Field()
    all_click = scrapy.Field()
    all_popular = scrapy.Field()
    all_recommend = scrapy.Field()
    month_click = scrapy.Field()
    month_popular = scrapy.Field()
    month_recommend = scrapy.Field()
    week_click = scrapy.Field()
    week_popular = scrapy.Field()
    week_recommend = scrapy.Field()
    all_word = scrapy.Field()
    comment = scrapy.Field()
    state = scrapy.Field()

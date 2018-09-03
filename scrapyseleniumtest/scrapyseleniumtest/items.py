# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class ProductItem(Item):

    image = Field()
    price = Field()
    deal = Field()
    title = Field()
    shop = Field()
    location = Field()
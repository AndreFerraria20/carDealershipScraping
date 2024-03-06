# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CarItem(scrapy.Item):
    url= Field()
    model= Field()
    price= Field()
    make= Field()
    year= Field()
    mileage= Field()
    location= Field()
    date_posted= Field()

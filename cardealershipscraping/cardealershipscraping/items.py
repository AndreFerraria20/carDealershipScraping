# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CarItem(scrapy.Item):
    url= Field()
    make= Field()
    model= Field()
    version=Field()
    potency=Field()
    fuel_type=Field()
    displacement=Field()
    price= Field()
    year= Field()
    kilometrage= Field()
    location= Field()
    date_posted= Field()

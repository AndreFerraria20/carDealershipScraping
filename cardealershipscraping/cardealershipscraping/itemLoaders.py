from scrapy.loader import ItemLoader
from currency_converter import CurrencyConverter
import operator as op
import re

from itemloaders.processors import MapCompose, TakeFirst


def clean_price(value):
    c=CurrencyConverter(fallback_on_missing_rate=True)
    euro_list=['€','euro','eur']
    value = value.replace('.', '').replace(' ','')
    for i in euro_list:        
        if op.contains(value, i):
            value.replace(i,"")
            return value

    zloti_list=['zł','PLN']
    value = value.replace('.', '')
    for i in zloti_list:
        if op.contains(value, i):
            value.replace(i,"")
            c.convert(value,'PLN','EUR')
            return value

    return float(value)

def clean_mileage(value):
    value = value.replace('.', '').replace(' ','')
    km_list=['km','kilometros']
    for i in km_list:        
            if op.contains(value, i):
                print("true")
                value=value.replace(i,"")
                return float(value)
    mileage_list=['miles','mileage']
    for i in mileage_list:        
            if op.contains(value, i):
                value=value.replace(i,"")
                value=float(value)*1.609344
                return value
    return value
class CarDealershipItemLoader(ItemLoader):
    default_input_processor=TakeFirst()
    price_in=MapCompose(clean_price)
    kilometrage_in=MapCompose(clean_mileage)
    displacement_in=MapCompose(lambda x: int(re.sub(r'\D', '', x)))
    potency_in=MapCompose(lambda x: int(re.sub(r'\D', '', x)))
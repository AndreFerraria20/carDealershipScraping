from scrapy.loader import ItemLoader
from currency_converter import CurrencyConverter
import operator as op

from itemloaders.processors import MapCompose, TakeFirst


def clean_price(value):
    print("Cleaning price",value)
    c=CurrencyConverter(fallback_on_missing_rate=True)
    euro_list=['€','euro','eur']
    value = value.replace('.', '').replace(' ','')
    print(value)
    for i in euro_list:        
        if op.contains(value, i):
            value.split(i)[-1]
            return value

    zloti_list=['zł','PLN']
    value = value.replace('.', '')
    for i in zloti_list:
        if op.contains(value, i):
            value.split(i)[-1]
            c.convert(value,'PLN','EUR')
            return value

    return float(value)


class CarDealershipItemLoader(ItemLoader):
    default_input_processor=TakeFirst()
    price_in=MapCompose(clean_price)
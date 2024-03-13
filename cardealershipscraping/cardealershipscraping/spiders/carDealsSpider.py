import scrapy
import csv 
import json
from cardealershipscraping.items import CarItem
from scrapy.loader import ItemLoader
from cardealershipscraping.itemLoaders import CarDealershipItemLoader

class CardealsspiderSpider(scrapy.Spider):
    name = "carDealsSpider"
    #allowed_domains = [""]
    start_urls = ['www.auto.pt']  # Start URL
    def start_requests(self):
        with open('C:/Users/André/OneDrive/Documentos/Projetos/Webscraping/CarDealershipScraping/config.json') as file:
            data = json.load(file)

        for row in data:
                url=row.get('website')
                yield scrapy.Request(url=url,callback=self.parse_car_deals,meta={'config':row, 'page_number':1})

    def parse_ad_page(self, response):
            # Extract additional data from the advertisement page
            loader = response.meta['loader']
            ad_page_data = response.meta['ad_page']
            print("PARSING",ad_page_data)
            for name, xpath in ad_page_data.items():
                print("nameADPAGE",name)
                if name=='page_url':
                     continue
                value = response.xpath(xpath).get()
                loader.add_value(name, value)
            yield loader.load_item()
    
    
    def parse_car_deals(self, response):
        car_selector=response.meta['config']['selector']
        car_ads=response.xpath(car_selector)
        for car_ad in car_ads:
            l = CarDealershipItemLoader(item=CarItem(), selector=car_ad)
            ad_data=response.meta['config']['ad_data']
            for name,xpath in ad_data.items():  
                if name=='ad_page':
                    print("adpageenter",ad_data['ad_page']['page_url'])
                    page_url = car_ad.xpath(ad_data['ad_page']['page_url']).get()
                    print("pageurl",page_url)
                    l.add_value('url',page_url)
                    break
                if xpath != "":
                    l.add_xpath(name,xpath)
            print("Yielding",ad_data)
            if('ad_page' in ad_data and ad_data['ad_page'] != None):
                yield scrapy.Request(url=page_url, callback=self.parse_ad_page, meta={'loader': l,'ad_page':ad_data['ad_page']})
            else:
                yield l.load_item()





            
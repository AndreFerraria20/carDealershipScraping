import scrapy
import csv 
from cardealershipscraping.items import CarItem
from scrapy.loader import ItemLoader
from cardealershipscraping.itemLoaders import CarDealershipItemLoader

class CardealsspiderSpider(scrapy.Spider):
    name = "carDealsSpider"
    allowed_domains = [""]
    start_urls = [""]
    def start_requests(self):
        with open(r'C:\Users\André\OneDrive\Documentos\Projetos\Webscraping\CarDealershipScraping\websitesConfig.csv',encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                url=row['url'].format(page_number=1)
                yield scrapy.Request(url=url,callback=self.parse_car_deals,meta={'config':row, 'page_number':1})

    
    
    def parse_car_deals(self, response):
        print("Meta",response.meta)
        url=response.meta["config"].pop('url')
        car_ads=response.xpath(response.meta["config"]['carDivs'])
        for car_ad in car_ads:
            l = CarDealershipItemLoader(item=CarItem(), selector=car_ad)
            for name,xpath in response.meta["config"].items():
                if name=='carDivs':
                    break
                if xpath != "":
                    l.add_xpath(name,xpath)
            return l.load_item()
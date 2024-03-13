# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itertools import count

class CardealershipscrapingPipeline:
    counter = count(start=1)  # Start counting from 1
    def process_item(self, item, spider):
        print("counter item",next(self.counter))  # Output: 1

        return item



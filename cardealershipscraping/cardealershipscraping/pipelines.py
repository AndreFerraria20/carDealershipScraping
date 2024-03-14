# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itertools import count
import json
import os



class CardealershipscrapingPipeline:
    def open_spider(self, spider):
        # Open a file for writing in the 'output' directory
        if not os.path.exists('output'):
                    os.makedirs('output')        
        self.file_path = 'output/items.json'
        self.file = open(self.file_path, 'a+')
        self.file.seek(0)

    def close_spider(self, spider):
        # Close the file when the spider is closed
        self.file.close()

    def process_item(self, item, spider):
        print("Process start item")
        # Convert the item to a dictionary and write it to the file as JSON
        line = json.dumps(dict(item)) + ",\n"
        print("line to write", line)
        self.file.write(line)
        return item



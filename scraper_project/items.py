# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperProjectItem(scrapy.Item):
    
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
   

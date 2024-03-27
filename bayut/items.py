# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BayutItem(scrapy.Item):
    price = scrapy.Field()
    space = scrapy.Field()
    city_and_region = scrapy.Field()
    path_rooms = scrapy.Field()
    sleep_rooms = scrapy.Field()


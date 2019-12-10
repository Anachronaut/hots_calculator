# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from main_calc.models import Hero

class HotsScraperHero(DjangoItem):
    django_model = Hero
    image_urls = scrapy.Field()
    images = scrapy.Field()

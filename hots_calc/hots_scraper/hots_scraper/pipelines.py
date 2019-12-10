# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import sqlite3
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os

class HotsScraperPipeline(object):

    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS main_calc_hero(
            id INTEGER PRIMARY KEY, 
            name VARCHAR(75), 
            image BLOB,
            win_rate REAL(8), 
            popularity INTEGER(3), 
            ban_rate REAL(8), 
            games_played INTEGER(15), 
            win_total INTEGER(15), 
            loss_total INTEGER(15))''')

    def process_item(self, item, spider):
        self.cursor.execute("select * from main_calc_hero where name=?", (item['name'],))
        result = self.cursor.fetchone()
        if result:
            if item['name'] == result[1]:
                logging.exception("Item already in database: %s" % item)
                self.cursor.execute("delete from main_calc_hero where name = ?", (item['name'],))
                self.connection.commit()
                logging.log(20, "Item stored : " % item)
            
        image = 'hero_images/' + item['images'][0]['path']
        self.cursor.execute("insert into main_calc_hero (name, image, win_rate, popularity, ban_rate, games_played, win_total, loss_total) values (?, ?, ?, ?, ?, ?, ?, ?)",
            (item['name'], image, item['win_rate'], item['popularity'], item['ban_rate'], item['games_played'], item['win_total'], item['loss_total']))
        self.connection.commit()
        logging.log(20, "Item stored : " % item)
        return item

def get_media_requests(self, item, info):
    # values in field "image_name" must have suffix ".jpg"
    # you can only change "image_name" to your own image name filed "images"
    # however it should be a list
    for (image_url, image_name) in zip(item[self.IMAGES_URLS_FIELD], item["image_name"]):
        yield scrapy.Request(url=image_url, meta={"image_name": name})

def file_path(self, item, response=None, info=None):
    image_guid = item['name']
    return '%s.jpg' % (image_guid)

def handle_error(self, e):
    logging.error(e)

class HeroImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [scrapy.Request(x, meta={'image_name': item["name"]}) 
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None):
        return f'{request.meta["image_name"]}.jpg'
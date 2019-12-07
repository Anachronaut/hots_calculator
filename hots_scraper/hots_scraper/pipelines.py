# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import sqlite3


class HotsScraperPipeline(object):

    def __init__(self):
        self.connection = sqlite3.connect('../db.sqlite3')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS main_calc_hero(
            id INTEGER PRIMARY KEY, 
            name VARCHAR(75), 
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
            logging.exception("Item already in database: %s" % item)
            pass
        else:
            self.cursor.execute(            #1       2          3         4           5            6          7               1  2  3  4  5  6  7
                "insert into main_calc_hero (name, win_rate, popularity, ban_rate, games_played, win_total, loss_total) values (?, ?, ?, ?, ?, ?, ?)",
                (item['name'], item['win_rate'], item['popularity'], item['ban_rate'], item['games_played'], item['win_total'], item['loss_total']))
                    #1                  2                   3                       4                   5                           6                   7
            self.connection.commit()
            logging.log(20, "Item stored : " % item)

        item.save()
        return item

def handle_error(self, e):
    logging.error(e)
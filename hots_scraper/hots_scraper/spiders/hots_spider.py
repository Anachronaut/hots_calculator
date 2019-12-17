# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from hots_scraper.hots_scraper.items import HotsScraperHero


def check_for_100per(rate_list):
    ctr = 0
    for i in rate_list:
        if ctr == 2:
            return True
        elif i[1] == 100 or i[1] == 100.00:
            ctr = ctr + 1
    return False

class HotsSpider(scrapy.Spider):
    name = 'hots_spider'
    allowed_domains = ['heroesprofile.com']
    start_urls = ['https://heroesprofile.com/Global/Hero/']

    def parse(self, response):
        custom_settings = {
        "IMAGES_STORE": '../hots_calc/main_calc/media/hero_images'
    }
        data = response.css("table.primary-data-table tbody tr")

        for i,j in enumerate(data):
            item = HotsScraperHero()
            if j.css("a.vertically-aligned::text").get() == None:
                continue
            else:
                item['name'] = j.css("a.vertically-aligned::text").get()
                image = j.css("div.hero-picture img::attr(src)").get()
                item['image_urls'] = ("https://heroesprofile.com/" + image,)
                item['win_rate'] = j.css("td.win_rate_cell::text").get()
                item['popularity'] = j.css("td.popularity_cell::text").get()
                item['ban_rate'] = j.css("td.ban_rate_cell::text").get()
                games_played = j.css("td.games_played_cell::text").get()
                item['games_played'] = int(games_played.replace(',',''))
                win_total = j.css("td.wins_cell::text").get()
                item['win_total'] = int(win_total.replace(',',''))
                loss_total = j.css("td.losses_cell::text").get()
                item['loss_total'] = int(loss_total.replace(',',''))
                request = scrapy.Request("https://heroesprofile.com/Global/Matchups/?hero="+item['name'],
                                         callback=self.parse_match)
                request.meta['item'] = item
                yield request

    def parse_match(self, response):
        item = response.meta['item']
        data = response.css("div.rectangular-box.hero-category div.hero-wrapper div.popup-trigger")
        match_list = []
        for i in data:
            popup_txt = i.css("div.popup::text").get()
            win_per = (re.search('(\d+(\.\d+)?%)',popup_txt).group())
            win_per = float(win_per.replace('%', ''))
            hero_name = i.css("div.popup h4::text").get()
            hero_win_tuple = (hero_name, win_per)
            match_list.append(hero_win_tuple)
        
        #hundreds = check_for_100per(match_list)

        #if not hundreds:

        if len(match_list) <=9:
            diff = 10 - len(match_list)
            for i in range(diff):
                match_list.append('No Match', '0.0')
        
        for i,j in enumerate(match_list[:5],1):
            str_i = str(i)
            #print(item['name']+':','Ally'+str_i,j)
            
            item['ally_'+str_i] = j[0]
            item['ally_'+str_i+'_win'] = j[1]

        for i,j in enumerate(match_list[5:],1):
            str_i = str(i)
            item['enemy_'+str_i] = j[0]
            item['enemy_'+str_i+'_win'] = j[1]
        
        yield item

        #else:
            #logging.log(30, 'Multiple 100% victories or losses, double-check data')
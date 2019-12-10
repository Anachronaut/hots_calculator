# -*- coding: utf-8 -*-
import scrapy
from hots_scraper.hots_scraper.items import HotsScraperHero


class HotsSpider(scrapy.Spider):
    name = 'hots_spider'
    allowed_domains = ['heroesprofile.com']
    start_urls = ['https://heroesprofile.com/Global/Hero/']

    def parse(self, response):
        custom_settings = {
        "IMAGES_STORE": '../hots_calc/main_calc/media/hero_images'
    }
        data = response.css("table.primary-data-table tbody tr")
        
        hero_dict={}

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
                yield item
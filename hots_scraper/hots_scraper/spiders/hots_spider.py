# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from hots_scraper.hots_scraper.items import HotsScraperHero


class HotsSpider(scrapy.Spider):
    name = 'hots_spider'
    allowed_domains = ['heroesprofile.com']
    start_urls = ['https://heroesprofile.com/Global/Hero/']

    def parse(self, response):
        
        data = response.css("table.primary-data-table tbody tr")

        for i in data:
            item = HotsScraperHero()
            if i.css("a.vertically-aligned::text").get() == None:
                continue
            else:
                item['name'] = i.css("a.vertically-aligned::text").get() #Hero Name
                image = i.css("div.hero-picture img::attr(src)").get()  #Hero Image
                item['image_urls'] = ("https://heroesprofile.com/" + image,)    #URL of Image
                item['win_rate'] = i.css("td.win_rate_cell::text").get()    #Hero Win Percentage
                item['popularity'] = i.css("td.popularity_cell::text").get()    #Hero Popularity Rating
                item['ban_rate'] = i.css("td.ban_rate_cell::text").get()    #Hero Ban Percentage
                games_played = i.css("td.games_played_cell::text").get()    #Hero Total Games Played
                item['games_played'] = int(games_played.replace(',',''))    #Remove commas from Games Played
                win_total = i.css("td.wins_cell::text").get()   #Hero Total Wins
                item['win_total'] = int(win_total.replace(',',''))  #Remove commas from Total Wins
                loss_total = i.css("td.losses_cell::text").get()    #Hero Total Losses
                item['loss_total'] = int(loss_total.replace(',',''))    #Remove commas from Total Losses
                #Pass to parse_match() to scrape Hero matchups
                request = scrapy.Request("https://heroesprofile.com/Global/Matchups/?timeframe_type=major&timeframe=2.49&hero="+item['name']+"&game_type=sl",   callback=self.parse_match) #TODO: ^Scrape Major Patch Dropdown for this URL
                request.meta['item'] = item
                yield request


    def parse_match(self, response): #Scrape hero matchups (top 5 teammates and top 5 counters)
        item = response.meta['item']
        data = response.css("div.rectangular-box.hero-category div.hero-wrapper div.popup-trigger")
        match_list = []
        for i in data:
            popup_txt = i.css("div.popup::text").get() #Match pop-up text (Contains matchup stats)
            win_per = (re.search('(\d+(\.\d+)?%)',popup_txt).group())   #Match percentage of wins with parent Hero
            win_per = float(win_per.replace('%', ''))
            hero_name = i.css("div.popup h4::text").get()   #Match name
            hero_win_tuple = (hero_name, win_per)
            match_list.append(hero_win_tuple)


        if len(match_list) <=9: #Check if less than 5 ally or enemy matchups, insert dummy matchups
            diff = 10 - len(match_list)
            for i in range(diff):
                match_list.append('No Match', '0.0')
        
        for i,j in enumerate(match_list[:5],1): #ally matchups 1-5
            str_i = str(i)
            
            item['ally_'+str_i] = j[0]
            item['ally_'+str_i+'_win'] = j[1]

        for i,j in enumerate(match_list[5:],1): #enemy matchups 1-5
            str_i = str(i)
            item['enemy_'+str_i] = j[0]
            item['enemy_'+str_i+'_win'] = j[1]
        
        yield item
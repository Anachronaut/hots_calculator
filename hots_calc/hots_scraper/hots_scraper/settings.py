# -*- coding: utf-8 -*-

# Scrapy settings for hots_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import sys
import os
import django

#Don't touch this
sys.path.append(os.path.dirname(os.path.abspath('../')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hots_calculator.settings'
django.setup()

'''
file_str_replace() and django_setup_update() prevent errors from directory tree/import issues
with the main_calc app in /hots_calc/settings.py, otherwise scraper or app do not recognize
main_calc ALLOWED_APP depending on configuration
'''
'''
def file_str_replace(str1, str2):
    settings = open('..\..\hots_calc\hots_calculator\settings.py', 'rt')
    data = settings.read()
    data = data.replace(str1, str2)
    settings.close()

    settings = open('..\..\hots_calc\hots_calculator\settings.py','wt')
    settings.write(data)
    settings.close()


def django_setup_update():

    file_str_replace('  main_calc', '   hots_calc.main_calc')
    django.setup()
    file_str_replace('  hots_calc.main_calc', ' main_calc')

django_setup_update()
'''

BOT_NAME = 'hots_scraper'

SPIDER_MODULES = ['hots_scraper.spiders']
NEWSPIDER_MODULE = 'hots_scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hots_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hots_scraper.middlewares.HotsScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'hots_scraper.middlewares.HotsScraperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hots_scraper.pipelines.HotsScraperPipeline': 300,
    'hots_scraper.pipelines.HeroImagesPipeline': 1
}
IMAGES_STORE = '../../media/hero_images'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
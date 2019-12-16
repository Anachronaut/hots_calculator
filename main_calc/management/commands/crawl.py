from django.core.management.base import BaseCommand

from scrapy.crawler import CrawlerProcess
#from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from hots_scraper.hots_scraper.spiders.hots_spider import HotsSpider

import hots_scraper.hots_scraper.settings as scrapy_settings

class Command(BaseCommand):
    help = '''
    The key to efficient web-crawling... Is proper distribution.
                                                        -Anub'arak, the Traitor King'''

    def handle(self, *args, **options):
        scraper_settings = Settings()
        scraper_settings.setmodule(scrapy_settings)
        process = CrawlerProcess(settings=scraper_settings)

        process.crawl(HotsSpider)
        process.start()
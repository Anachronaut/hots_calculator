from django.core.management.base import BaseCommand
from hots_scraper.hots_scraper.spiders.hots_spider import HotsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = "The key to efficient web-crawling... Is proper distribution."

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(HotsSpider)
        process.start()
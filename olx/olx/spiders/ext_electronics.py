from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExtElectronicsSpider(CrawlSpider):
    name = "ext_electronics"
    allowed_domains = ["www.olx.ua"]
    start_urls = [
        'https://www.olx.ua/computers-accessories/',
        'https://www.olx.ua/tv-video-audio/',
        'https://www.olx.ua/games-entertainment/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExtElectronicsSpider(CrawlSpider):
    name = "appartments"
    allowed_domains = ["www.olx.ua"]
    start_urls = [
        'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/kvartira/odessa/?search%5Bfilter_float_price%3Afrom%5D=4000&search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_number_of_rooms%3Ato%5D=2&search%5Bfilter_float_number_of_rooms%3Afrom%5D=1&search%5Bphotos%5D=1&search%5Bprivate_business%5D=private&search%5Bdistrict_id%5D=89'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)

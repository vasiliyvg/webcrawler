import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx.items import OlxItem


class ExtElectronicsSpider(CrawlSpider):
    name = "appartments"
    allowed_domains = ["www.olx.ua"]
    start_urls = [
        # 'https://www.olx.ua/',
        # 'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/odessa/'
        'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/kvartira/odessa/?search%5Bfilter_float_price%3Afrom%5D=4000&search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_number_of_rooms%3Ato%5D=2&search%5Bfilter_float_number_of_rooms%3Afrom%5D=2&search%5Bphotos%5D=1&search%5Bprivate_business%5D=private&search%5Bdistrict_id%5D=89'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    # def parse_item(self, response):
    #     print('Processing..' + response.url)

    def parse_item(self, response):
        # item_links = response.css('.offer-wrapper .detailsLink::attr(href)').extract()
        item_links = response.css('.detailsLink::attr(href)').extract()
        for a in item_links:
            yield Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('.price-label strong::text').extract()[0].strip()
        price = response.css('.offer-titlebox h1::text').extract()[0].replace('"', '').strip()

        item = OlxItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        yield item
# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.olx.ua']
    start_urls = ['http://www.olx.ua/']

    def parse(self, response):
        pass

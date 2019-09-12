# -*- coding: utf-8 -*-
import scrapy


class PowerbuySpider(scrapy.Spider):
    name = 'ishopchangi'
    allowed_domains = ['ishopchangi.com']
    start_urls = ['https://www.ishopchangi.com/category/electronics/audio-84/earphones-apple-earpods-703']

    def parse(self, response):
        print('---repso'
              'ne---')
        print(response)
        pass


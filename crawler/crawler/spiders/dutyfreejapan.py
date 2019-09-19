# -*- coding: utf-8 -*-
import scrapy

from re import sub
from decimal import Decimal



class DutyfreejapanSpider(scrapy.Spider):
    name = 'dutyfreejapan'
    allowed_domains = ['duty-free-japan.jp']
    start_urls = ['https://duty-free-japan.jp/narita/en/goodsList.aspx?catCd=021&itemCD=000056']

    def parse(self, response):
        for product_detail in response.css('.productDetail'):

            price_with_currency = product_detail.css('.goods_price ::text').get()
            name = product_detail.css('.goods_name-bold ::text').get()
            brand = product_detail.css('.goods_brand ::text').get()

            price = Decimal(sub(r'[^\d.]', '', price_with_currency))
            currency = price_with_currency[0]
            sku = product_detail.css('.goods_id span')[0].css('::text').get()

            yield {
                'name': name,
                'brand': brand,
                'price': price,
                'sku': sku,
                'currency': currency
            }

        for product_page_link in response.css('ul#js_listProduct a.productItem_link'):
            yield response.follow(product_page_link, self.parse)




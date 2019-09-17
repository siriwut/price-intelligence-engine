# -*- coding: utf-8 -*-
import scrapy



class DutyfreejapanSpider(scrapy.Spider):
    name = 'dutyfreejapan'
    allowed_domains = ['duty-free-japan.jp']
    start_urls = ['https://duty-free-japan.jp/narita/en/goodsList.aspx?catCd=021&itemCD=000056']

    def parse(self, response):
        for product_detail in response.css('.productDetail'):
            yield {
                'name': product_detail.css('.goods_name-bold ::text').get(),
                'brand': product_detail.css('.goods_brand ::text').get(),
                'price': product_detail.css('.goods_price ::text').get()
            }

        for product_page_link in response.css('ul#js_listProduct a.productItem_link'):
            yield response.follow(product_page_link, self.parse)

        for next_page_link in response.css('a.listPager'):


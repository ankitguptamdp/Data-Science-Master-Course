# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.in/Books-Last-30-days/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_85%3A10440599031&dc&qid=1573500212&rnid=10440598031&ref=sr_nr_p_85_1']

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        print(product_name)
        print(product_author)
        print(product_price)
        print(product_imagelink)

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.in/Books-Last-30-days/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_85%3A10440599031&dc&page=2&qid=1574433531&rnid=10440598031&ref=sr_pg_'+str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number<=100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
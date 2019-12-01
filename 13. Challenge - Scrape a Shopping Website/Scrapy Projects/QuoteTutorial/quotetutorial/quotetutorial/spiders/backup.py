import scrapy
from ..items import QuotetutorialItem


# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'http://quotes.toscrape.com/'
#     ]
#
#     def parse(self, response):
#
#         items = QuotetutorialItem()
#
#         all_div_quotes = response.css('div.quote') # all_div_quotes = response.css('div.quote')[0]
#         for quote in all_div_quotes:
#             title = quote.css('span.text::text').extract()
#             author = quote.css('.author::text').extract()
#             tag = quote.css('.tag::text').extract() #        tag = all_div_quotes.css('.tags::text').extract()
#
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#
#             # yield {
#             #     'title': title,
#             #     'author': author,
#             #     'tag': tag
#             # }
#
#             yield items
#
#         next_page = response.css('li.next a::attr(href)').get()
#
#         if next_page is not None:
#             yield response.follow(next_page, callback = self.parse)

# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     page_number = 2
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/'
#     ]
#
#     def parse(self, response):
#
#         items = QuotetutorialItem()
#
#         all_div_quotes = response.css('div.quote') # all_div_quotes = response.css('div.quote')[0]
#         for quote in all_div_quotes:
#             title = quote.css('span.text::text').extract()
#             author = quote.css('.author::text').extract()
#             tag = quote.css('.tag::text').extract() #        tag = all_div_quotes.css('.tags::text').extract()
#
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#
#             yield items
#
#         next_page = 'http://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
#
#         if QuoteSpider.page_number < 11:
#             QuoteSpider.page_number += 1
#             yield response.follow(next_page, callback = self.parse)

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        print()
        print(token)
        print()

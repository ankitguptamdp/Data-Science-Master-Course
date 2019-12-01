import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username' : 'happyankitgupta@gmail.com',
            'password' : 'password'
        }, callback= self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote') # all_div_quotes = response.css('div.quote')[0]
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract() #        tag = all_div_quotes.css('.tags::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items


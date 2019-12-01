import scrapy
from ..items import BookstoreItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        items = BookstoreItem()
        all_books = response.css('section')
        for book in all_books:
            image_urls = book.css('.thumbnail::attr(src)').extract()
            book_titles = book.css('.product_pod a::attr(title)').extract()
            product_prices = book.css('.price_color::text').extract()
            for i in range(len(image_urls)):
                items['image_url'] = image_urls[i]
                items['book_title'] = book_titles[i]
                items['product_price'] = product_prices[i]
                yield {
                    'image_url':image_urls[i],
                    'book_title':book_titles[i],
                    'product_price':product_prices[i]
                }

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"  

    def start_requests(self):

        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
            ]

        #Generator Function
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page_id = response.url.split("/")[-2] # -2 will give page index
        filename = "quotes-%s.html"%page_id

        for q in response.css("div.quote"):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()

            yield {
                'text':text,
                'author':author,
                'tags':tags,
                }

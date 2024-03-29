import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quote"  

    def start_requests(self):

        urls = [
            "http://quotes.toscrape.com/page/1/",
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

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

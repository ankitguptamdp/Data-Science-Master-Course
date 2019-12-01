import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"  

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
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s"%filename)
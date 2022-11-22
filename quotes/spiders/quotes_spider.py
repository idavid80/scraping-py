import scrapy
from scrapy import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(100)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        divs = response.css('div.quote')
        for div in divs:
            yield {
                'texto': div.css('span.text::text').getall(),
                'autor': div.css('span.text::text').getall(),
                'tags': div.css('a.tag::text').getall()
            }
            # filename = f'quotes-{page}.html'
            # with open(filename, 'wb') as file:
            #     file.write(response.body)
            # self.log(f'Saved file {filename}')

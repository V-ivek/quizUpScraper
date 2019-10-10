import scrapy


class QuizUpSpider(scrapy.Spider):
    name = "quizup"

    def start_requests(self):
        urls = [
            'https://quizup.net/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            for href in response.css('#text-5 > div > a::attr(href)'):
                yield{
                    'link': href.get()
                }
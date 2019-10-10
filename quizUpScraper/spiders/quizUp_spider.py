import scrapy

class QuizUp(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()

class QuizUpSpider(scrapy.Spider):
    name = "quizupone"

    def start_requests(self):
        urls = [
            'https://quizup.net/batman',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        i=0
        while i < (len(response.xpath('//tr[contains(@class, "row")]'))-1):
            print(str(response.xpath('//td[contains(@class, "column-1")]/text()').extract()[i]))
            item = QuizUp()
            item['question']= str(response.xpath('//td[contains(@class, "column-1")]/text()').extract()[i])
            item['answer']= str(response.xpath('//td[contains(@class, "column-2")]/text()').extract()[i])
            i=i+1
            yield item
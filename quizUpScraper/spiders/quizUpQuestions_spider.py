import scrapy
import json

class QuizUpSpider(scrapy.Spider):
    name = "questions"
    
    def start_requests(self):
        urls =  []
        with open('./links.json') as json_file:
                data = json.load(json_file)
                for l in data['links']:
                    urls.append(l)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ls = response.xpath('//tr[contains(@role, "row")]').get()
        print(ls)

    #     urls = [
    #         'https://quizup.net/',
    #     ]link
 
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #         for href in response.css('#text-5 > div > a::attr(href)'):
    #             yield  
    #                 'link': href.get()
    #               
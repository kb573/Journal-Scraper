import scrapy
import json
from urllib.parse import urlencode

class paper_spider(scrapy.Spider):
    name = 'paper_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("urls9.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["link"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)


    def parse(self, response):

        info_panel = response.css('[id="biblio-body"]')

        yield{
            'info1': info_panel.css('li::text').getall(),
            'info2': info_panel.css('a::text').getall(),
            'link': response.request.url
        }

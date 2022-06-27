import scrapy
import json

class paper_spider(scrapy.Spider):
    name = 'paper_spider'

    start_urls = []

    with open("test_urls.json", "r") as f:
        jsonlist = json.load(f)

    for i in range(len(jsonlist)):
        url = jsonlist[i]["link"]
        start_urls.append(url)

    def parse(self, response):

        info_panel = response.css('[id="biblio-body"]')

        yield{
            'title': response.css('title::text').get(),
            'authors': info_panel.css('li::text')[0].getall()[0][2:-9].split('&'),
            'journal_name': info_panel.css('a::text')[1].getall()[0],
            'organisation': info_panel.css('li::text')[2].getall()[0].split(',')[1][1:],
            'vol/iss': info_panel.css('li::text')[2].getall()[0].split(',')[2][6:],
            'pages': info_panel.css('li::text')[2].getall()[0].split(',')[3][7:],
            'month': info_panel.css('li::text')[2].getall()[0].split(',')[4][1:-2],
            'year': info_panel.css('li::text')[0].getall()[0][-7:-3],
            'link': response.request.url
        }

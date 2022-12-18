import scrapy

class url_spider(scrapy.Spider):
    name = 'url_spider'
    start_urls = ['https://ideas.repec.org/s/aea/aecrev.html',
                'https://ideas.repec.org/s/oup/qjecon.html',
                'https://ideas.repec.org/s/ucp/jpolec.html',
                'https://ideas.repec.org/s/ecm/emetrp.html',
                'https://ideas.repec.org/s/wly/emetrp.html',
                'https://ideas.repec.org/s/oup/restud.html',
                'https://ideas.repec.org/s/bla/jfinan.html',
                'https://ideas.repec.org/s/eee/jfinec.html',
                'https://ideas.repec.org/s/eee/revfin.html',
                'https://ideas.repec.org/s/wly/revfec.html'
                ]

    def parse(self, response):
        for panel in response.css('div.panel-body'):
            for paper in panel.css("::attr(href)"):
                yield{
                    'link': 'https://ideas.repec.org' + paper.get()
                }

        page_bar = response.css('ul.pagination.flex-wrap')[0]
        page_items = page_bar.css('li.page-item')[-1]
        next_page = page_items.css('a.page-link::attr(href)').get()

        if next_page is not None:
            next_page = response.request.url[:30] + next_page
            yield response.follow(next_page, callback=self.parse)

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEPS_DOMAIN, PEPS_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEPS_DOMAIN]
    start_urls = [PEPS_URL]

    def parse(self, response):
        peps = response.css('tbody tr td:nth-child(2) a::attr(href)').getall()
        for pep_link in peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('#pep-content h1::text').get().split(' – ')
        number = int(title[0].replace('PEP ', ''))
        name = ' – '.join(title[1:])
        data = dict(
            number=number,
            name=name,
            status=response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        )
        yield PepParseItem(data)

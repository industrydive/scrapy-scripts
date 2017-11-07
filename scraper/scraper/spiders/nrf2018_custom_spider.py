from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import NRFTradeShowExhibitor


class nrf2018(CrawlSpider):
    ''' Spider for NRF Conference 2018
        https://industrydive.atlassian.net/browse/TECH-2834

        example usage:
        scrapy crawl nrf2018 --output=nrf2018.csv --output-format=csv
    '''

    name = "nrf2018"
    allowed_domains = ["nrfbigshow.nrf.com"]
    start_urls = ["https://nrfbigshow.nrf.com/exhibitors"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.TradeShowCompanyAndWebsitePipeline': 1,
        },
        # 'CLOSESPIDER_ITEMCOUNT': 3,  # for testing - comment out for IRL
        # 'CONCURRENT_REQUESTS': 1,  # for testing - comment out for IRL
    }

    def parse_item(self, response):
        ''' Parse exhibitor detail page
            Override this as needed
        '''
        import urllib2

        item = NRFTradeShowExhibitor()
        html = BeautifulSoup(response.body, "html.parser")

        booth_obj = html.find('div', {'class': 'company_booths'})
        booth_number = booth_obj.find('a').text

        item['exhibitor_name'] = html.find('div', {'class': 'company_name'}).text

        # there is no prganic way to get to the URL that has the exhibitor details that were requested
        # there is no hpyerlink on the main list page or the normal details page for the spider to crawl to
        # so - let's just execute a urllib call here to open the page at the URL we know the details should
        # be at, and then BeautifulSoup it from there
        exhibitor_detail = BeautifulSoup(urllib2.urlopen("https://nrfbigshow.nrf.com/%s" % booth_number).read(), "html.parser")

        website_class = exhibitor_detail.body.find('div', {'class': 'field--name-field-booth-website'})

        link = website_class.find('a')
        if link:
            item['website_url'] = link.get('href')

        generic_fields = [
            'contact_first_name',
            'contact_last_name',
            'contact_address1',
            'contact_address2',
            'contact_city',
            'contact_state',
            'contact_country',
            'contact_zip',
            'contact_phone',
            'contact_email',
            'sponsored_item',
            'sponsor_level',
        ]

        for field in generic_fields:
            field_class = exhibitor_detail.body.find('div', {'class': 'field--name-field-booth-%s' % field.replace('_', '-')})
            item[field] = field_class.find('div', {'class': 'field__item even'}).text

        yield item

    rules = [
        Rule(
            # rule for exhibitor detail link
            LinkExtractor(
                allow=(
                    # ex: https://nrfbigshow.nrf.com/company/42-technologies
                    u'\/company\/',
                ),
            ),
            callback='parse_item',
            follow=False,  # no further info needed, stop at this page
        ),
    ]

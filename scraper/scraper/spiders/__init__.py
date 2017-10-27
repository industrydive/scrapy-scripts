from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import TradeShowExhibitor, NRFTradeShowExhibitor
from bs4 import BeautifulSoup


class TradeShowSpider(CrawlSpider):
    ''' Generic base spider for crawling tradeshow lists
    '''
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
        item = TradeShowExhibitor()
        html = BeautifulSoup(response.body, "html.parser")
        item['exhibitor_name'] = html.find('div', {'id': 'eboothContainer'}).find('h1').text.strip()
        contact_url_obj = html.find('a', {'id': 'BoothContactUrl'})
        if contact_url_obj:
            item['website_url'] = contact_url_obj.text
        # needs to be yield or else PipeLine.process_item() doesn't get called
        yield item


class HrTech2017(TradeShowSpider):
    ''' Spider for HR Technology Conference 2017
        https://industrydive.atlassian.net/browse/TECH-1623
    '''

    name = "hrtech2017"
    allowed_domains = ["s23.a2zinc.net"]
    start_urls = ["http://s23.a2zinc.net/clients/lrp/hrtechnologyconference2017/Public/exhibitors.aspx?Index=All"]

    rules = [
        Rule(
            # rule for exhibitor detail link
            LinkExtractor(
                allow=(
                    u'\/(clients/lrp/hrtechnologyconference2017/Public/eBooth.aspx\?)',
                ),
            ),
            callback='parse_item',
            follow=False,  # no further info needed, stop at this page
        ),
    ]


class DistribuTech2018(TradeShowSpider):
    ''' Spider for HR Technology Conference 2017
        https://industrydive.atlassian.net/browse/TECH-1623
    '''

    name = "distributech2018"
    allowed_domains = ["events.pennwell.com"]
    start_urls = ["http://events.pennwell.com/DTECH2018/Public/exhibitors.aspx?_ga=2.91461086.575732828.1507662078-248451487.1507662078"]

    rules = [
        Rule(
            # rule for exhibitor detail link
            LinkExtractor(
                allow=(
                    # ex: http://events.pennwell.com/DTECH2018/Public/eBooth.aspx
                    # ?IndexInList=0&FromPage=Exhibitors.aspx&ParentBoothID=&ListByBooth=true&BoothID=539921
                    u'\/(DTECH2018/Public/eBooth.aspx\?)',
                ),
            ),
            callback='parse_item',
            follow=False,  # no further info needed, stop at this page
        ),
    ]


class nrf2018(TradeShowSpider):
    ''' Spider for HR Technology Conference 2017
        https://industrydive.atlassian.net/browse/TECH-1623
    '''

    name = "nrf2018"
    allowed_domains = ["nrfbigshow.nrf.com"]
    start_urls = ["https://nrfbigshow.nrf.com/exhibitors"]

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

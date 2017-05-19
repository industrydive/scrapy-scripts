from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import HrTech2017Exhibitor
from bs4 import BeautifulSoup


class TradeShowSpider(CrawlSpider):
    ''' Generic base spider for crawling tradeshow lists
    '''
    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.TradeShowCompanyAndWebsitePipeline': 1,
        },
        'CLOSESPIDER_ITEMCOUNT': 5,  # for testing
        'CONCURRENT_REQUESTS': 1,  # for testing
    }

    def parse_item(self, response):
        ''' Parse exhibitor detail page
            Override this as
        '''
        item = HrTech2017Exhibitor()
        html = BeautifulSoup(response.body, "html.parser")
        item['exhibitor_name'] = html.find('div', {'id': 'eboothContainer'}).find('h1').text
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

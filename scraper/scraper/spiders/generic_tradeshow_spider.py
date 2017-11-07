import sys
from urlparse import urlparse
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import TradeShowExhibitor


def _get_start_url_from_cli():
    args = [arg for arg in sys.argv if arg.startswith("--set=start_url=")]
    for arg in args:
        return arg.replace("--set=start_url=", "")
    return None


class TradeShowSpider(CrawlSpider):
    ''' Generic base spider for crawling tradeshow lists

    '''
    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.TradeShowCompanyAndWebsitePipeline': 1,
        },
        'CLOSESPIDER_ITEMCOUNT': 3,  # for testing - comment out for IRL
        'CONCURRENT_REQUESTS': 1,  # for testing - comment out for IRL
    }

    name = "tradeshow"
    start_urls = [_get_start_url_from_cli()]
    if start_urls[0]:  # we need to do this because scrapy loads all spiders even if its not the one you named
        allowed_domains = [urlparse(start_urls[0]).hostname]

    rules = [
        Rule(
            # rule for exhibitor detail link
            LinkExtractor(
                allow=(
                    u'\/(eBooth.aspx\?)',
                ),
            ),
            callback='parse_item',
            follow=False,  # no further info needed, stop at this page
        ),
    ]

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

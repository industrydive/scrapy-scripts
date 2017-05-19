from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import HrTech2017Exhibitor
from bs4 import BeautifulSoup


class HrTech2017(CrawlSpider):
    ''' Spider for HR Technology Conference 2017
        https://industrydive.atlassian.net/browse/TECH-1623
    '''

    name = "hrtech2017"
    allowed_domains = ["s23.a2zinc.net"]
    start_urls = ["http://s23.a2zinc.net/clients/lrp/hrtechnologyconference2017/Public/exhibitors.aspx?Index=All"]

    rules = [
        Rule(
            # article page
            # follow links on this page
            LinkExtractor(
                allow=(
                    u'\/(clients/lrp/hrtechnologyconference2017/Public/eBooth.aspx\?)',
                ),
            ),
            callback='parse_item',
            follow=False,
        ),
    ]

    # handle an article page here
    def parse_item(self, response):
        item = HrTech2017Exhibitor()
        html = BeautifulSoup(response.body, "html.parser")
        item['exhibitor_name'] = html.find('div', {'id': 'eboothContainer'}).find('h1').text
        contact_url_obj = html.find('a', {'id': 'BoothContactUrl'})
        if contact_url_obj:
            item['website_url'] = contact_url_obj.text
        # needs to be yield or else PipeLine.process_item() doesn't get called
        yield item

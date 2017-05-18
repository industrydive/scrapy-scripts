from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import HrTech2017Exhibitor


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
            callback='parse_exhibitor_detail',
            follow=False,
        ),
    ]

    # handle an article page here
    def parse_exhibitor_detail(self, response):
        item = HrTech2017Exhibitor()
        item.process(response)
        return item

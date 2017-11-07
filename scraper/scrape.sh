#! /bin/bash
# A wrapper script for running a generic tradeshow scrape against 
# scraper.spiders.generic_tradeshow_spider.TradeShowSpider
# outputs CSV results into tradeshow-scrape.csv
# usage example:
# ./scrape.sh http://s23.a2zinc.net/clients/lrp/hrtechnologyconference2017/Public/exhibitors.aspx?Index=All

if [[ $# -eq 0 ]] ; then
    echo 'provide a start URL. usage:'
    echo ' ./scrape.sh [start-url]'
    exit 0
fi

echo "scraping $1"
rm -f -- tradeshow-scrape.csv
scrapy crawl tradeshow --output=tradeshow-scrape.csv --output-format=csv --set=start_url=$1
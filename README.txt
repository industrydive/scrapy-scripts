Getting started
============================
Create and activate a python virtual environment
Install requirements:
$ pip install -r requirements.txt


Running a Tradeshow Scrape
============================
For the most part, the generic spider at
scraper/spiders/generic_tradeshow_spider.py should be able to handle most
scraping requests that we get.

If you need to scrape something that follows the same format as sites like

http://s23.a2zinc.net/clients/lrp/hrtechnologyconference2017/Public/exhibitors.aspx?Index=All
or
http://events.pennwell.com/DTECH2018/Public/exhibitors.aspx?_ga=2.91461086.575732828.1507662078-248451487.1507662078

then you should be able to use this as-is by running the command:
scrapy crawl tradeshow --output=<name-your-file>.csv --output-format=csv --set=start_url=<your-start-url>

Otherwise, you may need to create a custom spider like in nrf2018_custom_spider.py


Scrapy Basics
============================

Callback functions
----------------------------
Each Rule should have a callback function
created for it - this is what will be executed on the HTML of a resulting
page when scrapy follows a link.

Items
----------------------------
For each type of item you need to capture information about, add an Item
to scraper/items.py. This is where you define the fields you want to
store data in for each item and how to populate those fields. Your
Rule callback functions should invoke these items.

Running a scraper
============================
$ cd scraper
$ scrapy crawl nameofyourspider \
  --output=location-of-output-file --output-format=[csv,jl,etc]

example:
$ scrapy crawl hrtech2017 --output-format=csv --output=hrtech2017.csv

For more details and tutorials, see the scrapy documentation:
https://doc.scrapy.org/

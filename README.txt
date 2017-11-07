Getting started
============================
Create and activate a python virtual environment
Install requirements:
$ pip install -r requirements.txt


Running a Tradeshow Scrape
============================
For the most part, the generic spider at
scraper/spiders/generic_tradeshow_spider.py should be able to handle most
scraping requests that we get. If this is the case, you can use the scrape.sh
wrapper script by passing it the exhibitor list page URL, like:
$ ./scrape.sh http://s23.a2zinc.net/clients/.../exhibitors.aspx?Index=All

This will write CSV output to a file called tradeshow-scrape.csv
If tradeshow-scrape.csv already exists, it will overwrite it


If a request comes in for a page that doesn't match the generic tradeshow
site format and you need to add a new spider, do so by creating one like
scraper/spiders/whatever_your_custom_spider.py



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

Getting started
============================
Create and activate a python virtual environment
Install requirements:
$ pip install -r requirements.txt


Creating a scraper
============================
Spiders
----------------------------
Add a news spider to scraper/spiders/__init__.py

Give it a class name that makes it clear what it is intended to be used
for

Give it a name property that you will use to call it on the commans line

Give it the appropriate allowed_domain & start_urls, as well as rules
for links it should follow.

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

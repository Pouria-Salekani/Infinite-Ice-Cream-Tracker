# Infinite Ice Cream Tracker

A website made using Python and Django that takes ice cream flavors of a local ice cream shop and updates my personal inventory *automatically* with newly added flavors and notifies me when done so.

The heavy lifting is done by a bot that runs serverlessly and scrapes the data automatically at scheduled intervals (bot not included here on GitHub).
<br>
Here is the ``bot.py`` that scrapes the data auatomatically which is deployed on Heroku:

```python
from collections import defaultdict
import scrapy
import requests

class IceCreamSpider(scrapy.Spider):
    name = 'ice_cream'

    start_urls = [
        'https://saltandstraw.com/pages/flavors'
    ]

    def __init__(self, name=None, **kwargs):
       super().__init__(name, **kwargs)
       self.data = defaultdict(list)



    def parse(self, response):
        #only interested in west coast flavors
        west = response.css('div#west_coast')
        special_flavor_list = []

        for flavor in west.css('div.flavorItem'):
          title = flavor.css('div.flavorItemTitle::text').get()

          #always a constant
          if title == 'Sea Salt w/ Caramel Ribbons':
            yield scrapy.Request(url=response.url, callback=self.parse_standard_flavors, meta={'special_flavor':special_flavor_list})
            break
          
          special_flavor_list.append(title)
          self.data['special_flavors'].append(title)
        

        
    #this will parse the standard flavors only
    def parse_standard_flavors(self, response):
        west = response.css('div#west_coast')
        special_flavor = response.meta['special_flavor']

        titles = [title.css('::text').get() for title in west.css('div.flavorItem div.flavorItemTitle')]

        for title in titles[len(special_flavor):]:
            self.data['standard_flavors'].append(title)

        urls = [redacted]
        
        for u in urls:
            responsive = requests.post(url=u, json=self.data)
 ```
 
 
 The bot then sends a **POST** request and then my Django program will decode the request and display the newly added flavors while removing the old ones that are not in stock anymore.
          

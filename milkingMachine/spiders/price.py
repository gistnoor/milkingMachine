import datetime
from scrapy import Spider, Item, Field
from scrapy.http import Request

from milkingMachine.items import MilkingmachineItem

class Price(scrapy.Spider):
    name = "price"
    allowed_domains = ["amazon.com"]
    start_urls = (
        "http://amazon.com"
    )

    def __init__(self, item_id=""):
        self.item_id = item_id
        listing_url = 

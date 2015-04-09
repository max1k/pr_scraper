
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
#from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import Join
from scrapy.selector import HtmlXPathSelector

from price_scraper.items import SSDItem

class SSDSpider(CrawlSpider):
    name='ssdspider'
    allowed_domains='citilink.ru'
    start_urls = ["http://www.citilink.ru/catalog/computers_and_notebooks/hdd/ssd_in/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('?p\d+')), follow=True),
        Rule(SgmlLinkExtractor(allow=('\d+')), callback='parse_item'),
    )

    def parse_item(self, response):

        l = ItemLoader(item=SSDItem(), response=response)
        #l.add_xpath('name', '//td[@id="content"]/h1/text()')
        #l.add_xpath('price','')
        #l.add_value('url', response.url)

        return l.load_item()
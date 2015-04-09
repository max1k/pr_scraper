import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.loader import ItemLoader

from price_scraper.items import SSDItem

class SSDSpider(CrawlSpider):
    name='ssdspider'
    allowed_domains=['citilink.ru']
    start_urls = ["http://www.citilink.ru/catalog/computers_and_notebooks/hdd/ssd_in/"]

    rules = (
        Rule(LxmlLinkExtractor(allow=('\?p=\d+$')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        t_cl_item=response.xpath('//table[@class="item"]')
        
        for t in t_cl_item:
            l = ItemLoader(item=SSDItem(), selector=t)
            l.add_xpath('name', './/td[@class="l"]/a/text()')
            l.add_xpath('usual_price', './/div[@class="price"]/text()')
            l.add_xpath('club_price', './/div[@class="price club_price"]/text()')
            l.add_xpath('img_url', './/div[@class="photo"]/span/img/@src')
            l.add_xpath('url', './/td[@class="l"]/a/@href')
            yield l.load_item()

    def parse_start_url(self, response):
        '''
        Crawl start_urls
        '''

        return self.parse_item(response)
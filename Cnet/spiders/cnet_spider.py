from scrapy.spider import Spider
from scrapy.selector import Selector
from Cnet.items import CnetItem
class CnetSpider(Spider):
    name = "cnet"
    allowed_domains = ["www.cnet.com"]
    start_urls = [
		"http://www.cnet.com/topics/phones/products/?filter=manufacturer_samsung&page=%d" % d for d in range (0,13)
    ]

    def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//section[@class="searchItem product"]')
		items = []
		for site in sites:
			item = CnetItem()
			item['title'] = site.xpath('div/a/h3/text()').extract()
			item['title'] = [x.strip() for x in item['title']]
			item['link'] = site.xpath('div/a/@href').extract()
			item['link'] = [x.strip() for x in item['link']]
			item['desc'] = site.xpath('div/p/text()').extract()
			item['desc'] = [x.strip() for x in item['desc']]
			item['image'] = site.xpath('a/figure/img/@src').extract()
			items.append(item)
		return items

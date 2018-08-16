import scrapy 
from Rice.items import RiceItem

class RiceSpider(scrapy.Spider):

	name = 'rice'

	start_urls = ['https://ccl.rice.edu/partners/current-partners-programs/partners/']

	def parse(self,response):	

		for sel in response.xpath('//tr/td/p/a[contains(@href,"http")]'):

			item = RiceItem()
			item['NPO_Name'] = sel.xpath('./text()').extract_first()
			item['Website'] = sel.xpath('./@href').extract_first()

			request = scrapy.Request(sel.xpath('./@href').extract_first(),callback=self.parse_item)
			request.meta['item'] = item	

			yield request

	def parse_item(self,response):

		item = response.meta['item']

		item['Facebook'] = response.xpath('//a[contains(@href,"facebook")]/@href').extract_first()
		item['Twitter'] = response.xpath('//a[contains(@href,"twitter")]/@href').extract_first()

		yield item
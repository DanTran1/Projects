import scrapy 
from SLP.items import SlpItem

class SLP_UA_Spider(scrapy.Spider):

	name = 'slp'

	start_urls = ['http://slpro.ua.edu/index.cfm?fuseaction=content.view&section=2&page=2']

	def parse(self,response):

		for sel in response.xpath('//tr/td/a'): 

			item = SlpItem()
			item['NPO_Name'] = sel.xpath('./text()').extract_first()

			org_site = 'http://slpro.ua.edu/' + sel.xpath('./@href').extract_first()

			request = scrapy.Request(org_site,callback = self.parse_item)
			request.meta['item'] = item

			yield request

	def parse_item(self,response):

		item = response.meta['item']

		item['Website'] = response.xpath('//b/text()[contains(.,"Website")]/../../following-sibling::td/a[contains(@href,"http")]/@href').extract_first()
		item['POC'] = response.xpath('//b/text()[contains(.,"Contact Person")]/../../following-sibling::td/text()').extract_first()
		item['Email'] = response.xpath('//b/text()[contains(.,"Email")]/../../following-sibling::td/a[contains(@href,"mailto")]/text()').extract_first()
		item['Phone_Number'] = response.xpath('//b/text()[contains(.,"Phone")]/../../following-sibling::td/text()').extract_first()
		item['About_Us'] = response.xpath('//b/text()[contains(.,"Mission")]/../../following-sibling::td/text()').extract_first()

		Address = response.xpath('//b/text()[contains(.,"Address")]/../../following-sibling::td/text()[position()<3]').extract()
		
		for i in range(len(Address)):

			Address[i] = Address[i].strip()

		item['Address'] = Address


		yield item
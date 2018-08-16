import scrapy 
from StLouisVolunteerCenter.items import StlouisvolunteercenterItem

class StLouisVolunteerSpider(scrapy.Spider):

	name = 'stlouis'

	start_urls = ['file:///Users/Dan/Desktop/Boston%20Cares%20_%20Volunteer%20Opportunities%20Search%20Results.htm']

	def parse(self,response):

		for link in response.xpath('//td[@data-th="Opportunity"]/a/@href').extract():

			yield scrapy.Request(link,dont_filter=True,callback = self.parse_item)


	def parse_item(self,response):

		item = StlouisvolunteercenterItem()

		Opportunity = response.xpath('//h2[@class="title-opportunity"]/text()').extract_first()
		NPO_Name = response.xpath('//a[@class="organization-name"]/text()').extract_first()
		Website = response.xpath('//a[@class="organization-link"]/@href').extract_first()
		POC = response.xpath('//span[@class="inline-element opportunity-leader"]/text()').extract_first()
		POC_Email = response.xpath('//a[@class="email opportunity-leader-email"]/@href').extract_first()

		if POC_Email != None:
			POC_Email = POC_Email.lstrip("mailto:")

		Tags = response.xpath('//span[@class="issue-areas"]/text()').extract_first()

		item = StlouisvolunteercenterItem()
		item['NPO_Name'] = NPO_Name
		item['Website'] = Website
		item['POC_Email'] = POC_Email
		item['POC'] = POC 
		item['Tags'] =Tags
		item['Opportunity'] = Opportunity

		org_link = 'https://www.bostoncares.org' + response.xpath('//a[@class="organization-name"]/@href').extract_first()

		request = scrapy.Request(org_link,dont_filter=True, callback = self.parse_opportunity)

		request.meta['item'] = item

		yield request

	def parse_opportunity(self,response):

		item = response.meta['item']

		# sometimes the about_us in the organization page changes, change it if needed
		About_Us = response.xpath('//p[@class="organization-detail"]/text()').extract_first()
		
		if About_Us != None:
			About_Us = About_Us.strip()

		Address = response.xpath('//span[@class="activity-type"]/text()').extract_first()

		item['About_Us'] = About_Us
		item['Address'] = Address
		item['Facebook'] = response.xpath('//li/a[@class="facebook"]/@href[contains(.,"facebook.com")]').extract_first()
		item['Twitter'] = response.xpath('//li/a[@class="twitter"]/@href[contains(.,"twitter.com")]').extract_first()

		yield item










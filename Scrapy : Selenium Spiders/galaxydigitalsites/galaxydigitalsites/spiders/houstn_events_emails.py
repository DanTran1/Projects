import scrapy 
from galaxy_events.items import GalaxyEventsItem

class VolunteerHouston(scrapy.Spider):

	name = 'houston'

	start_urls = ['https://volunteerhouston.galaxydigital.com/event/',
	'https://volunteerhouston.galaxydigital.com/event/index/12',
	'https://volunteerhouston.galaxydigital.com/event/index/24',
	'https://volunteerhouston.galaxydigital.com/event/index/36']

	def parse(self,response):

		for event in response.xpath('//div[@class="event "]/div[@class="card"]/a/@href').extract():

			yield scrapy.Request(event,callback = self.parse_item)

	def parse_item(self,response):

		item = GalaxyEventsItem()

		item['POC'] = response.xpath('//tr[@class="name"]/td[@class="text"]/text()').extract_first()
		item['Phone_Number'] = response.xpath('//tr[@class="phone"]/td[@class="text"]/text()').extract_first()
		item['Email'] = response.xpath('//tr[@class="email"]/td[@class="text"]/a[contains(@href,"mailto")]/@href').extract_first()

		npo_link = 'https://volunteerhouston.galaxydigital.com' + response.xpath('//div[@class="agency "]/div[@class="card"]/a/@href').extract_first()
		request = scrapy.Request(npo_link,callback=self.parse_npolink)

		request.meta['item'] = item

		yield request

	def parse_npolink(self,response):


		item = response.meta['item']

		item['NPO_Name'] = response.xpath('//h1[@class="panel-title"]/text()').extract_first()

		yield item
import scrapy

class BloomingtonEventSpider(scrapy.Spider):

	name = 'bloomington_event'

	start_urls = ['http://www.bloomingtonvolunteernetwork.org/need/']

	def parse(self,response):

		for event in response.xpath('//tr[@class="need "]/td[@class="details"]/a/@href').extract():

			yield scrapy.Request(event, callback = self.parse_item)


	def parse_item(self,response):

		address = response.xpath('//tr[@class="address"]/td[@class="text"]/text()').extract()

		yield_address = []

		for addy in address:

			clean_address = str(addy).strip()
			yield_address.append(clean_address)

		yield {


		'Event Address': yield_address,
#		there is a skills tag, try to split them and do two different columns
#		'Interest tags': response.xpath('//li[@class="interest"]/div[contains(@class,"icon-wrap")]/svg[contains(@class,"icon interest-icon")]/@title').extract(),
		'NPO name': response.xpath('//div[@class="card"]/a/div[@class="title"]/text()').extract_first(),
		'Date': (response.xpath('//td[@class="info-block date"]/div[@class="info"]/text()').extract()).strip(),
		'Time': (response.xpath('//td[@class="info-block time"]/div[@class="info"]/text()').extract_first()).strip()


		}


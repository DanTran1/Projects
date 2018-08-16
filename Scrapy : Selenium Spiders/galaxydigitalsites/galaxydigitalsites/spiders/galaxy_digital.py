import scrapy

class GalaxyDigitalSpider(scrapy.Spider):

	name = 'galaxy'

	#for galaxy digital websites just change the url and index

	url = 'http://www.handsonasheville.org/agency/'

	start_urls = ['http://www.handsonasheville.org/agency/']

	for i in range(1,7):

		i = i * 12

		new_url = url + "index/" + str(i) 

		start_urls.append(new_url)


	def parse(self,response):


		for org in response.xpath('//div[@class="agency "]/div[@class="card"]/a/@href').extract():

			yield scrapy.Request(org,callback=self.parse_item)


	def parse_item(self,response):

		address = response.xpath('//tr[@class="address"]/td[@class="text"]/text()[normalize-space()]').extract()

		address_list = []

		for addy in address:

			new_addy = str(addy).strip()

			address_list.append(new_addy)

		yield {

		'NPO Name': response.xpath('//h1[@class="panel-title"]/text()').extract_first(),
		'Phone number': response.xpath('//tr[@class="phone"]/td[@class="text"]/text()').extract_first(),
		'Email': response.xpath('//tr[@class="email"]/td[@class="text"]/a/text()').extract_first(),
		'POC': response.xpath('//tr[@class="contact"]/td[@class="text"]/text()').extract_first(),
		'POC Title': response.xpath('//tr[@class="contact-title"]/td[@class="text"]/text()').extract_first(),
		'Address': address_list,
		'Website': response.xpath('//tr[@class="website"]/td[@class="text"]/a/@href').extract_first(),
		'Facebook': response.xpath('//tr[@class="facebook"]/td[@class="text"]/a/@href').extract_first(),
		'Twitter': response.xpath('//tr[@class="twitter"]/td[@class="text"]/a/@href').extract_first(),
		'Who We Are': response.xpath('//section[@class="description"]/div[@class="section-inner"]/h4[text()="Who We Are"]/following-sibling::div[1]/p/text()').extract_first(),
		'What We Do': response.xpath('//section[@class="description"]/div[@class="section-inner"]/h4[text()="What We Do"]/following-sibling::div[1]/p/text()').extract_first(),
		'Causes': response.xpath('//svg[contains(@class,"icon cause-icon")]/@title').extract()


		}
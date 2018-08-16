import scrapy 

class GalaxySpider(scrapy.Spider):

	name = 'galaxy2'

	url = 'https://auw.galaxydigital.com/volunteer/agency/'

	start_urls = ['https://auw.galaxydigital.com/volunteer/agency/']

	for i in range(1,30):

		i = i * 10

		new_url = url + "index/" + str(i)

		start_urls.append(new_url)

	def parse(self,response):

		for org in response.xpath('//div[@class="agencyDetails"]/a[@class="agencyName"]/@href').extract():

			page = 'https://auw.galaxydigital.com' + org

			yield scrapy.Request(page, callback = self.parse_item)

	def parse_item_helper(self,item):

		try: 

			item_strip = item.strip()
			
		except AttributeError:

			item_strip = item

		return item

	def parse_address_helper(self,address):

		if len(address) != 0:

			for i in range(len(address)):

				address[i] = address[i].strip()

		return address

	def parse_item(self,response):

		poc = response.xpath('//div[@class="inner"]/strong[text()="Contact:"]/following-sibling::text()[1]').extract_first()
		poc_strip = self.parse_item_helper(poc)
		poc_title = response.xpath('//div[@class="inner"]/strong[text()="Contact Title:"]/following-sibling::text()[1]').extract_first()
		poc_title_strip = self.parse_item_helper(poc_title)
		poc_phone = response.xpath('//div[@class="inner"]/strong[text()="Phone:"]/following-sibling::text()[1]').extract_first()
		poc_phone_strip = self.parse_item_helper(poc_phone)
		email = response.xpath('//div[@class="inner"]/strong[text()="Email:"]/following-sibling::text()[1]').extract_first()
		email_strip = self.parse_item_helper(email)
		address = response.xpath('//div[@class="inner"]/strong[text()="Address Information"]/following-sibling::text()[position()<3]').extract()

		if "FL" not in address:

			address = response.xpath('//div[@class="inner"]/strong[text()="Address Information"]/following-sibling::text()[position()<4]').extract()

		address_strip = self.parse_address_helper(address)

		yield {

		'NPO Name': response.xpath('//h1/text()').extract_first(),
		'Who We Are': "",
		'What We Do': "",
		'POC': poc_strip,
		'POC Title': poc_title_strip,
		'Email': email_strip,
		'POC Phone': poc_phone,
		'Website': response.xpath('//div[@class="inner"]/strong/a[text()="Visit our Website"]/@href').extract_first(),
		'Twitter': response.xpath('//div[@class="inner"]/strong/a[text()="Follow us on Twitter"]/@href').extract_first(),
		'Facebook': response.xpath('//div[@class="inner"]/strong/a[text()="Visit our Facebook Page"]/@href').extract_first(),
		'Address': address_strip,
		'Causes': ""
		}
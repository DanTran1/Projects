import scrapy 

class WilliamsburgSpider(scrapy.Spider):

	name = 'william'

	start_urls = ['http://www.volunteerwilliamsburg.org/login.php']

	def parse(self,response):

		return scrapy.FormRequest.from_response(
			response,
			formdata={'username':'geohu123','passcode':'123test123'},
			callback = self.after_login)

	def after_login(self,response):

		url_list = [

		'http://www.volunteerwilliamsburg.org' + response.xpath('//a[@class="link_browse_listings"]/@href').extract_first(),
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=1',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=2',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=3',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=4',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=5',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=6',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=7',
		'http://www.volunteerwilliamsburg.org/volunteer/volunteer-listings.php?pageNum_rsListings=8'

		]

		for url in url_list:

			yield scrapy.Request(url,callback=self.parse_item)

	def parse_item(self,response):

		for link in response.xpath('//a[@class="link_special"]/@href|//a[@class="link_details"]/@href').extract():

			opportunity_url = 'http://www.volunteerwilliamsburg.org/volunteer/' + link
			yield scrapy.Request(opportunity_url,callback = self.parse_opportunity)

	def parse_opportunity(self,response):

		Address_list = response.xpath('//div[@id="content"]/p[1]/text()[1]|//div[@id="content"]/p[1]/text()[2]').extract()

		if len(Address_list) >= 1:
			for i in range(len(Address_list)):
				Address_list[i] = Address_list[i].strip()
		else:
			Address_list = None

		yield{

		'Opportunity Name': response.xpath('//h2[2]/text()').extract_first(),
		'Email': response.xpath('//a[contains(@href,"mailto")]/text()').extract_first(),
		'Website': response.xpath('//a[contains(@href,"http")]/@href').extract_first(),
		'Address': Address_list,
		'NPO Name': response.xpath('//p[1]/strong/text()').extract_first()

		}	
			
import scrapy

class AmplifySpider(scrapy.Spider):
	name = "amplify"

	start_urls = [

				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=39',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=40',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=41',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=42',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=43',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=44',
				'https://amplifyatx.ilivehereigivehere.org/nonprofits?=undefined&search_keywords=&search_category=Show%20All&search_officeLocation=0&organizations_id=&page=45'
			
				]
	def parse(self,response):

		for npo_page in response.css('div.searchItemContent a::attr(href)').extract():

			npo_page = response.urljoin(npo_page) + '/overview'
			yield scrapy.Request(npo_page,callback=self.parse_item)

	def parse_item(self,response):

		yield {

			'Name': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/dl/dd[1]/text()').extract_first(),
			'Email': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/dl/dd[4]/a/text()').extract_first(),
			'Phone Number': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[2]/dl/dd[1]/text()').extract_first(),
			'Website': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/dl/dd[3]/a/text()').extract_first(),
			'IRS EIN': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/dl/dd[2]/text()').extract_first(),
			'Address': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[2]/div[2]/dl/dd[2]/text()').extract(),
			'Facebook': response.css('div.span3 a.facebook-icon::attr(href)').extract_first(),
			'Twitter': response.css('div.span3 a.twitter-icon::attr(href)').extract_first(),
			'Instagram': response.css('div.span3 a.instagram-icon::attr(href)').extract_first(),
#			'Mission Statement': response.xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div/div[3]/div/text()').extract_first()


		}	

			

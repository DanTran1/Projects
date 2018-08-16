import scrapy
from calstate_2.items import Calstate2Item

class CalStateSpider(scrapy.Spider):

	name = 'calstate_2'

	start_urls = ['https://app.calstates4.com/cpp/sites?title_op=contains&title=&field_prog_site_address_locality=&combine_1=&items_per_page=All']

	def parse(self,response):

		# change this back to "extract()" for complete scraping

		for url in response.xpath('//div[@class="col-sm-8 left "]/h3/a/@href').extract():

			new_url = 'https://app.calstates4.com' + str(url)

			yield scrapy.Request(new_url,callback = self.parse_item)
		

	def parse_item(self,response):

		# extract partial url for site staff page, contact info is on here
		site_staff = response.xpath('//li/a[text()="Site staff"]/@href').extract_first()
		site_staff_page = response.urljoin(site_staff)
		# other needed info
		street = response.xpath('//div[@class="thoroughfare"]/text()').extract_first()
		city = response.xpath('//span[@class="locality"]/text()').extract_first()
		state = response.xpath('//span[@class="state"]/text()').extract_first()
		zipcode = response.xpath('//span[@class="postal-code"]/text()').extract_first()
		country = response.xpath('//span[@class="country"]/text()').extract_first()

		# puts everything in a list to output
		address = [street,city,state,zipcode,country]
		address_out = []

		for i in address:
			if i != None:
				address_out.append(i)
			else:
				pass


		# actual dict output
		item = Calstate2Item()
		item['NPO_name'] = response.xpath('//h1[@class="title"]/text()').extract_first()
		item['Address'] = address_out
		item['Website'] = response.xpath('//div[contains(@class,"parent-websites")]/div/a/@href').extract_first()
		item['Main_Phone'] = response.xpath('//div[contains(@class,"telephone")]/div/div/a/text()').extract_first()
		item['General_Email'] = response.xpath('//div[contains(@class,"general-email")]/div/div/a/text()').extract_first()
		item['Description'] = response.xpath('//*[@id="block-system-main"]/div/div/div[1]/div[1]/div[2]/div/div/div/div/p/text()').extract()
		item['Program_Info'] = response.xpath('//*[@id="block-system-main"]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/p/text()').extract()

		request = scrapy.Request(site_staff_page,callback = self.staff_info)

		request.meta['item'] = item

		yield request


 	def staff_info(self,response):

 		item = response.meta['item']
 		# clean up "poc_title" data for csv
 		title = response.xpath('//td[contains(@class,"staff-role")]/text()').extract_first()
 		try:
 			poc_title = title.strip()
 			item['POC_Title'] = poc_title
 		except AttributeError:
 			pass	
 		item['First_name'] = response.xpath('//td[contains(@class,"first-name")]/a/text()').extract_first()
 		item['Last_name'] = response.xpath('//td[contains(@class,"last-name")]/a/text()').extract_first()	
 		item['POC_Email'] = response.xpath('//td[contains(@class,"email-address")]/a/text()').extract_first()
 		item['POC_Phone_Number'] = response.xpath('//td[contains(@class,"staff-phone")]/a/text()').extract_first()
 		yield item
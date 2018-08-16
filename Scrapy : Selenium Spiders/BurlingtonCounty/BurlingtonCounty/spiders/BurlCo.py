import scrapy

class BurlCoSpider(scrapy.Spider):

	name = 'burlco'

	# add a-z behing glossary after test run
	start_urls = ['http://vcbc.burlco.org/glossary/z']


	def parse(self,response):

		# extracts the href link
		for org in response.xpath('//td[@class="views-field views-field-title active"]/a/@href').extract():
			# add href link to website to get to org site
			org_site = 'http://vcbc.burlco.org' + org
			# crawls org site
			yield scrapy.Request(org_site,callback = self.parse_item)

	def parse_item(self,response):

		name = response.xpath('//*[@id="page-title"]/text()').extract_first()

		# clean up npo name 
		if name != None:
			NPO_name = name.strip()
		else:
			NPO_name = name

		about = response.xpath('//div[@class="field-items"]/div[@class="field-item even"]/p/text()').extract_first()

		numbers =[]
		for i in range(0,10):
			numbers.append(str(i))

		phone_number = []

		if about != None:

			about_split = about.split()
			print(about_split)
			for j in about_split:
				j_split = j.split()
				print(j_split)
				for k in j_split: 
					for num in numbers:
						if num in k:
							phone_number.append(j)
							break

		for num in phone_number:

		# 	if len(num) <3:
		# 		list.remove(num)

		 	if ":" in num:
		 		list.remove(num)

	
		yield {

		'NPO Name': NPO_name,
		'Website': response.xpath('//div[@class="field-items"]/div[@class="field-item even"]/p/a[contains(@href,"http")]/text()').extract_first(),
		'Email': response.xpath('//div[@class="field-items"]/div[@class="field-item even"]/p/a[contains(@href,"mailto")]/text()').extract_first(),
		'Tags': response.xpath('//li[contains(@class,"field-item")]/a/text()').extract(),
		'Phone Number': phone_number,
		'About Us': about
		}



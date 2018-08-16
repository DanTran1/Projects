import scrapy 

class AubernServesSpider(scrapy.Spider):

	name = 'aubern'

	start_urls = ['https://auburnserves.com/Partner']

	url = 'https://auburnserves.com/Partner?searchString=&InterestFilter=&Page='

	for n in range(2,20):

		page = url + str(n)

		start_urls.append(page)


	def parse(self,response):

		for link in response.xpath('//div[@class="participantEventList"]/h3/a/@href').extract():

			partner_page = 'https://auburnserves.com' + link

			yield scrapy.Request(partner_page,callback=self.parse_item)

	def parse_item(self,response):

		npo_name = response.xpath('//h2/text()').extract_first()

		if npo_name != None:

			npo_name = npo_name.strip()


		name_title = response.xpath('//div[@class="contact"]/text()').extract_first()

		if name_title != None:

			name_title = name_title.strip()
			name_title = name_title.split(",")
			name = name_title[0]
			title = name_title[1]

		if "N/A" in name:

			name = None

		if "N/A" in title:

			title = None

		address_list = response.xpath('//div[@class="address"]/text()').extract()

		if len(address_list) != 0:

			for i in range(len(address_list)):

				address_list[i] = address_list[i].strip()

		contact_list = response.xpath('//div[@class="contact"]/text()').extract()

		if len(contact_list) != 0:

			for j in range(len(contact_list)):

				contact_list[j] = contact_list[j].strip()

		if "fax" not in contact_list[3]:

			phone = contact_list[3]

			if "(Preferred)" in phone:

				phone = phone.rstrip("(Preferred)")

		else:

			phone = None 

		tags_list = response.xpath('//div[@class="tags"]/span[@class="label labeler"]/text()').extract()

		if len(tags_list) != 0:

			for k in range(len(tags_list)):

				tags_list[k] = tags_list[k].strip()

		email = response.xpath('//div[@class="contact"]/a/text()[contains(.,"@")]').extract_first()

		if (email != None) and ("(Preferred)" in email):

			email = email.rstrip("(Preferred)")

		yield {

		'NPO Name': npo_name,
		'Tags': tags_list,
		'POC Email': email,
		'Website': response.xpath('//div[@class="website"]/a[contains(@href,"http")]/text()').extract_first(),
		'POC': name,
		'POC Title': title,
		'About Us': response.xpath('//div[@class="website"]/following-sibling::div/p/text()').extract_first(),
		'Address': address_list,
		'Phone': phone

		}





import scrapy

class UclaSpider(scrapy.Spider):

	name = 'ucla'

	start_urls = ['http://volunteer.ucla.edu/volunteer']

	def parse(self,response):

		for name in response.css('div.side a::attr(href)').extract():

			npo_page = 'http://volunteer.ucla.edu' + name

			yield scrapy.Request(npo_page,callback=self.parse_item)


	def parse_item(self,response):

		yield {
			'Event Name': response.xpath('//*[@id="article"]/h1/text()').extract_first(),
			'NPO Name': response.xpath('//*[@id="aboutOrg"]/p[text()="Organization: "]/strong/text()').extract_first(),
			'POC Name': response.xpath('//*[@id="aboutOrg"]/p[text()="Contact Person: "]/strong/text()').extract_first(),
			'POC Phone Number': response.xpath('//*[@id="aboutOrg"]/p[text()="Contact Phone Number: "]/strong/text()').extract_first(),
			'Address': response.xpath('//p[@class="postOppItem"]/text()[contains(normalize-space(),"Location")]/following-sibling::strong/text()').extract_first(),
			'Duration': response.xpath('//p[@class="postOppItem"]/text()[contains(normalize-space(),"Duration")]/following-sibling::strong/text()').extract_first(),
			'Date': response.xpath('//p[@class="postOppItem"]/text()[contains(normalize-space(),"Date") or contains(normalize-space(),"First Day")]/following-sibling::strong/text()').extract(),
			'Email': response.xpath('//*[@id="aboutOrg"]/p/strong/a[starts-with(@href,"mailto")]/text()').extract_first(),
			'Website': response.xpath('//*[@id="aboutOrg"]/p/a[starts-with(@href,"http")]/@href').extract_first(),
			'Facebook': response.xpath('//*[@id="aboutOrg"]/p/a[starts-with(@href,"https://www.facebook.com")]/@href').extract_first(),
			'Twitter': response.xpath('//*[@id="aboutOrg"]/p/a[starts-with(@href,"https://twitter.com")]/@href').extract_first(),
			'Tags': response.xpath('//*[@id="article"]/div[@class]/a[starts-with(@href,"/volunteer/#search")]/text()').extract()
		}

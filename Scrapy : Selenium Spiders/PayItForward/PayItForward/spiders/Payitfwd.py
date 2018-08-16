import scrapy 
from PayItForward.items import PayitforwardItem

class PayItForwardSpider(scrapy.Spider):

	name = 'payitforward'

	start_urls = [
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%201_files/Pay%20It%20Forward%201.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%202_files/Pay%20It%20Forward%202.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%203_files/Pay%20It%20Forward%203.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%204_files/Pay%20It%20Forward%204.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%205_files/Pay%20It%20Forward%205.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%206_files/Pay%20It%20Forward%206.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%207_files/Pay%20It%20Forward%207.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%208_files/Pay%20It%20Forward%208.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%209_files/Pay%20It%20Forward%209.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2010_files/Pay%20It%20Forward%2010.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2011_files/Pay%20It%20Forward%2011.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2012_files/Pay%20It%20Forward%2012.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2013_files/Pay%20It%20Forward%2013.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2014_files/Pay%20It%20Forward%2014.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2015_files/Pay%20It%20Forward%2015.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2016_files/Pay%20It%20Forward%2016.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2017_files/Pay%20It%20Forward%2017.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2018_files/Pay%20It%20Forward%2018.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2019_files/Pay%20It%20Forward%2019.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2020_files/Pay%20It%20Forward%2020.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2021_files/Pay%20It%20Forward%2021.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2022_files/Pay%20It%20Forward%2022.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2023_files/Pay%20It%20Forward%2023.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2024_files/Pay%20It%20Forward%2024.htm',
	'file:///Users/Dan/Desktop/Pay%20It%20Forward%2025_files/Pay%20It%20Forward%2025.htm'
	]

	def parse(self,response):

		for org_link in response.xpath('//div[@class="orgLink"]/a/@href').extract():

			yield scrapy.Request(org_link,callback = self.parse_item)


	def parse_item(self,response):
		# needs to be cleaned
		Tags = response.xpath('//ul[@class="tagList spaceAfter"]/li/a/text()').extract()

		i = 0
		while i < len(Tags):
			Tags[i] = self.clean_data(Tags[i])
			i += 1
		# needs to be cleaned
		About_Us = response.xpath('//h4[contains(text(),"Description")]/following-sibling::p/text()').extract_first()

		About_Us = self.clean_data(About_Us)
		# needs to be cleaned
		Address = response.xpath('//h4[contains(text(),"Organization")]/following-sibling::p[1]/text()[2]|//h4[contains(text(),"Organization")]/following-sibling::p[1]/text()[3]').extract()

		j = 0
		while j < len(Address):
			Address[j] = self.clean_data(Address[j])
			j += 1

		Website = response.xpath('//h4[contains(text(),"Web")]/following-sibling::p/a[contains(@href,"http")]/@href').extract_first()
		# needs to be cleaned
		NPO_Name = response.xpath('//div[@class="spaceAfter"]/h2/text()').extract_first()

		NPO_Name = self.clean_data(NPO_Name)
		# needs to be cleaned
		Phone_Number = response.xpath('//h4[contains(text(),"Contact Person")]/following-sibling::p/text()[2]').extract_first()	

		Phone_Number = self.clean_data(Phone_Number)
		# needs to be cleaned
		POC = response.xpath('//h4[contains(text(),"Contact Person")]/following-sibling::p/text()[1]').extract_first()

		POC = self.clean_data(POC)

		Email = response.xpath('//h4[contains(text(),"Contact Person")]/following-sibling::p/a/text()').extract_first()

		item = PayitforwardItem()

		item['Tags'] = Tags
		item['NPO_Name'] = NPO_Name
		item['About_Us'] = About_Us
		item['Website'] = Website
		item['Phone_Number'] = Phone_Number
		item['POC'] = POC
		item['Address'] = Address
		item['Email'] = Email

		yield item


	def clean_data(self,data):

		if data != None:
			data = data.strip()

		return data
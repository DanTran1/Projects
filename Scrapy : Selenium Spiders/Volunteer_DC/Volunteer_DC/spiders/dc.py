import scrapy
from Volunteer_DC.items import VolunteerDcItem

class VolunteerDcSpider(scrapy.Spider):

	name = 'dc'

	start_urls = [

	'https://onegooddeedchicago.org/organizations/',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=2',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=3',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=4',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=5',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=6',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=7',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=8',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=9',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=10',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=11',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=12',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=13',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=14',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=15',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=16',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=17',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=18',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=19',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=20',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=21',
	'https://onegooddeedchicago.org/organizations/index.php?sort_mode=title_asc&max_records=10&list_page=22'

	]

	def parse(self,response):

		for sel in response.xpath('//tr/td[@width="33%"]/a'):

			item = VolunteerDcItem()

			item['NPO_Name'] = sel.xpath('./text()').extract_first()

			link = 'https://onegooddeedchicago.org' + sel.xpath('./@href').extract_first()

			request = scrapy.Request(link,callback = self.parse_item)

			request.meta['item'] = item

			yield request

 	def parse_item(self,response):

 		item = response.meta['item']

 		website = response.xpath('//div[@class="orginfo"]/strong[contains(text(),"website:")]/following-sibling::a/@href[contains(.,"http")]').extract_first()
 		item['Website'] = website
 		item['Description'] = response.xpath('//h3[contains(text(),"Description & History")]/following-sibling::div/p/span/text()').extract_first()
 		item['POC'] = response.xpath('//*[contains(text(),"Contact:")]/following-sibling::div[@class="repinfo"]/text()').extract_first()
 		item['POC_Title'] = response.xpath('//*[contains(text(),"Contact:")]/following-sibling::div[@class="repinfo"]/span/text()').extract_first()
 		item['Address'] = response.xpath('//div[@class="address"]/a/text()').extract()

 		if website != None:

 			npo_website = scrapy.Request(website,callback = self.parse_item2)

 			npo_website.meta['item'] = item

 			yield npo_website

 		else:

 			yield item

 	def parse_item2(self,response):

 		item = response.meta['item']

 		item['Facebook'] = response.xpath('//a[contains(@href,"facebook.com")]/@href').extract_first()
 		item['Twitter'] = response.xpath('//a[contains(@href,"twitter.com")]/@href').extract_first()

 		yield item


import scrapy 

class JustServeSpider(scrapy.Spider):

	name = 'justserve'

	start_urls = ['https://www.stlvolunteer.org/search?page=28&sort_c=&sort_o=&opportunity_id=']

	def parse(self,response):

		return scrapy.FormRequest.from_response(
			response,
			formdata={'searchvo_zip':'63101','searchvo_distance':'Any'},
			callback = self.parse_item)

	def after_login(self,response):

		if 
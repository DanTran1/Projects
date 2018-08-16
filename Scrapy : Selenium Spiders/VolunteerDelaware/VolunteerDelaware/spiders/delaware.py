import scrapy 

class VolunteerDelaware(scrapy.Spider):

	name = 'delaware'

	start_urls = ['http://www.volunteerdelaware.org/HOC__Volunteer_Opportunity_Search_Page?p=vct']

	def parse(self,response):

		for url in response.xpath('//a[@class="opps"]/@href').extract():

			yield {
			'URL': url
			}
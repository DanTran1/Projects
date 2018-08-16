import scrapy 
from scrapy.selector import Selector
from selenium import webdriver
import time
from OrgSync.items import OrgsyncItem

class OrgSyncSpider(scrapy.Spider):

	# name spider
	name = 'orgsync'

	# change the start url as needed for all of the org sync websites
	start_urls = ['https://orgsync.com/892/community/opportunities/partners']

	def __init__(self):

		# open up the testing browser
		self.driver = webdriver.Chrome()

	def parse(self,response):

		# navigates to the given url, will wait until the page loads.. unless its ajax heavy
		self.driver.get(response.url)
		# let the script sleep
		time.sleep(3)
		# find buttons to click
		next_buttons = self.driver.find_elements_by_xpath('//button[@class="osw-button"]')
		# an empty list to append links of NPOs 
		site_links = []

		for button in next_buttons:

			try: 
				# clicks the button
				button.click()
				# scroll down
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				# give 1 second for javascript to load
				time.sleep(1)
				# selects the response for the button clicked pages
				selector = Selector(text=self.driver.page_source)
				# select and extracts the links needed
				bottom_links = selector.xpath('//div[@class="osw-portals-list-item"]/a/@href').extract()

				self.driver.execute_script("window.scrollTo(0, 250);")

				middle_links = selector.xpath('//div[@class="osw-portals-list-item"]/a/@href').extract()

				self.driver.execute_script("window.scrollTo(0, 0);")

				top_links = selector.xpath('//div[@class="osw-portals-list-item"]/a/@href').extract()

				time.sleep(1)

				if len(bottom_links) >= 1:

					for link in bottom_links:

						site_links.append(link)

				if len(middle_links) >= 1:

					for link in middle_links:

						site_links.append(link)
				
				if len(top_links) >= 1:

					for link in top_links:

						site_links.append(link)


				else:

					pass

			except WebDriverException:

				pass

		for link in site_links:

			yield scrapy.Request(link, callback = self.parse_item)		


	def parse_item(self,response):

		self.driver.get(response.url)

		profile_button = self.driver.find_element_by_xpath('//a[@data-tab="profile"]')

		profile_button.click()

		time.sleep(.5)

		selector = Selector(text=self.driver.page_source)

		item = OrgsyncItem()

		Address = selector.xpath('//div[contains(text(),"Organization Address")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		City = selector.xpath('//div[contains(text(),"City")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		State = selector.xpath('//div[contains(text(),"State")]/../following-sibling::div[@class="response"]/p/text()').extract_first()

		Address_list = [Address,City,State]


		# # # # this is if the address has breaklines between the text
		if len(Address_list) > 0:

			i = 0

		 	while i < len(Address_list):

		 		if Address_list[i] != None:

					Address_list[i] = Address_list[i].strip()
					i += 1

				else:

					del Address_list[i]


		# special case 
		# if Address != None:

		# 	Address =  Address + " " + 'Miami, FL'

		# else:

		# 	Address = 'Miami, FL'

		item['Address'] = Address_list
		item['POC'] = selector.xpath('//div[contains(text(),"Name")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		item['Twitter'] = selector.xpath('//div[contains(text(),"Twitter")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		item['Facebook'] = selector.xpath('//a[contains(@href,"facebook.com")]/@href').extract_first()
		item['NPO_Name'] = selector.xpath('//h1/text()').extract_first()
		item['Website'] = selector.xpath('//div[contains(text(),"Website")]/../following-sibling::div[@class="response"]/p/a[contains(@href,"http")]/@href').extract_first()
		item['Email'] = selector.xpath('//div[contains(text(),"Email")]/../following-sibling::div[@class="response"]/p/a[contains(@href,"mailto")]/text()').extract_first()
		item['Phone'] = selector.xpath('//div[contains(text(),"Phone")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		item['Tags'] = selector.xpath('//div[contains(text(),"Category")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		item['About_Us'] = selector.xpath('//div[contains(text(),"Description")]/../following-sibling::div[@class="response"]/p/text()').extract_first()
		yield item










import scrapy

class BlogsSpider(scrapy.Spider):
	name="blogs"
	start_urls = [
		'http://knowledge.wharton.upenn.edu/?s=behaviour economics',
	]
	
	def parse(self, response):
		reading = []
		for page in response.css('a'):
			if len(page.css('a::text').re(r'[a-zA-Z\s:,\']*.Behavioral\sEconomics.*')) > 0:
				reading.append(page.css('a::text'))
		for read in reading:
			print(read.get())
	



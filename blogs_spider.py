import scrapy

class BlogsSpider(scrapy.Spider):
	name="blogs"
	inc = 1
	start_urls = [
		'http://knowledge.wharton.upenn.edu/?s=behavior economics',
	]
	
	def parse(self, response):
		reading = []
		for page in response.css('a'):
			if len(page.css('a::text').re(r'[a-zA-Z\s:,\']*.Economic.*')) > 0:
				reading.append(page.css('a::text'))
		for read in reading:
			print(read.get())	
		BlogsSpider.inc = BlogsSpider.inc + 1
		if BlogsSpider.inc < 20:
			yield scrapy.Request(url='http://knowledge.wharton.upenn.edu/page/'+str(BlogsSpider.inc)+'/?s=behavior+economics',callback=self.parse)	

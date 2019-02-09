import scrapy


class BlogsSpider(scrapy.Spider):
	name="blogs"
	inc = 1
	def __init__(self, *args, **kwargs):
                super(BlogsSpider, self).__init__(*args, **kwargs)
                self.start_urls = ['http://knowledge.wharton.upenn.edu/?s='+self.keywords]

	def writeToFile(self, response):
		try:
			fptr=open('blogs_data.txt','a+')
			data = response.xpath('//div[contains(@class,"article-content")]').get()
			print(type(data))
			fptr.write(data.encode('utf-8'))
			fptr.close()
		except Exception as e:
			print("error",e.message)
			print("error in file open")
			

	def articleWriteToFile(self, url):
		print("article func")
		print(url)
		return scrapy.Request(url = url, callback= self.writeToFile)

	def parse(self, response):
		reading = []
		for page in response.css('a'):
			if len(page.css('a::text').re(r'[a-zA-Z\s:,\']*.Economic.*')) > 0:
				yield self.articleWriteToFile(page.css('a::attr(href)').get())
				reading.append(page.css('a::text'))
		for read in reading:
			print(read.get())	
		BlogsSpider.inc = BlogsSpider.inc + 1
		if BlogsSpider.inc < 20:
			yield scrapy.Request(url='http://knowledge.wharton.upenn.edu/page/'+str(BlogsSpider.inc)+'/?s=behavior+economics',callback=self.parse)	


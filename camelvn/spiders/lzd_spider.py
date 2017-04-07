import scrapy
from pprint import pprint
class LzdSpider(scrapy.Spider):
	name = "Lazada"
	def start_requests(self):
		urls=["http://www.lazada.vn/may-anh-may-quay-phim/"]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self,response):
		homepage = "http://www.lazada.vn";

		for i in response.css('a.c-product-card__name::attr(href)'):
			product_link = homepage + i.extract();
			request =  scrapy.Request(url=product_link, callback=self.parse_product)
			request.meta['product_link'] = product_link
			yield request
	def parse_product(self,response):		
		filename = "abc.txt"
		pd_name = (response.css('h1#prod_title::text').extract_first()).strip()
		sku = (response.css('div.rocket__wishlist-add::attr(data-simple-sku)').extract_first()).strip()
		price = response.css('span#product_price::text').extract_first().strip()
		display_price = response.css('span#special_price_box::text').extract_first().strip()
		origin_price = response.css('span#price_box::text').extract_first().strip()
		seller = response.css('div.product__seller span::text').extract_first().strip()
		img = response.css('meta[itemprop=image]::attr(content)').extract()[1].strip()
		print(price);
		with open(filename,"a",encoding='utf-8') as f:
			f.write( "--------------\n")
			f.write(response.meta['product_link']+ "\n")
			f.write(pd_name + "\n")
			f.write(sku + "\n")
			f.write(price + "\n")
			f.write(display_price + "\n")
			f.write(origin_price + "\n")
			f.write(seller + "\n")
			f.write(img + "\n")
			f.write("+++++++++++++++++++++\n")

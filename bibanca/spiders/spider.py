import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import BibancaItem
from itemloaders.processors import TakeFirst


class BibancaSpider(scrapy.Spider):
	name = 'bibanca'
	start_urls = ['https://www.bibanca.it/la-banca/news-media']

	def parse(self, response):
		post_links = response.xpath('//article/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-sm-12 col-md-8"]/div//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//time/text()').get()

		item = ItemLoader(item=BibancaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()

import scrapy
import pandas as pd
from ..items import ScraperProjectItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name='quotes'
    page_number=2
    start_urls=[
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):

        token=response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'email@gmail.com',
            'password':'gigijhlms'
        },callback=self.start_scraping)


    def start_scraping(self,response):
        open_in_browser(response)
        items=ScraperProjectItem()
        quotes_div=response.css("div.quote")

        for quote in quotes_div:
            title=quote.css("span.text::text").extract()
            author=quote.css(".author::text").extract()
            tag=quote.css(".tag::text").extract()

            items['title']=title
            items['author']=author
            items['tag']=tag

            yield items


        # next_page=response.css("li.next a::attr(href)").get()
        next_page=f'https://quotes.toscrape.com/page/{QuoteSpider.page_number}/'
        if QuoteSpider.page_number<=11:
            QuoteSpider.page_number +=1
            yield response.follow(next_page,callback=self.start_scraping)

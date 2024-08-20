#scrap name of the project
#product_api for django
"""To save the data to a JSON file, you can run your Scrapy spider with the following command:

scrapy crawl product_spider -o products.json
Now, set up a ReactJS frontend to display the product data.

Initialize React Project
Create a React project:

npx create-react-app product_frontend

"""

import scrapy
import requests

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = [
        'https://nobero.com/pages/men '  # Change to your target website
    ]
    api_url = 'http://localhost:8000/api/products/'  # Django API endpoint

    def parse(self, response):
        for product in response.css('div.product-item'):
            yield {
                'name': product.css('h2.product-title::text').get(),
                'price': product.css('span.product-price::text').get(),
                'availability': product.css('span.availability::text').get(),
                'description': product.css('p.product-description::text').get(),
            }

        # Handle pagination if applicable
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
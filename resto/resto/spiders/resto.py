import scrapy
import json

class RestoSpider(scrapy.Spider):
    name = 'resto'

    start_urls = ['https://www.ubereats.com/au/city/canberra-act']

    payload = '{"pathname":"/au/city/canberra-act"}'
    headers = {
        'authority': 'www.ubereats.com',
        'method': 'POST',
        'path': '/api/getStoreV1?localeCode=au',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
        'cache-control': 'no-cache',
        'content-length': '36',
        'content-type': 'application/json',
        'origin': 'https://www.ubereats.com',
        'x-csrf-token': 'x',
    }

    def parse(self, response):
        store_urls = 'https://www.ubereats.com/api/getSeoFeedV1?localeCode=au'
        request = scrapy.Request(url=store_urls, callback=self.parse_stores,
                                 headers=self.headers, method='POST', body=self.payload)
        yield request

    def parse_stores(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        store_list = data['data']['elements'][-2]['feedItems']
        for store in store_list:
            yield {
                'uuid' : store['uuid']
            }










# import scrapy
# import json
#
# from scrapy.utils.response import open_in_browser
#
#
# class RestoSpider(scrapy.Spider):
#     name = 'resto'
#
#     start_urls= ["https://www.ubereats.com/au/city/canberra-act"]
#
#     api_url = "https://www.ubereats.com/api/getSeoFeedV1?localeCode=au"
#     d = {"pathname": "/au/city/canberra-act"}
#     # print(pathname)
#     payload = json.dumps(d)
#     headers = {
#         'authority': 'www.ubereats.com',
#         'method': 'POST',
#         'path': '/api/getStoreV1?localeCode=au',
#         'scheme': 'https',
#         'accept': '*/*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
#         'cache-control': 'no-cache',
#         'content-length': '36',
#         'content-type': 'application/json',
#         'origin': 'https://www.ubereats.com',
#         'x-csrf-token': 'x',
#     }
#
#
#     def parse(self, response):
#         open_in_browser(response)
#         store_urls = 'https://www.ubereats.com/api/getSeoFeedV1?localeCode=au'
#         request = scrapy.Request(url=store_urls, callback=self.parse_stores,
#                                  headers=self.headers, method='POST', body=self.payload)
#         yield request
#
#     def parse_stores(self, response):
#         print(response.body)
#
#
#
#
#
#
#
#
#
#

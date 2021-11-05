import requests
import json


def get_json_stores():
    url = "https://www.ubereats.com/api/getSeoFeedV1?localeCode=au"

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

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


def get_store(uuid):
    url = "https://www.ubereats.com/api/getStoreV1?localeCode=au"
    d = {"storeUuid": uuid, "sfNuggetCount": 6}
    payload = json.dumps(d)
    headers = {
        'authority': 'www.ubereats.com',
        'method': 'POST',
        'path': '/api/getStoreV1?localeCode=au',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
        'cache-control': 'no-cache',
        'content-length': '70',
        'content-type': 'application/json',
        'origin': 'https://www.ubereats.com',
        'x-csrf-token': 'x',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)


def get_store_details(details):
    store_info = {}
    try:
        data = details['data']
    except:
        data = None
    if data is not None:
        try:
            title = store_info["title"] = data['title']
        except:
            title = store_info["title"] = "NA"
        try:
            store_info["images"] = data['heroImageUrls']
        except:
            store_info["images"] = []
        try:
            store_info["location"] = data['location']['address']
        except:
            store_info["location"] = "NA"
        try:
            store_info["currency"] = data['currencyCode']
        except:
            store_info["currency"] = "NA"
        try:
            store_info["rating"] = data['ratingValue']
        except:
            store_info["rating"] = "NA"
        try:
            store_info["meal_data"] = data['sectionEntitiesMap']
        except:
            store_info["meal_data"] = "NA"

        try:
            meal_category = data['sectionEntitiesMap']
        except:
            meal_category = None

        menu_info = []
        if meal_category is not None:
            for category in meal_category.values():
                for meal in category.values():
                    try:
                        img_url = meal['imageUrl']
                    except:
                        img_url = "NA"

                    try:
                        price = meal['price']
                    except:
                        price = "NA"

                    try:
                        meal_name = meal['title']
                    except:
                        meal_name = "NA"
                    menu_info.append({
                        "img_url": img_url,
                        "price": price,
                        "meal_name": meal_name
                    })

    store_final = {
        title: {
            "store_info": store_info,
            "menu_info": menu_info
        }
    }

    return store_final


def save_file(save_store):
    for key, value in save_store.items():
        with open(f"{key}.txt", "w") as f:
            f.write(json.dumps(save_store))
        f.close()
        break


if __name__ == '__main__':
    json_stores = get_json_stores()
    store_list = json_stores['data']['elements'][-2]['feedItems']
    my_list = []
    for store in store_list:
        # print(store['uuid'])
        # store = store_list[3]
        store_uuid = store['uuid']
        store_details = get_store(store_uuid)
        # print(store_details)
        # for key, value in store_details.items():
        #     print(f"{key} -- {value}")
        # break
        this_store = get_store_details(store_details)
        save_file(this_store)
        break
"""
stores names = response.css(".ag.b9 > a > h3::text").extract()

collection name h2.h0.h1.f5.ei.eg
details fro a particular store
import requests

url = "https://www.ubereats.com/api/getStoreV1?localeCode=au"

payload = {"storeUuid":"25da35b0-4148-495b-b475-7c59ac98f524","sfNuggetCount":6}
headers = {
  'authority': ' www.ubereats.com',
  'method': ' POST',
  'path': ' /api/getStoreV1?localeCode=au',
  'scheme': ' https',
  'accept': ' */*',
  'accept-encoding': ' gzip, deflate, br',
  'accept-language': ' en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
  'cache-control': ' no-cache',
  'content-length': ' 70',
  'content-type': ' application/json',
  'origin': ' https://www.ubereats.com',
  'x-csrf-token': ' x',
}


homepage with all restos
import requests

url = "https://www.ubereats.com/api/getSeoFeedV1?localeCode=au"

payload = "{\"pathname\":\"/au/city/canberra-act\"}"
headers = {
  'authority': '  www.ubereats.com',
  'method': '  POST',
  'path': ' /api/getStoreV1?localeCode=au',
  'scheme': '  https',
  'accept': '  */*',
  'accept-encoding': '  gzip, deflate, br',
  'accept-language': '  en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
  'cache-control': '  no-cache',
  'content-length': '  36',
  'content-type': '  application/json',
  'origin': '  https://www.ubereats.com',
  'x-csrf-token': '  x',
  'Cookie': 'dId=a8401ca3-7389-4486-a3fd-d627f302447a; marketing_vistor_id=2fead8fe-20b6-45bb-afb7-4f53fb4b6032; uev2.id.session=739d7e4c-71fb-4e69-94ed-d12f1a34c194; uev2.id.xp=fa4d10a6-ad61-4dc7-86c7-24f854b8c025; uev2.ts.session=1636054626965; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MzYwNDg0MzQsImV4cCI6MTYzNjEzNDgzNH0.bx25clALDY3THPhp1pLr0ZQcM6lyWPoICoGazT_g7cU'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)





response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
import requests

url = "https://www.ubereats.com/api/getStoreV1?localeCode=au"

payload = "{\"storeUuid\":\"25da35b0-4148-495b-b475-7c59ac98f524\",\"sfNuggetCount\":6}"
headers = {
  'authority': ' www.ubereats.com',
  'method': ' POST',
  'path': ' /api/getStoreV1?localeCode=au',
  'scheme': ' https',
  'accept': ' */*',
  'accept-encoding': ' gzip, deflate, br',
  'accept-language': ' en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
  'cache-control': ' no-cache',
  'content-length': ' 70',
  'content-type': ' application/json',
  'origin': ' https://www.ubereats.com',
  'x-csrf-token': ' x',
  'Cookie': 'dId=a8401ca3-7389-4486-a3fd-d627f302447a; marketing_vistor_id=2fead8fe-20b6-45bb-afb7-4f53fb4b6032; uev2.id.session=6dde9733-bd3a-4563-90c2-22474013021c; uev2.id.xp=fa4d10a6-ad61-4dc7-86c7-24f854b8c025; uev2.ts.session=1636092484860; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MzYwNDg0MzQsImV4cCI6MTYzNjEzNDgzNH0.bx25clALDY3THPhp1pLr0ZQcM6lyWPoICoGazT_g7cU'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

"""
from scrapy import Selector

# response = []
# for store in response.css(".ag.b9 > a::attr(href)").getall():
#     print(store)
#
#
# for category in response.css("ul.gy > .gz h2::text"):
#     category.css("h2::text")

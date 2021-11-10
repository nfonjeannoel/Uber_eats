from random import randint

import requests
import json

cities_urls = [

    #urls for all the cities in Australia
    # "https://www.ubereats.com/au/city/canberra-act",
    # "https://www.ubereats.com/au/city/byron-bay-nsw",
    # "https://www.ubereats.com/au/city/galston-nsw",
    # "https://www.ubereats.com/au/city/queanbeyan-nsw",
    # "https://www.ubereats.com/au/city/wagga-wagga-nsw",
    # "https://www.ubereats.com/au/city/catherine-field-nsw"
    # "https://www.ubereats.com/au/city/central-coast-nsw",
    # "https://www.ubereats.com/au/city/bathurst-nsw",
    # "https://www.ubereats.com/au/city/wollongong-nsw",
    # "https://www.ubereats.com/au/city/leppington-nsw",
    # "https://www.ubereats.com/au/city/sydney-nsw",
    # "https://www.ubereats.com/au/city/newcastle-nsw",
    # "https://www.ubereats.com/au/city/tweed-heads-nsw",
    # "https://www.ubereats.com/au/city/old-bar-nsw",
    # "https://www.ubereats.com/au/city/wagga-wagga-nsw"
    # "https://www.ubereats.com/au/city/darwin-nt",
    # "https://www.ubereats.com/au/city/brisbane-qld",
    # "https://www.ubereats.com/au/city/cairns-qld",
    # "https://www.ubereats.com/au/city/gold-coast-qld",
    # "https://www.ubereats.com/au/city/hervey-bay-qld",
    # "https://www.ubereats.com/au/city/highfields-qld",
    # "https://www.ubereats.com/au/city/mackay-qld",
    # "https://www.ubereats.com/au/city/mount-cotton-qld",
    # "https://www.ubereats.com/au/city/rockhampton-qld",
    # "https://www.ubereats.com/au/city/sunshine-coast-qld",
    # "https://www.ubereats.com/au/city/toowoomba-qld",
    # "https://www.ubereats.com/au/city/townsville-qld",
    # "https://www.ubereats.com/au/city/tweed-heads-qld",
    # "https://www.ubereats.com/au/city/withcott-qld"
    # "https://www.ubereats.com/au/city/adelaide-sa",
    # "https://www.ubereats.com/au/city/angle-vale-sa",
    # "https://www.ubereats.com/au/city/gawler-sa",
    # "https://www.ubereats.com/au/city/hobart-tas",
    # "https://www.ubereats.com/au/city/launceston-tas",
    # "https://www.ubereats.com/au/city/ballarat-vic",
    # "https://www.ubereats.com/au/city/bendigo-vic",
    # "https://www.ubereats.com/au/city/diggers-rest-vic",
    # "https://www.ubereats.com/au/city/geelong-vic",
    # "https://www.ubereats.com/au/city/lara-vic",
    # "https://www.ubereats.com/au/city/leopold-vic",
    # "https://www.ubereats.com/au/city/melbourne-vic",
    # "https://www.ubereats.com/au/city/melton-vic"
    # "https://www.ubereats.com/au/city/officer-vic",
    # "https://www.ubereats.com/au/city/pakenham-vic",
    # "https://www.ubereats.com/au/city/rockbank-vic",
    # "https://www.ubereats.com/au/city/sunbury-vic",
    # "https://www.ubereats.com/au/city/wonga-park-vic",
    # "https://www.ubereats.com/au/city/baldivis-wa",
    # "https://www.ubereats.com/au/city/bunbury-wa",
    # "https://www.ubereats.com/au/city/ellenbrook-wa",
    # "https://www.ubereats.com/au/city/perth-wa",
    # "https://www.ubereats.com/au/city/yanchep-wa"
]


def get_json_stores(pathname):
    api_url = "https://www.ubereats.com/api/getSeoFeedV1?localeCode=au"
    d = {"pathname": pathname}
    # print(pathname)
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
        'content-length': '36',
        'content-type': 'application/json',
        'origin': 'https://www.ubereats.com',
        'x-csrf-token': 'x',
    }

    response = requests.request("POST", api_url, headers=headers, data=payload)

    return json.loads(response.text)


def get_store(uuid):
    api_url = "https://www.ubereats.com/api/getStoreV1?localeCode=au"
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
    response = requests.request("POST", api_url, headers=headers, data=payload)
    return json.loads(response.text)


def get_store_details(details):
    store_info = {}
    try:
        data = details['data']
    except:
        data = None
    if data is not None:
        sections_list = []

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
            store_info["phoneNumber"] = data['phoneNumber']
        except:
            store_info["phoneNumber"] = "NA"

        try:
            meal_category = data['sectionEntitiesMap']
        except:
            meal_category = None

        menu_info = []
        if meal_category is not None:
            for category in meal_category.values():
                for meal in category.values():
                    sub_section = data['subsectionsMap']
                    # subsection_list = sections_list['subsectionUuids']
                    meal_uuid = meal['uuid']
                    # print(meal_uuid)
                    meal_type = "NA"
                    for section in sub_section.values():
                        uuids = section['itemUuids']
                        if meal_uuid in uuids:
                            meal_type = section['title']

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

                    # uuid = meal['uuid']

                    menu_info.append({
                        "img_url": img_url,
                        "price": str(price)[:-2] + "." + str(price)[-2:],
                        "meal_name": meal_name,
                        "meal_type": meal_type
                    })

    store_final = {
        title: {
            "store_info": store_info,
            "menu_info": menu_info
        }
    }

    return store_final


def save_file(save_store, file_name):
    with open(f"{file_name.split('/')[-1]}.txt", "w") as f:
        f.write(json.dumps(save_store))
    f.close()


def get_path_url(param_url):
    split_url = param_url[24:]
    return split_url


from time import sleep


# def small_sleep():
#     sleep(1)


def process_store(city_url):
    path = get_path_url(city_url)
    print(path)
    json_stores = get_json_stores(path)
    if json_stores['status'] == "failure":
        print(f"store {path} not found")
        return
    # print(json.dumps(json_stores))

    ind = 0
    for ind_store, store in enumerate(json_stores['data']['elements']):
        if "feedItems" in store.keys() and "storesMap" in store.keys():
            ind = ind_store
            break
    store_list = json_stores['data']['elements'][ind]['feedItems']
    my_list = []
    counter = 0
    for store in store_list:
        counter += 1
        # print(store['uuid'])
        # store = store_list[3]
        store_uuid = store['uuid']
        store_details = get_store(store_uuid)
        # print(store_details)
        # for key, value in store_details.items():
        #     print(f"{key} -- {value}")
        # break
        this_store = get_store_details(store_details)
        my_list.append(this_store)
        print("added new store" + store_uuid)
    save_file(my_list, path)

    print(f"saved file {path}")
    # if counter == 4:
    #     break


if __name__ == '__main__':
    # counter = 0
    for url in cities_urls:
        process_store(url)
        # break
        # counter += 1
        # if counter == 2:
        #     break
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

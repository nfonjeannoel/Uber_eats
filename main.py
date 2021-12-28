import datetime
import os
import pathlib
from random import randint

import boto3
import requests
import json
import datetime

cities_urls = [
    # urls for all the cities in Australia
    # "https://www.ubereats.com/au/city/canberra-act",
    # "https://www.ubereats.com/au/city/byron-bay-nsw",
    # "https://www.ubereats.com/au/city/galston-nsw",
    # "https://www.ubereats.com/au/city/queanbeyan-nsw",
    "https://www.ubereats.com/au/city/wagga-wagga-nsw",
    # "https://www.ubereats.com/au/city/catherine-field-nsw",
    # "https://www.ubereats.com/au/city/central-coast-nsw",
    # "https://www.ubereats.com/au/city/bathurst-nsw",
    # "https://www.ubereats.com/au/city/wollongong-nsw",
    # "https://www.ubereats.com/au/city/leppington-nsw",
    # "https://www.ubereats.com/au/city/sydney-nsw",
    # "https://www.ubereats.com/au/city/newcastle-nsw",
    # "https://www.ubereats.com/au/city/tweed-heads-nsw",
    # "https://www.ubereats.com/au/city/old-bar-nsw",
    # "https://www.ubereats.com/au/city/wagga-wagga-nsw",
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
    # "https://www.ubereats.com/au/city/withcott-qld",
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
    # "https://www.ubereats.com/au/city/melton-vic",
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
locale_code = 'au'
city_name = "australia"


def get_week():
    return str(datetime.datetime.utcnow().isocalendar()[0]) + '-' + str(datetime.datetime.utcnow().isocalendar()[1])


week = ""
site_name = "ubereats"


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

    for i in range(5):
        response = requests.request(method="POST", url=api_url, headers=headers, data=payload)
        # print(response.text)
        response = json.loads(response.text)
        # title = response['data'].get('title', None)
        # if response['status'] == "failure":
        #     print(f"failed to get data, retrying {i + 1} of 5 times")
        # else:
        #     if title is None:
        #         continue
        #     else:
        #         break
    return response


def get_store(uuid):
    api_url = f"https://www.ubereats.com/api/getStoreV1?localeCode={locale_code}"
    d = {"storeUuid": uuid, "sfNuggetCount": 8}
    # print(uuid)
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
    for i in range(5):
        response = requests.request(method="POST", url=api_url, headers=headers, data=payload)
        # print(response.text)
        response = json.loads(response.text)
        # title = response['data'].get('title', None)
        # if response['status'] == "failure":
        #     print(f"failed to get data, retrying {i + 1} of 5 times")
        # else:
        #     if title is None:
        #         continue
        #     else:
        #         break
    return response


def create_path_store(my_section_name):
    global week
    week = get_week()
    parent_dir = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/") + f"/{site_name}/{city_name}/"
    path = os.path.join(parent_dir, week)

    try:
        os.makedirs(path, exist_ok=True)
        print("sub Directory '%s' created successfully" % my_section_name)

    except OSError as error:
        print("sub Directory '%s' can not be created" % my_section_name)


def get_store_details(details):
    store_info = {}
    data = details.get('data', None)
    if data is not None:
        title = store_info["title"] = data.get('title', "NA")
        store_info["uuid"] = data.get('uuid', "NA")
        store_info["cuisine"] = data.get("categories", [])
        store_info["slug"] = data.get("slug", "NA")
        store_info["images"] = data.get('heroImageUrls', [])

        temp = data.get('location')
        if temp is not None:
            store_info["location"] = temp.get('address', 'NA')
        else:
            store_info["location"] = "NA"

        store_info["currency"] = data.get('currencyCode', "NA")
        store_info["rating"] = data.get('rating', "NA")
        store_info["phoneNumber"] = data.get('phoneNumber', "NA")
        store_info["price_range"] = data.get('priceBucket', "NA")

        try:
            start_time = str(data["hours"][0]["sectionHours"][0]["startTime"])
        except:
            start_time = ""
        try:
            end_time = str(data["hours"][0]["sectionHours"][0]["endTime"])
        except:
            end_time = ""
        store_info["opening_hours"] = {
            "start_time": start_time,
            "end_time": end_time
        }
        meal_category = data.get('sectionEntitiesMap', {})
        # print(meal_category)
        menu_info = []
        if meal_category == {} or meal_category is None:
            print("meal category is none, fetching catalog-section")
            meal_category = data.get('catalogSectionsMap', {})
            if meal_category == {} or meal_category is None:
                print("no menu data for " + title)
            else:
                # print(meal_category)

                for category in meal_category.values():
                    for meal in category:
                        try:
                            menu = meal['payload']['standardItemsPayload']['catalogItems']  # returns list
                        except:
                            menu = []
                        if not menu:
                            print(f"menu for {title} is differny format")
                        else:
                            for a_meal in menu:
                                menu_info.append({
                                    "img_url": a_meal.get('imageUrl', "NA"),
                                    "price": a_meal.get('price', "NA"),
                                    "priceTagline": a_meal.get('priceTagline', "NA"),
                                    "meal_name": a_meal.get('title', "NA"),
                                    "meal_description": a_meal.get('itemDescription', "NA"),
                                    "meal_type": "NA",
                                    "meal_uuid": a_meal.get('uuid', "NA")
                                })
                # catalogSectionUUID
        else:
            for category in meal_category.values():
                for meal in category.values():
                    # print(meal)
                    sub_section = data['subsectionsMap']
                    # subsection_list = sections_list['subsectionUuids']
                    meal_uuid = meal['uuid']
                    # print(meal_uuid)
                    meal_type = []
                    for section in sub_section.values():
                        uuids = section['itemUuids']
                        if meal_uuid in uuids:
                            meal_type.append(section['title'])

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

                    try:
                        meal_desc = meal['description']
                    except:
                        meal_desc = "NA"

                    try:
                        meal_uuid = meal['uuid']
                    except:
                        meal_uuid = "NA"

                    # uuid = meal['uuid']

                    menu_info.append({
                        "img_url": img_url,
                        "price": str(price)[:-2] + "." + str(price)[-2:],
                        "meal_name": meal_name,
                        "meal_description": meal_desc,
                        "meal_type": meal_type,
                        "meal_uuid": meal_uuid
                    })

        store_final = {
            title: {
                "store_info": store_info,
                "menu_info": menu_info
            }
        }
        return store_final


def save_file_locally(save_store, path):
    for key, val in save_store.items():
        file_name = val.get('store_info')
        file_name = file_name.get("uuid", str(randint(1, 4000)))
        break
    save_location = str(pathlib.Path(__file__).parent.resolve()).replace("\\",
                                                                         "/") + f"/{site_name}/{city_name}/{week}/{file_name}"
    with open(f"{save_location}.json", "w") as f:
        f.write(json.dumps(save_store))
    f.close()


# new saving format
def save_file(save_store, file_name):
    s3 = boto3.resource('s3', aws_access_key_id="XXXXXXXX",
                        aws_secret_access_key="xxxxxxx")
    s3object = s3.Object('tw-external-dumps1',
                         f"opentable/canada/{str(datetime.datetime.utcnow().isocalendar()[0]) + '-' + str(datetime.datetime.utcnow().isocalendar()[1])}/{file_name.split('/')[-1]}.json")

    s3object.put(
        Body=(bytes(json.dumps(save_store).encode('UTF-8')))
    )
    save_file_locally(save_store, file_name)


def get_path_url(param_url):
    split_url = param_url[24:]
    return split_url


from time import sleep


# def small_sleep():
#     sleep(1)


def process_store(city_url):
    path = get_path_url(city_url)
    # print(path)
    create_path_store(path.split('/')[-1])
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
    # my_list = []
    # print(store_list)
    counter = 0
    for store in store_list:
        counter += 1
        # print(store['uuid'])
        # store = store_list[3]
        store_uuid = store['uuid']
        # print(store_uuid)
        store_details = get_store(store_uuid)
        # print(store_details)
        # return
        # for key, value in store_details.items():
        #     print(f"{key} -- {value}")
        # break
        this_store = get_store_details(store_details)
        # this_store['store_url'] = f"https://www.ubereats.com/{locale_code}/city/{path.split('/')[-1]}"
        # save store
        # my_list.append(this_store)
        # print(this_store)
        # print("added new store" + store_uuid)
        # if counter == 2:
        save_file_locally(this_store, path.split('/')[-1])
        # print(my_list)
        print(f"saved file {store_uuid}")
    # if counter == 4:
    #     break


if __name__ == '__main__':
    # counter = 0
    for url in cities_urls:
        process_store(url)
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

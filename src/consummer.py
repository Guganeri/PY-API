from flask import Flask, jsonify, Response
from cat.CatRequest import CatRequest
from dotenv import load_dotenv
from bson.json_util import dumps
import json
import pymongo
import os


load_dotenv()

BDURL = os.getenv("BDURL")

client = pymongo.MongoClient(BDURL)
db = client.api_cat
catCollection = db['api_cat']
hatCatCollection = db['hat_Cat']
glassCatCollection = db['glass_Cat']

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")


def insertDatabse():

    cat_data = CatRequest(f'{URL}/breeds', TOKEN)
    cats = []  # Lista final para insert na base
    catd = []  # Lista para guardar informações durante for e concatenar inf

    for cat in cat_data:
        get = catCollection.find({"id": cat["id"]})
        if (list(get) == []):
            print(f'No exist: {cat["id"]} in database add.')
            catd = {
                'id': cat["id"],
                'origin': cat["origin"],
                'temperament': cat["temperament"],
                'description': cat["description"]
            }
            cat_dataNew = CatRequest(
                f'{URL}/images/search?id="{cat["id"]}"&limit=3&format=jpg', TOKEN)
            for cat in range(len(cat_dataNew)):
                # print(cat_dataNew[cat]["url"])
                catd.update({
                    f'url{cat}': (cat_dataNew[cat]["url"])
                })
            cats.append(catd)

        else:
            print("exist ! not add")
            continue

    if not cats == []:
        catCollection.insert_many(cats)

    ###### END INSERT BREEDS ######

    cat_data = CatRequest(
        f'{URL}/images/search?category_ids={"1"}&limit=3', TOKEN)

    catsIMG = []
    catsTempImg = []

    for hatCat in range(len(cat_data)):
        get = hatCatCollection.find({"url": cat_data[hatCat]["url"]})
        if (list(get) == []):
            catsTempImg = {
                f'url': (cat_data[hatCat]["url"])
            }
        catsIMG.append(catsTempImg)
    if not catsIMG == []:
        hatCatCollection.insert_many(catsIMG)
        catsIMG.clear()
        catsTempImg.clear()

    cat_data = CatRequest(
        f'{URL}/images/search?category_ids={"4"}&limit=3', TOKEN)

    for glassCat in range(len(cat_data)):
        get = hatCatCollection.find({"url": cat_data[glassCat]["url"]})
        if (list(get) == []):
            catsTempImg = {
                f'url': (cat_data[glassCat]["url"])
            }
        catsIMG.append(catsTempImg)
    if not catsIMG == []:
        glassCatCollection.insert_many(catsIMG)
        catsIMG.clear()
        catsTempImg.clear()


#if __name__ == "__main__":
#    insertDatabse()

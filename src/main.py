from cat.CatRequest import CatRequest
from cat.CatFiller import CatFiller
from dotenv import load_dotenv
from bson.json_util import dumps
import pymongo
import os


load_dotenv()

BDURL = os.getenv("BDURL")

client = pymongo.MongoClient()
db = client.api_cat
catCollection = db['api_cat']

#dblist = client.list_database_names()
# if "api_cat" in dblist:
#    print("database up")

#collist = db.list_collection_names()
# if "api_cat" in collist:
#    print("Collection exists.")

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")


def main():

    cat_data = CatRequest(URL, TOKEN)
    cats = []
    #catList = ()

    for cat in cat_data:
        get = catCollection.find({"id": cat["id"]})
        if (list(get) == []):
                print("not exist")
 
                cats.append({
                'id' : cat["id"],
                'origin' : cat["origin"],
                'temperamen' : cat["temperament"],
                'description' : cat["description"]
                })
 
        else:
                print("exist ! not add")
 
    if not cats == []:
        catCollection.insert_many(cats)

        # if (catCollection.find({"id": cat["id"]})):
        #    cats.append({
        #        'id' : cat["id"],
        #        'origin' : cat["origin"],
        #        'temperamen' : cat["temperament"],
        #        'description' : cat["description"]
        #    })

    # for cat in cats:
    #    print(cat["id"])

    # catCollection.insert_many(cats)


if __name__ == "__main__":
    main()

from cat.CatRequest import CatRequest
from cat.CatFiller import CatFiller
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")


def main():

    cat_data = CatRequest(URL, TOKEN)
    cats = []

    for cat in cat_data:
        cats.append(CatFiller(
            id=cat["id"],
            origin=cat["origin"],
            temperament=cat["temperament"],
            description=cat["description"]
        ))

    for cat in cats:
        print(cat.id)        


if __name__ == "__main__":
    main()

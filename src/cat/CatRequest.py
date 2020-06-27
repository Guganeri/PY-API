import requests
import json

def CatRequest(url: str, token: str):

    cat_json = None

    try:
        response = requests.get(url=url, headers={'x-api-key':token},verify=True)
        cat_json = response.json()
    except Exception as exception:
        print ("OOps: Something Else",exception)
    
    return cat_json
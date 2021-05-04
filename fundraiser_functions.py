import requests
import json
from fundraiser import Fundraiser

DEAN_FARM_TRUST_URL = "https://api.justgiving.com/137f78b6/v1/fundraising/pages/paula-walsh11/"

def getDeanFarmTrustFun():
    fundraiser_json = getJsonFromRequest(DEAN_FARM_TRUST_URL)
    donations_json = getJsonFromRequest(DEAN_FARM_TRUST_URL+"donations/")
    return Fundraiser(donations_json['pagination']['totalResults'],fundraiser_json['grandTotalRaisedExcludingGiftAid'])


def getJsonFromRequest(url):
    content = requests.get(url, headers={"Content-type": "application/json"}).content
    return json.loads(content)
import requests
import json
from fundraiser import Fundraiser

DEAN_FARM_TRUST_URL = "https://api.justgiving.com/137f78b6/v1/fundraising/pages/teameh10/"
AMF_URL = "https://www.againstmalaria.com/Fundraiser.aspx?FundraiserID=8534"

AMF_SPONSOR_TAG = b'MainContent_UcFundraiserSponsors1_ucPager2_pnlTextCounter">Sponsors'
AMF_TOTAL_TAG = b'id="MainContent_lblGrandTotal">'



def getDeanFarmTrustFun():
    fundraiser_json = getJsonFromRequest(DEAN_FARM_TRUST_URL)
    donations_json = getJsonFromRequest(DEAN_FARM_TRUST_URL+"donations/")
    return Fundraiser(int(donations_json['pagination']['totalResults']),float(fundraiser_json['grandTotalRaisedExcludingGiftAid']))


def getJsonFromRequest(url):
    content = requests.get(url, headers={"Content-type": "application/json"}).content
    return json.loads(content)
    

#Logic for if it's one page or more
def getAMFFun():
    donationNo = 0
    content = requests.get(AMF_URL).content.replace(b" ",b"").replace(b'\r',b"").replace(b'\t',b"").replace(b'\n',b"")
    
    #Get number of donations
    try:
        sponsors=content[content.index(AMF_SPONSOR_TAG)+len(AMF_SPONSOR_TAG):content.index(AMF_SPONSOR_TAG)+100].decode("utf-8")
        donationNo = int(sponsors.split("of")[1].split("<")[0])
    except:
        empty_row_content = b'<tdalign="center"valign="top"width="20"></td><tdalign="left"valign="top"height="14"></td>'
        all_rows_content = b'<tdalign="left"valign="top"height="14">'
        all_rows=content.split(all_rows_content)
        empty_rows=content.split(empty_row_content)
        donationNo = len(all_rows) - len(empty_rows)
    print(donationNo)
    
    #Get total amounts
    grand_total_str = content[content.index(AMF_TOTAL_TAG)+len(AMF_TOTAL_TAG):content.index(AMF_TOTAL_TAG)+100].decode("utf-8")
    grand_total = float(grand_total_str.split("<")[0].replace(",",""))
    print(grand_total)
    
    return Fundraiser(donationNo,grand_total)
    
    
    
    
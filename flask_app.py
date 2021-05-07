from flask import Flask, render_template
from fundraiser import Fundraiser
from fundraiser_functions import *

app = Flask(__name__)

temp_list = ["harry", "david", "barney", "heol"]



@app.route("/")
def home():
    #temp_fun = Fundraiser(12, 25)
    #contents = urllib.request.urlopen('GET',"https://api.justgiving.com/137f78b6/v1/fundraising/pages/mark-clark6/").read()
    
    dean_fun = getDeanFarmTrustFun()
    amf_fun = getAMFFun()
    
    return render_template('home.html', total=dean_fun.getTotalRaised()+amf_fun.getTotalRaised(), donations=dean_fun.getDonationNo()+amf_fun.getDonationNo())
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/test")
def faq_two():
    return render_template('test.html')
    
@app.route("/goodbye")
def goodbye():
    return "Goodbye"
    
if __name__ == "__main__":
    app.run(debug=True)

#API request to get donations in JSON format of a thing
#curl --request GET -H "Content-type: application/json" https://api.justgiving.com/137f78b6/v1/fundraising/pages/mark-clark6/donations
#curl --request GET -H "Content-type: application/json" https://api.justgiving.com/137f78b6/v1/fundraising/pages/mark-clark6/

#Use web scraping to get the grand total & number of donations from against malaria


#Receive emails as Python, update a database somewhere?
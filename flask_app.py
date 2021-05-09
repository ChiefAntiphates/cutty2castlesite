from flask import Flask, render_template
from fundraiser import Fundraiser
from fundraiser_functions import *

app = Flask(__name__)


@app.route("/")
def home():
    dean_fun = getDeanFarmTrustFun()
    amf_fun = getAMFFun()
    return render_template('home.html', 
        total=dean_fun.getTotalRaised()+amf_fun.getTotalRaised(), 
        donations=dean_fun.getDonationNo()+amf_fun.getDonationNo())
    
@app.route("/charities")
def charities():
    return render_template('charities.html')
    
if __name__ == "__main__":
    app.run(debug=True)
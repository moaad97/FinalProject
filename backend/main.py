import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime
import urllib, json
import urllib.request
import socket
from pip._internal import req
from werkzeug.utils import redirect

# list to save the transction
app = Flask(__name__)
info_list =[] 

@app.route("/", methods=["POST", "GET"])
def index():
    meta_data = "http://169.254.169.254/latest/meta-data/public-ipv4"
    ip_address = (requests.get(meta_data).content).decode('utf-8')
    if request.method == "POST":
        response = requests.get("http://data.fixer.io/api/latest?access_key=85aa5a4fb3533fbae7223f74ccb1befb")
        app.logger.info(response)
        jsonfile = response.json()
        result = (jsonfile["rates"][request.form.get("secondCurrency")] / jsonfile["rates"][request.form.get("firstCurrency")]) * float(request.form.get("amount"))
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = request.form.get("firstCurrency")
        currencyInfo["secondCurrency"] = request.form.get("secondCurrency")
        currencyInfo["amount"] = request.form.get("amount")
        currencyInfo["result"] = result
        now = datetime.now()
        newchange = [now.strftime("%H:%M:%S"), request.form.get("amount"), request.form.get("firstCurrency"), request.form.get("secondCurrency"), jsonfile["rates"][request.form.get("secondCurrency")], result]
        info_list.append(newchange)
        res = requests.post(ip_address + ':5002/', json=currencyInfo)
        return redirect(ip_address + ':5002/', code=302)
    else:
        return redirect(ip_address + ':5002/', code=302)

@app.route("/Auti/", methods=["POST", "GET"])
def Auti():
    ip_address2 = (requests.get("http://169.254.169.254/latest/meta-data/public-ipv4").content).decode('utf-8')
    info_dict = dict()
    info_dict["info"] = info_list
    res = requests.post( ip_address2 + ':5001/', json=info_dict)
    return redirect( ip_address2 + ':5001/', code=302)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime

app = Flask(__name__)
info_dict = dict() 
@app.route("/", methods=["POST", "GET"])
def index():
    ip_address = (requests.get("http://169.254.169.254/latest/meta-data/public-ipv4").content).decode('utf-8')
    if request.method == "POST":
        global info_dict
        input_json = request.get_json(force=True)
        info_dict = input_json
    return render_template("index2.html", info = info_dict, val = ip_address+":5000", val2 = ip_address + ":5000/Auti/")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
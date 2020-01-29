from flask import Flask, jsonify, request
import requests
import os
import markdown
import json
import User
import mysql.connector as mysql

API_URL = "https://www.alphavantage.co/query"

app = Flask(__name__)


# Show Readme file to describe the use of each and every API
@app.route("/")
def index():
    # read readme.txt and load it in the browser

    with open(os.path.dirname(app.root_path) + "/Readme.txt", "r") as helpfile:
        contents = helpfile.read()

    return markdown.markdown(contents), 200


@app.route("/AuthenticateUser")
def AuthenticateUser():
    new_User = User()
    user = request.json
    new_User.uname = user['Uname']
    new_User.pwd = user['Pwd']
    new_User.token = user['Token']

    #DBManager.initdb()

    db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="dutch@123",
            database="StockAPI"
        )

    cursor = db.cursor()

    cursor.execute("select * from StockAPI.Investor_Details")
    rows = cursor.fetchall()
    if cursor.rowcount > 0:
        return true
    else:
        return false

    #return new_User.toJSON(), 200


# Get Quote for the company mentioned in the parameter (Company Symbol)
@app.route("/GetQuote/<string:symbol>")
def getquote(symbol):
    data = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "datatype": "json",
        "apikey": "2I7USOWXF6BYGCT1"
    }
    response = requests.get(API_URL, params=data)
    return response.text


@app.route("/Search/<string:searchstring>")
def searchcomp(searchstring):
    data = {
        "function": "SYMBOL_SEARCH",
        "keywords": searchstring,
        "datatype": "json",
        "apikey": "2I7USOWXF6BYGCT1"
    }
    response = requests.get(API_URL, params=data)
    return response.content


class User:

    def __init__(self):
        '''self.uname = "abc"
        self.pwd = "hq"'''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


'''class DBManager:

    @staticmethod
    def initdb(self):
        db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="dutch@123",
            database="TestDb"
        )
'''

if __name__ == '__main__':
    app.run()

from flask import Flask, escape, request
import requests
import logging

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    q = request.form.get('q')
    logging.log(0, q)
    appid = request.form.get('appid')
    logging.log(0, appid)
    response = requests.get('http://api.openweathermap.org/data/2.5/weather',
                 params = [('q', q), ('appid', appid)])
    return response.json()

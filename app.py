from flask import Flask, escape, request
import requests
import logging

logger = logging.getLogger('Anya')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    q = request.form.get('q')
    logger.info(q)
    appid = request.form.get('appid')
    logger.info(appid)
    response = requests.get('http://api.openweathermap.org/data/2.5/weather',
                 params = [('q', q), ('appid', appid)])
    return response.json()

from flask import Flask, escape, request
import requests
import logging

app = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

@app.route('/', methods=['POST'])
def main():
    q = dict(request.get_json())['q']
    appid = dict(request.get_json())['appid']
    response = requests.get('http://api.openweathermap.org/data/2.5/weather',
                 params = [('q', q), ('appid', appid)])
    return response.json()

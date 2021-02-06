import requests
import json
from pprint import pprint
import os

token = os.environ['TOKEN']

#81633833

def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()
    updates = data['result']
    return updates



import requests

import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 

def sendDice(idx):
    url = f'https://api.telegram.org/bot{token}/sendDice'
    payload = {
    'chat_id':idx,
    }
    r = requests.get(url,params=payload)
    return r.json()


ids= 81633833
sendDice(ids)
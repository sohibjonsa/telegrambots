import requests
import json
import os
from pprint import pprint


token = os.environ['TOKEN']

def sendMsg(idx, txt):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    p = {
        'chat_id': idx,
        'text': txt,
        'parse_mode': 'MarkdownV2'
    }
    r = requests.get(url, params=p)
   

sendMsg(81633833, '*Salom*')

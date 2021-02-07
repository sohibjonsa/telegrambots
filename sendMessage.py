import requests
from pprint import pprint
import os

token = os.environ['TOKEN']

def sendMsg(idx):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    p = {
        'chat_id': idx,
        'text': 'Yaxshimisiz?'
    }
    r = requests.get(url, params=p)
    print(r.url)

ids = '81633833'
for idx in ids:
    sendMsg(idx)

import requests
import json
import os
from pprint import pprint


token = os.environ['TOKEN']

def getUpd():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()
    updates = data['result']
    return updates
# def getTxt(data):
#     return data['text']

def sendMsg(idx, txt):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    p = {
        'chat_id': idx,
        'text': txt
    }
    r = requests.get(url, params=p)
   


upd_len = len(getUpd())
upd_len_last = len(getUpd())

while True:
    upd_len_last = len(getUpd())
    message = getUpd()[-1]['message']['text']

    if upd_len != upd_len_last:
        sendMsg(81633833, message)
        upd_len = len(getUpd())


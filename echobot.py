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

upd_len = len(getUpd())
upd_len_last = len(getUpd())

while True:
    upd_len_last = len(getUpd())
    print(f'len: {upd_len}, last_len:{upd_len_last}')

    if upd_len != upd_len_last:
        print('*'*10)
        print(f'len: {upd_len}, last_len:{upd_len_last}')
        upd_len = len(getUpd())
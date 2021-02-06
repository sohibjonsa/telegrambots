import requests
from pprint import pprint
import os

token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/sendMessage'
p = {
    'chat_id': 81633833,
    'text': 'Yaxshimisiz?'
}
r = requests.get(url, params=p)

print(r.json())

print(r.url)


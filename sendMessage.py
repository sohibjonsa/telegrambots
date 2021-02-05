import requests
from pprint import pprint

token = '1583466472:AAGguScK6YXMLPCiRKN01kbEkviCw92wmqw'
url = f'https://api.telegram.org/bot{token}/sendMessage'
p = {
    'chat_id': 81633833,
    'text': 'Yaxshimisiz?'
}
r = requests.get(url, params=p)

print(r.json())

print(r.url)


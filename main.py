import requests
from pprint import pprint
import os

token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

print(r.url)

for update in updates:
    message = update['message']
    user = message['from']
    id = user['id']
    text = message['text']
    first = user.get('first_name', '')
    last = user.get('last_name', '')
    print(f'ID: {id} \n Fullname: {first} {last} \n Message {text}')

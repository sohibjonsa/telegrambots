import requests
from pprint import pprint

token = '1583466472:AAGguScK6YXMLPCiRKN01kbEkviCw92wmqw'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']
update = updates[0]
# for update in updates:
#     message = update['message']
#     user = message['from']
#     first = user.get('first_name', '')
#     last = user.get('last_name', '')
#     print(f'{first} {last}')

pprint((data)
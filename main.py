import requests
from pprint import pprint

token = '1583466472:AAFxCsiR1XSl_oUaIRIfdfa2DOINEBzdnVE'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

for update in updates:
    message = update['message']
    user = message['from']
    name = user['first_name']
    print(name)
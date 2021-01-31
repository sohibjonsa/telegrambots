import requests
from pprint import pprint

token = '1583466472:AAFxCsiR1XSl_oUaIRIfdfa2DOINEBzdnVE'
url = f'https://api.telegram.org/bot{token}/getMe'
r = requests.get(url)
data = r.json()

pprint(data)
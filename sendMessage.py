import requests
from pprint import pprint

token = '1583466472:AAGguScK6YXMLPCiRKN01kbEkviCw92wmqw'
url = f'https://api.telegram.org/bot{token}/sendMessage'
r = requests.get(url)

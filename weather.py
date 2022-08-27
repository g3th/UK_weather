import requests
import json
import time
from bs4 import BeautifulSoup as soup

while True:
	try:
		postcode = input('Please Enter a Valid UK Postcode: ')
		page = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{}'.format(postcode)
		request = requests.get(page).json()
		date = str(request['forecasts'][0]['detailed']['lastUpdated']).split('T')[0]
		time = str(request['forecasts'][0]['detailed']['lastUpdated']).split('T')[1].split('.')[0]
		break
	except KeyError:
		print ('Invalid Postcode.'); time.sleep(0.8)
		print('\x1bc')
		continue

print(request)



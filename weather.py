import requests
import json
import time
from header import title
from bs4 import BeautifulSoup as soup
title()

while True:
	try:
		postcode = input('\nPlease Enter a Valid UK Postcode: ')
		location = 'https://www.doogal.co.uk/UKPostcodes.php?Search='
		location_page=location+postcode[:3]
		fetch_location = requests.get(location_page)
		parse_location = soup(fetch_location.content, 'html.parser')
		location= parse_location.find('p').text.split('areas of')[1].split('.')[0].replace(' ','').replace(',',', ')
		page = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{}'.format(postcode)
		request = requests.get(page).json()
		date = str(request['forecasts'][0]['detailed']['lastUpdated']).split('T')[0]
		time = str(request['forecasts'][0]['detailed']['lastUpdated']).split('T')[1].split('.')[0]
		break
	except KeyError:
		print ('Invalid Postcode.'); time.sleep(0.8)
		print('\x1bc')
		continue

print('Current weather for {}\n'.format(location))



import requests
import json
import time
from random import randint
from header import title
from bs4 import BeautifulSoup as soup

while True:
	title()
	try:
		postcode = input('\nPlease Enter a Valid UK Postcode (format: AB1 2CD): ')
		location = 'https://www.doogal.co.uk/UKPostcodes.php?Search='
		location_page=location+postcode
		fetch_location = requests.get(location_page)
		parse_location = soup(fetch_location.content, 'html.parser')
		location= parse_location.find('p').text.split('areas of')[1].split('.')[0]
		break
	except IndexError:
		print('Invalid Postcode, Please Try Again.\n')
		input('(Hit Enter)')

title()
print('\n\33[38;5;226mCurrent weather for{}'.format(location))
print('---------------------------------------------------')
page = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{}'.format(postcode)
current_weather = requests.get(page).json()
day = 0
forecast_and_reports_counter = 0
descriptions_counter = 0
timeout = 0

while day < 7:
	try:
		if descriptions_counter < 1:
			print('\r\33[38;5;202mThis is the forecast for {}'.format(current_weather['forecasts'][forecast_and_reports_counter]['detailed']['reports'][descriptions_counter]['localDate']),end='')
			print('\n---------------------------------------------------')
			error_flag = 0
	except KeyError:
		print('\r\33[38;5;{}mFetching Please Wait'.format(str(randint(0,255))), end='')
		current_weather = requests.get(page).json()
		error_flag = 1
		timeout += 1
		if timeout == 50:
			print('\nNot Found. Postcode is probably not an active post code')
			exit()
	if error_flag == 0:
		try:		
			print('\33[38;5;154mForecast: {} 		| Time Slot: {}	| Temp: {}'.format(current_weather['forecasts'][forecast_and_reports_counter]['detailed']['reports'][descriptions_counter]['enhancedWeatherDescription'], current_weather['forecasts'][forecast_and_reports_counter]['detailed']['reports'][descriptions_counter]['timeslot'], current_weather['forecasts'][forecast_and_reports_counter]['detailed']['reports'][descriptions_counter]['temperatureC']))
			descriptions_counter +=1
		except IndexError:
			forecast_and_reports_counter += 1
			descriptions_counter = 0
			day += 1
			input('\n\33[38;5;81mHit Enter for {}'.format(current_weather['forecasts'][forecast_and_reports_counter]['detailed']['reports'][descriptions_counter]['localDate']))
			title()
			print('\n\33[38;5;226mCurrent weather for{}'.format(location))
			print('---------------------------------------------------')
title()
print ('\nThat was your 7 day forecast')

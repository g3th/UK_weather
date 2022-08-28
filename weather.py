import requests
import json
import time
from header import title
from bs4 import BeautifulSoup as soup
#title()
error_flag =1
postcode = 'UB6 8JF' #input('\nPlease Enter a Valid UK Postcode: ')
location = 'https://www.doogal.co.uk/UKPostcodes.php?Search='
location_page=location+postcode
fetch_location = requests.get(location_page)
parse_location = soup(fetch_location.content, 'html.parser')
location= parse_location.find('p').text.split('areas of')[1].split('.')[0]

title()
print('\nCurrent weather for{}\n'.format(location))
page = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{}'.format(postcode)
current_weather = requests.get(page).json()


forecast_counter = 0


print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription'], current_weather['forecasts'][0]['detailed']['reports'][0]['timeslot']))
print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription'], current_weather['forecasts'][0]['detailed']['reports'][1]['timeslot']))
print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription'], current_weather['forecasts'][0]['detailed']['reports'][2]['timeslot']))
print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][1]['detailed']['reports'][0]['enhancedWeatherDescription'], current_weather['forecasts'][1]['detailed']['reports'][0]['timeslot']))
print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][1]['detailed']['reports'][1]['enhancedWeatherDescription'], current_weather['forecasts'][1]['detailed']['reports'][1]['timeslot']))
print('Forecast: {} | Time Slot {}'.format(current_weather['forecasts'][1]['detailed']['reports'][2]['enhancedWeatherDescription'], current_weather['forecasts'][1]['detailed']['reports'][2]['timeslot']))




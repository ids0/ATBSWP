#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, os, sys, requests, pprint

# Compute location from command line arguments. 

while False:
# if len(sys.argv) < 2:
    print('UsageL quickWeather.py location')
    sys.exit()

# location = ' '.join(sys.argv[1:])
location = 'London,UK'
API = 'No'
# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' %(location,API)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# pprint.pprint(weatherData)
# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
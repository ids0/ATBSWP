#! python3
# umbrellaReminder.py

import requests, json,pprint

import sys
sys.path.insert(0, r'D:\Drive\Code\Random')
import file
sys.path.insert(0, r'D:\Drive\Code\ATBSWP\Chapter_16')
import textMyself

location = file.myLocation
API = file.wheAPI
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API}'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
w = weatherData['list']

if w[1]['weather'][0]['main'] == 'Rain':
    weatherTom = w[1]['weather'][0]['main'] + ' - ' + w[1]['weather'][0]['description']
    textMyself.textmyself(weatherTom)
    print(weatherTom)
else:
    print('Umbrella not needed')




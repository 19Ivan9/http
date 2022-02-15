import requests
from bs4 import BeautifulSoup
import json
from pyowm import OWM
# tack1
url = 'https://pl.wikipedia.org/wiki/Pan'
req = requests.get(url)

with open('robots.txt', 'w', encoding='utf-8') as file:
    file.write(req.text)

# tack2

url = 'https://api.pushshift.io/reddit/comment/search/'
req = requests.get(url)
if req.ok:
    bs = BeautifulSoup(req.text, 'lxml')
    comments = bs.find('body')
    # print(comments.text)
    # with open('com.json', 'w') as file:
    #     json.dump(comments.text, file)
    with open('com.json', 'r') as file:
        temp = json.load(file)
    print(temp)


# # tack3

owm = OWM('cdb20d6a38445cc66fd75b8527fac7f6')
mgr = owm.weather_manager()

place = input('input place: ')
observation = mgr.weather_at_place(place)
w = observation.weather

print(f'In {place} city now : {w.detailed_status}\n{w.temperature("celsius")}')

#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.umass.edu/events/')
soup = BeautifulSoup(r.text, 'html.parser')

events = soup.find_all('div', class_='event-text')

for event in events:
    title = event.find('div', class_='views-field-title').find('a').string.strip()
    print(title)

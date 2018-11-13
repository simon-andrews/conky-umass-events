#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.cics.umass.edu/events')
soup = BeautifulSoup(r.text, 'html.parser')

events = soup.find_all('div', class_='view-event-wrapper')
for event in events:
    date = event.find('span', class_='date-display-single').string.strip()
    title = event.find('div', class_='views-field-title').find('a').string.strip()
    print(date + ': ' + title)

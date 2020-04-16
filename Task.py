import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv

# Set the URL you want to webscrape from
url = 'https://www.avito.ma/fr/maroc/v%C3%A9hicules-%C3%A0_vendre?o='



for page in range(3):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : "item li-hover"})


    for pt in  ancher:
        name = pt.find('h2', {'class': 'fs14 d-inline-block text-truncate'})
        price = pt.find('span', {'class': 'price_value'})
        date = pt.find('span', {'class': 'age-text'})
        city = pt.find('div', {'class': 're-text'})
        print('--------------------------------------------------')
        print('Title :' + name.text.replace('                    ', '').strip('\r\n'))
        print('City : ' + city.text.replace('                    ', '').strip('\r\n'))
        print('Price : ' + price.text)
        print('Date : ' + date.text.replace('                    ', '').strip('\r\n'))  
        print('--------------------------------------------------')
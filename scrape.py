# loading required packages
# import pandas as pd
from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# import datetime

import requests
import csv

url = 'https://en.wikipedia.org/wiki/Mobile_Web_Ghana'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.table.tbody.contents[1:-1]
# print(table.string)

f = csv.writer(open('mwgdata.csv', 'w'))
f.writerow(['Name', 'Link'])



for row in table:
    heading = row.th.string
    value = row.td.string
    print(str(heading) + " - " + str(value))
    # Add each artist’s name and associated link to a row
    f.writerow([str(heading), str(value)])
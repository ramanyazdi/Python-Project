import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/html/html_intro.asp'
r = requests.get(url) 
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find_all('h2')


for t in title:
    print(t.text)


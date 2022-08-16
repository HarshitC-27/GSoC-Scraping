import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
url = "https://summerofcode.withgoogle.com/programs/2022/organizations"
driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
time.sleep(5) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


all_divs = soup.find_all('div', {'class' : 'card'})

names=list()
links=list()
about=list()

for item in all_divs:
    names.append(item.find('div', {'class' : 'name'}).getText())
    links.append("https://summerofcode.withgoogle.com"+item.find('a').get('href'))
    about.append(item.find('div', {'class' : 'short-description'}).getText())

data = {'Names': names, 'Links': links, 'Short description': about};
df = pd.DataFrame(data) 
df.to_json('output.json')

# for item in all_divs:
#     print(item.find('div', {'class' : 'name'}).getText())
#     print("https://summerofcode.withgoogle.com"+item.find('a').get('href'))
#     print(item.find('div', {'class' : 'short-description'}).getText())

driver.close() # closing the webdriver
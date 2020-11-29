import pandas as pd
import requests # For downloading the website
from bs4 import BeautifulSoup # For parsing the website
import time # To put the system to sleep
import random # For random numbers
import country_converter as coco # To standardize country names

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Yelp DC restaurants url
DC_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Washington%2C%20DC'

# Download the webpage
DC_page = requests.get(DC_url)
DC_page.status_code # 200 == Connection

# Parse the content
DC_soup = BeautifulSoup(DC_page.content,'html.parser')

# Extract relevant links
links = set()

# body > yelp-react-root > div > div.spinnerContainer__09f24__2XcuX.border-color--default__09f24__R1nRO.background-color--white__09f24__2jFAt > div > div.leftRailContainer__09f24__3fttY.border-color--default__09f24__R1nRO > div.leftRailMainContent__09f24__1ncfZ.padding-r5__09f24__hWLOF.padding-b5__09f24__28TLK.padding-l5__09f24__3g2Ty.border-color--default__09f24__R1nRO > div.leftRailSearchResultsContainer__09f24__3vlwA.border-color--default__09f24__R1nRO > div:nth-child(2) > ul > li:nth-child(6) > div > div > div > div.arrange-unit__09f24__1gZC1.arrange-unit-fill__09f24__O6JFU.border-color--default__09f24__R1nRO > div:nth-child(1) > div > div.mainAttributes__09f24__26-vh.arrange-unit__09f24__1gZC1.arrange-unit-fill__09f24__O6JFU.border-color--default__09f24__R1nRO > div > div:nth-child(1) > div > div > h4 > span > a

for tag in DC_soup.select('span > a'):
    href = tag.attrs.get('href')
    if '?osq=Restaurants' in href and 'https:' not in href:
        links.update(['https://www.yelp.com'+href])

links

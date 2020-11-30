# Data processing
import pandas as pd
import country_converter as coco

# Scraping web content
import requests # For downloading the website
from bs4 import BeautifulSoup # For parsing the website
import time # To put the system to sleep
import random # For random numbers

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


# Extract page urls
DC_urls = set([DC_url])
DC_page_no = 24

for i in range(10, DC_page_no*10, 10):
    DC_urls.update([DC_url+'&start='+str(i)])

DC_urls


# Extract relevant links for one page
links = set()

# body > yelp-react-root > div > div.spinnerContainer__09f24__2XcuX.border-color--default__09f24__R1nRO.background-color--white__09f24__2jFAt > div > div.leftRailContainer__09f24__3fttY.border-color--default__09f24__R1nRO > div.leftRailMainContent__09f24__1ncfZ.padding-r5__09f24__hWLOF.padding-b5__09f24__28TLK.padding-l5__09f24__3g2Ty.border-color--default__09f24__R1nRO > div.leftRailSearchResultsContainer__09f24__3vlwA.border-color--default__09f24__R1nRO > div:nth-child(2) > ul > li:nth-child(6) > div > div > div > div.arrange-unit__09f24__1gZC1.arrange-unit-fill__09f24__O6JFU.border-color--default__09f24__R1nRO > div:nth-child(1) > div > div.mainAttributes__09f24__26-vh.arrange-unit__09f24__1gZC1.arrange-unit-fill__09f24__O6JFU.border-color--default__09f24__R1nRO > div > div:nth-child(1) > div > div > h4 > span > a

for tag in DC_soup.select('span > a'):
    href = tag.attrs.get('href')
    if '?osq=Restaurants' in href and 'https:' not in href:
        links.update(['https://www.yelp.com'+href])

links


# Build a scraper to extract relevant links
def page_scraper(urls=None,sleep=3):
    """
    Scrape a Yelp url.

    Args:
        urls (list): list of Yelp urls.
        sleep (int): integer value specifying how long the machine should be put to sleep (random uniform); defaults to 3.

    Returns:
        set: set containing all relevant restaurant links.
    """
    links = set()

    for url in urls:

        # Keep track of where we are at
        print(url)

        # Download the webpage
        page = requests.get(url)

        # If a connection was reached
        if page.status_code == 200:

                # Parse
                soup = BeautifulSoup(page.content,'html.parser')

                for tag in soup.select('span > a'):
                    href = tag.attrs.get('href')
                    if '?osq=Restaurants' in href and 'https:' not in href:
                        links.update(['https://www.yelp.com'+href])

        # Put the system to sleep for a random draw of time
        time.sleep(random.uniform(0,sleep))

    # Return data
    return links


# Scrape Yelp DC page
DC_links = page_scraper(urls=DC_urls)


# View DC_links
DC_links


# Check number of DC_links
len(DC_links)


# Create an empty DataFrame
Yelp_DC = pd.DataFrame(columns=['business_name','rating','review_count','price_category'])

for tag in DC_soup.select('[class*=container]'):
    if tag.find('h4'):
        Yelp_DC = Yelp_DC.append({'business_name':tag.select('h4')[0].get_text(),
                                  'rating':tag.select('[aria-label*=rating]')[0]['aria-label'],
                                  'review_count':tag.select('[class*=reviewCount]')[0].get_text(),
                                  'price_category':tag.select('[class*=priceCategory]')[0].get_text()},
                                 ignore_index=True)

Yelp_DC


# for tag in DC_soup.select('[class*=container]'):
#     if tag.find('h4'):
#         print(tag.select('h4')[0].get_text())
#         print(tag.select('[aria-label*=rating]')[0]['aria-label'])
#         print(tag.select('[class*=reviewCount]')[0].get_text())
#         print(tag.select('[class*=priceCategory]')[0].get_text())









# import json
# import ssl
# from urllib.request import Request, urlopen
#
# # For ignoring SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# # Yelp Ambar Arlington url
# Ambar_url = 'https://www.yelp.com/biz/ambar-arlington-4?osq=Restaurants'
#
# # Marking the website believe that you are accessing it using a mozilla browser
# req = Request(Ambar_url,headers={'User-Agent':'Mozilla/5.0'})
# webpage = urlopen(req).read()
#
# # Creating a BeautifulSoup obeject of the html page for easy extraction of data
# soup = BeautifulSoup(webpage,'html.parser')
# html_obj = soup.prettify('utf-8')
# business_details = {}
#
# for script in Ambar_soup.findAll('script', attrs={'type':'application/ld+json'}):
#     json_data = json.loads(script.text)
#     business_details["phone_number"] = json_data["telephone"]
#     business_details["address"] = json_data["address"]
#     business_details["rating"] = json_data["aggregateRating"]["ratingValue"]
#     business_details["reviewCount"] = json_data["aggregateRating"]["reviewCount"]
#     business_details["cuisine"] = json_data["servesCuisine"]










# -------------

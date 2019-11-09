"""
Use the BeautifulSoup and requests Python packages to
print out a list of all the article titles on the New York Times homepage.
"""
# https://www.nytimes.com
"""
Our plan should be as follows:

Use the requests library to load the HTML of the page into Python
Set up BeautifulSoup to process the HTML
Find out which HTML tags contain all the titles
Use BeautifulSoup to extract all the titles from the HTML
Format them nicely
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('http://nytimes.com')
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="css-1m5bs2v"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
"""
https://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

easy code
import requests
import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup.BeautifulSoup(requests.get(url).text)
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print ttl_lst
"""

# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com/'
r = requests.get(url)
htmlcon = r.content
print(htmlcon)

soup = BeautifulSoup(htmlcon, 'html.parser')
print(soup)

# prettifies the html code
print(soup.prettify())


# title of content
title = soup.title
print(title)


# all paragrph started with mentioned letter
paragraph = soup.find_all('p')
print(paragraph)


# all anchors in html page
anchhors = soup.find_all('a')
print(anchhors)


# for first paragraph
first_para = soup.find('p')
print(first_para)


# To find the class in paragraph
classin_para = soup.find_all('p'), ['class']
print(classin_para)


# to find only mentioned class in html content
print(soup.find_all('p', class_='lead'))


# get all text from html content
print(soup.get_text())


# get all text from mentioned paragraph
print(soup.find('p').get_text())


# get all links from anchor tags in html content

anchhors = soup.find_all('a')
all_link = set()
for link in anchhors:
    # print(link.get('href'))
    if link.get('href') != '#':

        links = 'https://www.codewithharry.com/' + link.get('href')
        all_link.add(links)

for i in all_link:
    print(i)


# for comments in html content
comment = '<p><!-- this is a comment --></p>'
soup2 = BeautifulSoup(comment)
print(soup2.p)

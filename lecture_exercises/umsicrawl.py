
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.si.umich.edu/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(baseurl, headers=header).text
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

content_div = page_soup.find_all(class_='view-content')
print (len(content_div)) # to see if there's more than one

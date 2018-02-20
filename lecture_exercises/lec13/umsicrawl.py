
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.si.umich.edu/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(baseurl, headers=header).text
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

content_div = page_soup.find(class_='view-content')
#print (len(content_div)) # to see if there's more than one


table_rows = content_div.find_all('tr')
for tr in table_rows:
    table_cells = tr.find_all('td')
    if len(table_cells) == 2:
     # extract course number and course name
     course_number = table_cells[0].text.strip()
     course_name = table_cells[1].text.strip()
     print(course_number, " : ", course_name)
     print('-' * 20)

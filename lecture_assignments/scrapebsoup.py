
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').text
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())


searching_div = soup.find(id='searching-the-tree')
#print(searching_div)


heads = searching_div.find_all(['h2',"h3"])


for h in heads:
    if h.name == 'h2':
        print(h.text)
    else:
        print("\t" + h.text) 
    


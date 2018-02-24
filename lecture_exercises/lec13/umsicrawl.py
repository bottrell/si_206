
import requests
from bs4 import BeautifulSoup
import json

# on startup, try to load the cache from file
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}


def get_unique_key(url):
  return url

# The main cache function: it will always return the result for this
# url+params combo. However, it will first look to see if we have already
# cached the result and, if so, return the result from cache.
# If we haven't cached the result, it will get a new one (and cache it)

def make_request_using_cache(url):
    header = {'User-Agent': 'SI_CLASS'}
    unique_ident = get_unique_key(url)

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]

class CourseListing:
    def __init__(self, course_num, course_name):
        self.num = course_num
        self.name = course_name

    def __str__(self):
        return self.num + ': ' + self.name + '\n\t' + self.description

    def init_from_details_url(self, details_url):
        page_text = make_request_using_cache(details_url)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        desc_elem = page_soup.find(class_='course2desc')
        self.description = desc_elem.text.strip()

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
page_text = make_request_using_cache(catalog_url)
page_soup = BeautifulSoup(page_text, 'html.parser')

content_div = page_soup.find(class_='view-content')

table_rows = content_div.find_all('tr')
course_listings = []
# for tr in table_rows:
for i in range(20):
    tr = table_rows[i]

    table_cells = tr.find_all('td')
    if len(table_cells) == 2:
        # extract info from this row
        course_number = table_cells[0].text.strip()
        course_name = table_cells[1].text.strip()


        # crawl over to the details page
        details_url_end = table_cells[0].find('a')['href']
        details_url = baseurl + details_url_end
        course_listing = CourseListing(course_number, course_name)
        course_listing.init_from_details_url(details_url)
        course_listings.append(course_listing)


for cl in course_listings:
    print(cl)
    print('-' * 20)
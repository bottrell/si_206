
import requests
from bs4 import BeautifulSoup



CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}

# A helper function that accepts 2 parameters
# and returns a string that uniquely represents the request
# that could be made with this info (url + params)
def get_unique_key(baseurl):
    return baseurl

# The main cache function: it will always return the result for this
# url+params combo. However, it will first look to see if we have already
# cached the result and, if so, return the result from cache.
# If we haven't cached the result, it will get a new one (and cache it)
def make_request_using_cache(baseurl, params):
    unique_ident = params_unique_combination(baseurl,params)

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(baseurl, params)
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
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
        str_ = self.num + ' ' + self.name + '\n\t'
        return str_

    def init_from_details_url(self, details_url):
        global header
        page_text = requests.get(details_url, headers=header).text
        page_soup = BeautifulSoup(page_text, 'html.parser')
        #self.description = page_soup.find(class_='course2desc').text

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(catalog_url, headers=header).text
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

content_div = page_soup.find(class_='view-content')
#print (len(content_div)) # to see if there's more than one
view_content_section = page_soup.find(class_='view-content')
table_rows = view_content_section.find_all('tr')

course_listings = []

for i in range(4):
	row = table_rows[i]
	cells = row.find_all('td')
	if len(cells) == 2:
		course_num = cells[0].text.strip()
		course_name = cells[1].text.strip()
		if course_name[-1] == ':':
			course_name = course_name[:-1]

		course_listing = CourseListing(course_num, course_name)
		details_url = baseurl + cells[0].find('a')["href"]
		course_listing.init_from_details_url(details_url)
		course_listings.append(course_listing)

for cl in course_listings:
	print(cl)


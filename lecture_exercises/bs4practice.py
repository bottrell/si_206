
# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')
all_list_items_and_all_divs = soup.find_all(['li','div'])

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')

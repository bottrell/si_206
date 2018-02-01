baseurl = "https://api.datamuse.com/words"
params_diction = {"rel_rhy": "blue"}
response = requests.get(baseurl, params_diction)

if you know that the response is going to be in json format,
response_data_struct = response.json()

otherwise response_body = response.text

caching usually consists of a dictionary with keys of querys and values of the results of those querys

#typical syntax for caching
CACHE_FNAME = 'cache_file_name.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}
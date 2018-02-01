baseurl = "https://api.datamuse.com/words"
params_diction = {"rel_rhy": "blue"}
response = requests.get(baseurl, params_diction)
import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"

    #Dictionary for Query Parameter
    params_diction = {}
    params_diction["rel_rhy"] = word
    params_diction["max"] = "5"

    resp = requests.get(baseurl, params=params_diction)
    word_ds = resp.json()
    #Converting the JSON File into a python representative Object (List in this case)

    return [d['word'] for d in word_ds]

print(get_rhymes("who"))
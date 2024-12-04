import requests

def get_meaning(string_val):
    baseurl = "https://api.datamuse.com/words"

    #Dictionary for Query Parameter
    params_diction = {}
    params_diction["ml"] = string_val
    params_diction["max"] = "1"

    resp = requests.get(baseurl, params=params_diction)
    print(resp.url)
    word_ds = resp.json()
    #Converting the JSON File into a python representative Object (List in this case)

    return [d['word'] for d in word_ds]

print(get_meaning("Someone who choreographs dances attuning certain sequences of steps and movements along music"))

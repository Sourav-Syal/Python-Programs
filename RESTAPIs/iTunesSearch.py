import requests

def track_names(singer, count_s = 0):

    itunes_base_url = "https://itunes.apple.com/search"
    itunes_p = {}

    itunes_p['term'] = singer
    itunes_p['media'] = "music"
    if count_s > 0:
        itunes_p['limit'] = str(count_s)

    itunes_response = requests.get(itunes_base_url, itunes_p)
    obj = itunes_response.json()
    print(itunes_response.url)

    return [dictionary['trackName'] for dictionary in obj['results']]

print(track_names("Hansraj Raghuwanshi", 4))




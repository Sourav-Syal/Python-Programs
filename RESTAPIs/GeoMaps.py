import json
import requests

api_key = 42
baseurl = 'http://py4e-data.dr-chuck.net/json'

while True:
    address = input('Enter Location:')
    if len(address) < 1: break

    payload = {}   #dictionary for query parameters
    payload['address'] = address
    payload['key'] = api_key

    r = requests.get(baseurl, params = payload)
    print('Retrieved from', r.url)

    #converting JSON oriented data into python representative object (Dictionary in this case)
    data = r.text
    js = json.loads(data)

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Fail to Retrieve')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
import urllib
import requests

main_api = "https://maps.googleapis.com/maps/api/geocode/json?"

address = 'lrh'
url = main_api + urllib.parse.urlencode({'address': address})

json_data = requests.get(url).json
print(json_data)

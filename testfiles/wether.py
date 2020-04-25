import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"lat":"0","units":"%22imperial%22","mode":"xml%2C html","q":"Alliston"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "bf8145af8emsh882cbe4cee55ea9p114679jsn9a97d316c12c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

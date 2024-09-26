import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f05fc31e62324eb71a755fa04b6f05cb"

weather_params = {
    "lat": 41.784851,
    "lon": -88.186279,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
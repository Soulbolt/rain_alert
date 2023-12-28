import requests

api_key = "c3786c1934232636bffda24c8eea4332"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
lat = 33.306160
lng = -111.841248

weather_params = {
    "lat": lat,
    "lon": lng,
    "appid": api_key,
    "cnt": 4,
}

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q=Chandler,AZ,01&appid={api_key}")
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lng}&appid={api_key}")
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
else:
    print("I guess is sunny today?")

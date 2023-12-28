import requests
from twilio.rest import Client # requires a twilio account to use this service(require account Id + auth token)

# We can add our main.py file to have automated through pythonanywhere.com
api_key = "c3786c1934232636bffda24c8eea4332"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
account_sid = "id goes here"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
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
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from="twilio_provided_number",
            to="your_phone_number",
        )

print(message.status)

import requests
import os
from twilio.rest import Client


#recovery code tw 1K7TKTGPRALEJZK7N1CYD86P
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ.get("OWN_API_KEY")

account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

# Params
weather_params = {
    "lat": -8.238020,
    "lon": -35.764469,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data_response = response.json()


will_rain = False

# getting the id weather and description weather
    # this code verify if is rain
for item in data_response["list"]:
    weather_id = item["weather"][0]["id"]
    if int(weather_id) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        # SMS
        # body="It's goin to rain today. Remember to bring an ☂️️.",
        # from_="+12762935848",
        # to="+5581999056534'",

        # Whatsapp
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an ☂️",
        to="whatsapp:+558199056534"
    )
    print(message.status)





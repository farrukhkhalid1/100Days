import requests
from twilio.rest import Client

Parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "exclude": "current,minutely,daily",
    "appid": "05775a798733142d641d8e7ba1673b17",
}
# after creating twilio account
account_sid = 'your account id here'
auth_token = 'your twilio token here'

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=Parameters)
response.raise_for_status()
data = response.json()

hourly_data = data["hourly"][:13]
id = [x["weather"][0]["id"] for x in hourly_data]

will_rain = False

for i in id:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(to="Your Number", from_='Else num', body='Good Day')

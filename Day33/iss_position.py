import requests
import datetime as dt
import smtplib

my_lat = 40
my_long = -120


def iss_position_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    print(latitude,longitude)
    if my_lat - 5 <= latitude <= my_lat + 5 and my_long - 5 <= longitude <= my_long + 5:
        return True


def is_nighttime():
    parameters = {
        "lat": my_lat,
        "long": my_long,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    now = dt.datetime.now().hour

    if now <= sunrise or now >= sunset:
        return True


if iss_position_nearby() and is_nighttime():
    print("look up")

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login("blabla@gmail.com", "1234")
    #     connection.sendmail(
    #         from_addr="blabla@gmail.com",
    #         to_addrs="blabla@gmail.com",
    #         msg="Subject:Look up \n\nThe ISS is above you."
    #     )

import requests
from datetime import datetime

# part1
# set it to your username&token
url = "https://pixe.la/v1/users"
TOKEN = "your token"
USERNAME = "your username"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=url,json=parameters)
# print(response.text)
# part2
# set it to your username
graph_url = "https://pixe.la/v1/users/username/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers_s = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_url,json=graph_parameters, headers = headers_s)
# print(response.text)
# part3
today = datetime.today()
today = f"{today.year}{today.month}{today.day}"

pixel_parameters = {
    "date": today,
    "quantity": input("How many kms did you cycled?"),
}

pixel_url = f"{graph_url}/graph1"

response = requests.post(url=pixel_url, json=pixel_parameters, headers=headers_s)
print(response.text)

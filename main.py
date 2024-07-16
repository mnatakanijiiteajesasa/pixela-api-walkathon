import requests
from datetime import datetime

TOKEN = 'hhhdjhdfavhjcusvskjn'
USERNAME = 'diggy'
GRAPHID = "walkathon2"
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": 'walkathon2',
    "name": 'Walking Graph',
    "unit": 'Km',
    "type": 'float',
    "color": 'kuro',
}
header = {
    "X-USER-TOKEN": 'hhhdjhdfavhjcusvskjn'
}
# responses = requests.post(url=graph_endpoint,json=graph_params, headers=header)
# print(responses.text)
today = datetime(year=2024, month=5, day=1)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18",
}
header = {
    "X-USER-TOKEN": "hhhdjhdfavhjcusvskjn"
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=header)
# print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
put_params = {
    "quantity": "20"
}
head = {
    "X-USER-TOKEN": "hhhdjhdfavhjcusvskjn"
}

responses = requests.put(url=pixel_put_endpoint, json=put_params, headers=head)
print(responses.text)

app_id ="9b82840e"
api_key= '1464b0f0d970aafb799b528883b38a9a'




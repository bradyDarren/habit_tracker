import requests

PIXELA_URL = 'https://pixe.la/v1/users'

user_params = {
    'token':'abcd1234',
    'username':"darrenb",
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

response = requests.post(url=PIXELA_URL, json=user_params)
print(response.text)
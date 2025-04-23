import requests
from datetime import datetime

PIXELA_TOKEN = 'abcd1234'
USERNAME = 'darrenb'

PIXELA_URL = 'https://pixe.la/v1/users'

# creation of the pixela user account
user_params = {
    'token':PIXELA_TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=PIXELA_URL, json=user_params)

# creation of a graph wiht in our pixela account
GRAPH_URL = f'{PIXELA_URL}/{USERNAME}/graphs'

graph_params = {
    'id':'graph1',
    'name':'Workout Graph',
    'unit':'minutes',
    'type':'int',
    'color':'ajisai',
    'startOnMonday': True, 
}

graph_headers = {
    'X-USER-TOKEN':PIXELA_TOKEN
}

# graph = requests.post(url=GRAPH_URL, json=graph_params, headers=graph_headers)
# print(graph.text)

# posting of a pixel onto the above graph

PIXEL_UPDATE_URL = f'{PIXELA_URL}/{USERNAME}/graphs/graph1'

pixel_header = {
    'X-USER-TOKEN':PIXELA_TOKEN
}

today = datetime.now()

pixel_posting_params = {
    'date':today.strftime('%Y%m%d'),
    'quantity':'250',
}

# pixel = requests.post(url=PIXEL_UPDATE_URL, json=pixel_posting_params, headers=pixel_header)
# print(pixel.text)

# usng the put method to update a previous post
PIXEL_ADJUSTMENT_URL = f'{PIXELA_URL}/{USERNAME}/graphs/graph1/20250422'

pixel_adjustment_params = {
    'quantity':'125'
}

adjustment = requests.put(url=PIXEL_ADJUSTMENT_URL, json=pixel_adjustment_params, headers=pixel_header)
print(adjustment.text)




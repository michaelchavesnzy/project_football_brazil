import requests 
import pandas as pd

url = "https://api.football-data.org/v4/competitions/BSA/teams"
headers = {"X-Auth-Token": "177399c00efe422ba957c9a8ef28b832"}

response = requests.get(url=url,headers=headers)

data = response.json()

df = pd.json_normalize(data['teams'])


df_ = pd.json_normalize(data['squad'])


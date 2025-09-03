import requests 
import pandas as pd

url = " "
headers = {"X-Auth-Token": "177399c00efe422ba957c9a8ef28b832"}

response = requests.get(url=url,headers=headers)

data = response.json()

df = pd.json_normalize(data['matches'])

df.loc[df.id == 535153][['homeTeam.name', 'awayTeam.name', 'score.winner']]

df.loc[(df['awayTeam.name'] == 'Ceará SC') | (df['homeTeam.name'] == 'Ceará SC')][['homeTeam.name', 'awayTeam.name', 'score.winner']]
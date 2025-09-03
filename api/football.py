import requests
from config.settings import FOOTBALL_API_URL, FOOTBALL_API_TOKEN

class FootballApi:

    def __init__(self):
        self.base_url = FOOTBALL_API_URL
        self.headers = {"X-Auth-Token": FOOTBALL_API_TOKEN}

    def api_request(self, endpoint):
        
        url = self.base_url+endpoint
        response = requests.get(url=url,headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Erro: ", response.status_code, response.text)
            return None
        
    def get_teams(self):

        return self.api_request("competitions/BSA/teams")

    def get_standings(self):

        return self.api_request("competitions/BSA/standings")
    
    def get_matches(self):

        return self.api_request("ompetitions/BSA/matches")

    
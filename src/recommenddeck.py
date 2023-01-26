import requests
import json
class RecommendDeck():
    def __init__(self):
        self.url="https://raw.githubusercontent.com/PilotSherlock/b4bRecommendDeck/master/recommend.json"


    def get_recommend_deck(self):
        try:
            response = requests.get(self.url)
            return json.loads(response.content)
        except:
            return None


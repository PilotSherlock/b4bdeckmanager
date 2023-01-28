import requests
import json
class RecommendDeck():
    def __init__(self):
        self.url_cn_zh="https://raw.githubusercontent.com/PilotSherlock/b4bRecommendDeck/master/recommend.json"
        self.url_en="https://raw.githubusercontent.com/PilotSherlock/b4bRecommendDeck/master/recommend_en.json"

    def get_recommend_deck(self,language="cn_zh"):
        try:
            if language=="cn_zh":
                response = requests.get(self.url_cn_zh)
                return json.loads(response.content)
            elif language == "en":
                response = requests.get(self.url_en)
                return json.loads(response.content)
        except:
            return None


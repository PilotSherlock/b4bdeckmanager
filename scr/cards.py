import json
import os
import codecs

class CardsSet():
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/cardSet.json"):
            with open('data/cardSet.json',"w") as file:
                self.cards = dict()
                json.dump(self.cards,file,ensure_ascii=False)
        else:
            self.cards = dict()
            with open('data/cardSet.json',"r",encoding="utf-8") as file:
                self.cards = json.load(file)

    def update(self):
        with codecs.open('data/cardSet.json',"w","utf-8") as file:
            json.dump(self.cards,file,ensure_ascii=False)
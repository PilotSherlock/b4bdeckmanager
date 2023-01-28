from src.ppocr import PPOCR

class Ocr(PPOCR):
    def __init__(self):
        super().__init__("./PaddleOCR-json/PaddleOCR_json.exe --use_debug=0")
    def to_list(self,path):
        return [card['text'] for card in self.run(path)['data']]

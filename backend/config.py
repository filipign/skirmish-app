import json
import os

class Config():
    def __init__(self, path=os.path.abspath('./backend/config.json')):
        if '/backend/backend' in path:
            path = os.path.abspath('./config.json')
        self.config = { }
        with open(path) as file_handler:
            self.config = json.load(file_handler)

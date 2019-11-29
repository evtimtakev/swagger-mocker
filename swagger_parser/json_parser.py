import json


class JsonParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse_json(self):
        """Parse json and get all api endpoints"""
        endpoints = {}

        with open(self.file_path) as f:
            data = json.load(f)

        paths = data['paths']

        endpoints = {key: [k.upper() for k in paths[key]] for key in paths}

        return endpoints

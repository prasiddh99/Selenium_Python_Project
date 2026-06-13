import json


def get_test_data():
    with open("data/credentials1.json") as file:
        return json.load(file)

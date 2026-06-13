import json


def get_test_data():
    with open("Main_demoblaze_automation/data/credentials1.json") as file:
        test_data = json.load(file)
        return test_data

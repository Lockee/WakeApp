import json

filepath = './wakeapp/data/data.json'

def safe_to_json(data: object, filepath: str):
    with open(filepath, "w") as outfile:
        json.dump(data, outfile)

def load_from_json(filepath: str) -> object:
    with open(filepath) as json_file:
        data = json.load(json_file)
    return data

testobj = {
    "Hallo": "Blub",
    "bye": "slub"
}

safe_to_json(testobj)
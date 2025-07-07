import json
import os

def load_hospitals():
    file_path = os.path.join("hospitals_data", "hospitals.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_hospitals_by_district(district):
    data = load_hospitals()
    return data.get(district.lower(), [])

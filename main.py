import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT_KG = 73
HEIGHT_CM = 175
AGE = 22

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

exercise_name = result["exercises"][0]["name"].title()
exercise_duration = result["exercises"][0]["duration_min"]
exercise_calories = result["exercises"][0]["nf_calories"]

dt = datetime.now()

sheet_api = os.environ["sheet_api"]

TOKEN = os.environ["TOKEN"]
headers = {
    "Authorization": TOKEN
}

sheet_params = {
    "workout": {
        "date": dt.strftime("%d/%m/%Y"),
        "time": dt.strftime("%X"),
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

response = requests.post(url=sheet_api, json=sheet_params, headers=headers)
print(response.json())
import requests
from datetime import datetime
APP_ID = 'your app id'
API_KEY = 'your api key'
GENDER = 'your gender'
WEIGHT_KG = 'your weight'
HEIGHT_CM = 'your height'
AGE = 'your age'


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
date = datetime.now()
sheet_endpoint = 'https://api.sheety.co/username/projectName/sheetName'
for exercise in result["exercises"]:
    sheet_inputs = {
        'workout': {
            'date': date.strftime('%d/%m/%Y'),
            'time': date.strftime('%H:%M:%S'),
            'exercise': result['exercises'][0]['user_input'].title(),
            'duration': result['exercises'][0]['duration_min'],
            'calories': result['exercises'][0]['nf_calories']
        }
    }

bearer_headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
print(sheet_response.text)

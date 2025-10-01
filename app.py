import datetime
import pywhatkit as kit
import requests
import os

# Store sensitive data in environment variables
api_key = os.getenv("AIRVISUAL_API_KEY", "YOUR_API_KEY_HERE")   #"72eddaac-b2c7-456f-85b1-ee850493d94b"
group_id = os.getenv("WHATSAPP_GROUP_ID", "YOUR_GROUP_ID_HERE") #"E6wGO5tFFRcKlxO8tOHpWj"

base_url = "https://api.airvisual.com/v2"
endpoint = f"{base_url}/city"
params = {"city": "Dhaka", "state": "Dhaka", "country": "Bangladesh", "key": api_key}

try:
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    data = response.json()
    aqi = data.get('data', {}).get('current', {}).get('pollution', {}).get('aqius')

    if aqi is None:
        raise ValueError("AQI data not found in API response")

    print(f"Fetched AQI for Dhaka: {aqi}")
    now = datetime.datetime.now()
    time_hour = now.hour
    time_min = now.minute + 1
    if time_min == 60:
        time_hour = (time_hour + 1) % 24
        time_min = 0

    message = f"Dhaka AQI Update: {aqi}"
    kit.sendwhatmsg_to_group(
        group_id=group_id,
        message=message,
        time_hour=time_hour,
        time_min=time_min,
        wait_time=10
    )

except Exception as e:
    print(f"An error occurred: {e}")


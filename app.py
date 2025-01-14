import datetime
import pywhatkit as kit
import requests

api_key = "72eddaac-b2c7-456f-85b1-ee850493d94b"
base_url = "https://api.airvisual.com/v2"
group_id = "E6wGO5tFFRcKlxO8tOHpWj"

endpoint = f"{base_url}/city"
params = {
    "city": "Dhaka",
    "state": "Dhaka",
    "country": "Bangladesh",
    "key": api_key
}

try:
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    data = response.json()
    aqi = data.get('data', {}).get('current', {}).get('pollution', {}).get('aqius')
    print(aqi)


    # Get the current time
    now = datetime.datetime.now()

    # Set the time a few seconds in the future
    time_hour = now.hour
    time_min = (now.minute + 1) % 60

    kit.sendwhatmsg_to_group(
        group_id=group_id,  # Replace with your actual group ID
        message="Dhaka AQI(TEST)! " + str(aqi),
        time_hour=time_hour,
        time_min=time_min,
        wait_time=10  # Seconds to wait before sending
    )

except requests.exceptions.RequestException as e:
    print(f"Error fetching AQI data: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
# Air Quality Index (AQI) Notifier for Dhaka

This project is a simplified version of a real-world script originally developed for a real estate company. The original application was used internally to raise environmental awareness among employees and to showcase the company’s commitment to sustainability in front of clients.

This open-source edition is shared as a learning resource and a practical example that can be adapted for similar awareness-driven use cases. 

The program fetches the current Air Quality Index (AQI) for Dhaka, Bangladesh, using the AirVisual API, and sends the AQI information as a WhatsApp message to a specified group via the pywhatkit library.

## Prerequisites

- Python 3.x
- `pywhatkit` library
- `requests` library

## Setup

1. **API Key**: Obtain your API key from [AirVisual](https://www.iqair.com/).
2. **Group ID**: Get the ID of the WhatsApp group where you want to send the message.

## Installation

To install the required libraries, use:

```bash
pip install pywhatkit requests
```

## Usage

Replace the placeholders in the script with your actual API key and group ID. Then, run the script to fetch the AQI and send the message.

```python
import datetime
import pywhatkit as kit
import requests

api_key = "YOUR_API_KEY"
base_url = "https://api.airvisual.com/v2"
group_id = "YOUR_GROUP_ID"

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
        group_id=group_id,
        message="Dhaka AQI(TEST)! " + str(aqi),
        time_hour=time_hour,
        time_min=time_min,
        wait_time=10  # Seconds to wait before sending
    )

except requests.exceptions.RequestException as e:
    print(f"Error fetching AQI data: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## 🚀 Use Cases for Dhaka AQI WhatsApp Notifier
This Python script automatically fetches Dhaka's AQI and broadcasts it to a WhatsApp group, providing timely environmental information.

Here are its key use cases:

* Public Health Awareness: Alerts communities, schools, and workplaces about air quality for health precautions and activity planning.
* Environmental Monitoring: Provides automated AQI updates for enthusiasts and advocacy groups, aiding informal data tracking.
* Personal & Family Safety: Delivers direct AQI alerts for personal health management and caregiver notifications.
* Smart City & IoT Integration (Conceptual): Potential for basic integration with environmental sensors for real-time data dissemination.
* Event Planning: Helps outdoor event organizers monitor air quality for attendee safety and adjustments.

This script offers a simple, effective solution for sharing vital air quality information via WhatsApp.

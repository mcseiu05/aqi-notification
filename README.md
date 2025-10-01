# Air Quality Index (AQI) Notifier for Dhaka

A real estate company wanted a simple but meaningful way to raise awareness about air quality among their team and clients. They believed that by sharing daily updates on environmental conditions, they could both encourage healthier habits internally and highlight their commitment to sustainability externally.

To support this idea, I created a script that automatically fetches the Air Quality Index (AQI) for Dhaka from the AirVisual API and delivers the information directly to a WhatsApp group using the pywhatkit library. Employees receive these updates daily, and the company uses it as a small but impactful step to show that they care about the environment.

This repository contains a simplified version of that script — free of company-specific details — so others can learn from it and adapt it for their own awareness-driven initiatives.

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
import os

import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("AIRVISUAL_API_KEY")
group_id = os.getenv("WHATSAPP_GROUP_ID")

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

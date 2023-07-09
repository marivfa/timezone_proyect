import requests
import os
from dotenv import load_dotenv

from src.crud.timezone import save_error_log

load_dotenv()

API_BASE_URL = str(os.getenv('API_BASE_URL'))
API_KEY = str(os.getenv('API_KEY'))

def get_timezones_api():
    try:
        url = f'{API_BASE_URL}list-time-zone?key={API_KEY}&format=json'
        response = requests.get(url)
        data = response.json()
        if "zones" in data:
            timezones = [
                {
                    'countrycode': tz['countryCode'], 
                    'countryname': tz['countryName'], 
                    'zonename': tz['zoneName'],
                    'gmtoffset' : tz['gmtOffset']
                } 
                for tz in data['zones']]
            return timezones
        else:
            error_message = "Failed to retrieve timezones from the API"
            save_error_log(error_message)
            return None
    except requests.RequestException as e:
        error_message = f"RequestException: {str(e)}"
        save_error_log(error_message)
        return None
    except ValueError as e:
        error_message = f"ValueError: {str(e)}"
        save_error_log(error_message)
        return None



def get_timezones_detail_api(zone):
    try:
        url = f'{API_BASE_URL}get-time-zone?key={API_KEY}&format=json&by=zone&zone={zone}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and "status" in data and data["status"] == "OK":
            zone_details = {
                'countrycode': data['countryCode'],
                'countryname': data['countryName'],
                'zonename': data['zoneName'],
                'gmtoffset': data['gmtOffset'],
                'dst': int(data['dst']),
                'zonestart': int(data['zoneStart']) if data['zoneStart'] else 0,
                'zoneend': int(data['zoneEnd']) if data['zoneEnd'] else 0
            }
            return zone_details
        else:
            error_message = f"Failed to retrieve zone details for {zone}: {data['message']}"
            save_error_log(error_message)
            return None
    except requests.RequestException as e:
        error_message = f"RequestException: {str(e)} | Zone {zone}"
        save_error_log(error_message)
        return None
    except ValueError as e:
        error_message = f"ValueError: {str(e)}"
        save_error_log(error_message)
        return None

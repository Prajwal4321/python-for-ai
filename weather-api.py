import requests

def get_weather(lat, lon):
    # API URL for Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Using a 'params' dictionary is cleaner than f-strings for URLs
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "timezone": "auto"
    }

    try:
        # 1. Use a timeout to prevent the script from hanging
        response = requests.get(url, params=params, timeout=10)
        
        # 2. Raise an error if the request failed (e.g., 404 or 500)
        response.raise_for_status()
        
        data = response.json()

        # 3. Extract specific data points for a clean output
        temp = data["current"]["temperature_2m"]
        unit = data["current_units"]["temperature_2m"]
        
        print(f"--- Weather Report ---")
        print(f"Location: {lat}, {lon}")
        print(f"Current Temp: {temp}{unit}")
        print(f"----------------------")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Paris Coordinates
    get_weather(48.85, 2.35)

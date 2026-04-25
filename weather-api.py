import requests

def weath(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

bangalore_temp = weath(12.9719, 77.5937)

print (f"The current temperature in Bangalore is: {bangalore_temp}°C")



#update weather api code
import requests
import pandas as pd #to organize data
import matplotlib.pyplot as plt #for visualization
import os 
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)
# Format dates for API (DD-MM-YYYY)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
# Get B'lore weather
url = f"https://api.open-meteo.com/v1/forecast?latitude=12.9719&longitude=77.5937&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
#print(data)

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')
# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Bangalore Weather - Past 7 Days')
plt.legend()
# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot
plt.savefig('weather_chart.png')
plt.show()

df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2


if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/b-lore_weather.csv', index=False)

print(f"Average temperature: {df['avg_temp'].mean():.1f}°C")

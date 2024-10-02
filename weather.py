import requests
import json
from datetime import datetime

def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "forecast_days": 1
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        current = weather_data["current"]
        print("\nCurrent Weather:")
        print(f"Temperature: {current['temperature_2m']}°C")
        print(f"Relative Humidity: {current['relative_humidity_2m']}%")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")

        print("\nHourly Forecast:")
        hourly = weather_data["hourly"]
        for i in range(24):
            time = datetime.fromisoformat(hourly["time"][i]).strftime("%H:%00")
            temp = hourly["temperature_2m"][i]
            humidity = hourly["relative_humidity_2m"][i]
            wind = hourly["wind_speed_10m"][i]
            print(f"{time}: {temp}°C, {humidity}% humidity, {wind} km/h wind")
    else:
        print("Unable to fetch weather data.")

def main():
    print("Welcome to the Weather Forecast Application!")
    
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")

    weather_data = get_weather(latitude, longitude)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
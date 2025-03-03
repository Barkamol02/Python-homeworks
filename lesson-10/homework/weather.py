import requests

API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  
}


response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    
   
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print(f"Error fetching data: {response.status_code} - {response.text}")

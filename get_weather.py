
import requests

# Replace with your actual OpenWeatherMap API key
OPENWEATHER_API_KEY = "your_api_key_here"
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location: str) -> dict:
    """Fetch current weather data for a given location using OpenWeatherMap API."""
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(OPENWEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            "location": data.get("name"),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].capitalize()
        }
        return weather_info

    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    location = input("Enter a city name: ")
    result = get_weather(location)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\nWeather in {result['location']}:")
        print(f"- Description: {result['description']}")
        print(f"- Temperature: {result['temperature']}°C (Feels like {result['feels_like']}°C)")
        print(f"- Humidity: {result['humidity']}%")
        print(f"- Wind Speed: {result['wind_speed']} m/s")
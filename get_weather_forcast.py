import requests

# Set your API key here
OPENWEATHER_API_KEY = "your_api_key"
OPENWEATHER_FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather_forecast(location: str, hours_ahead: int) -> dict:
    """
    Retrieves the forecasted weather for a specified city and number of hours into the future.
    """
    if hours_ahead is None:
        hours_ahead = 24

    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(OPENWEATHER_FORECAST_URL, params=params)
        response.raise_for_status()
        data = response.json()

        idx = hours_ahead // 3  # 3-hour forecast intervals
        forecast_entry = data["list"][idx]

        return {
            "forecast_time": forecast_entry["dt_txt"],
            "location": data["city"]["name"],
            "temperature": forecast_entry["main"]["temp"],
            "feels_like": forecast_entry["main"]["feels_like"],
            "humidity": forecast_entry["main"]["humidity"],
            "wind_speed": forecast_entry["wind"]["speed"],
            "description": forecast_entry["weather"][0]["description"].capitalize()
        }

    except requests.RequestException as e:
        return {"error": str(e)}


# --- Test it ---
if __name__ == "__main__":
    city = input("Enter a city name: ")
    hours = int(input("How many hours ahead? (e.g., 24): "))

    result = get_weather_forecast(city, hours)
    print("\n📊 Forecast Result:")
    for key, value in result.items():
        print(f"{key}: {value}")
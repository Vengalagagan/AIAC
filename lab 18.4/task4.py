import requests

def get_weather():
    """
    Fetch and display weather details for a given city using the OpenWeatherMap API.
    Takes API key and city name as user input.
    """
    # Get user input
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city_name = input("Enter city name: ").strip()

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }

    try:
        # Send request to API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for bad HTTP status codes

        # Parse JSON data
        data = response.json()

        # Extract and display weather details
        city = data.get('name', 'Unknown')
        country = data['sys'].get('country', 'N/A')
        temp = data['main'].get('temp', 'N/A')
        feels_like = data['main'].get('feels_like', 'N/A')
        humidity = data['main'].get('humidity', 'N/A')
        description = data['weather'][0].get('description', 'N/A').title()

        print(f"\n🌤️ Weather Details for {city}, {country}")
        print("-" * 40)
        print(f"🌡️ Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌦️ Condition   : {description}")
        print("-" * 40)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"❌ City '{city_name}' not found. Please check the name and try again.")
        elif response.status_code == 401:
            print("🔒 Invalid API key. Please verify your API credentials.")
        else:
            print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("🌐 Network error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⏳ The request timed out. Try again later.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
get_weather()

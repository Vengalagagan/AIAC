import requests
import json
import os

def get_weather_json():
    """
    Fetch and display weather details of a city using the OpenWeatherMap API.
    Displays the result as JSON and appends it to a text file in the current directory.
    Includes robust error handling.
    """
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city_name = input("Enter city name: ").strip()

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract required weather details
        weather_details = {
            "City": data.get('name', 'N/A'),
            "Temperature (°C)": data['main'].get('temp', 'N/A'),
            "Humidity (%)": data['main'].get('humidity', 'N/A'),
            "Weather": data['weather'][0].get('description', 'N/A').title()
        }

        # Display weather details as JSON
        json_output = json.dumps(weather_details, indent=4)
        print("\nWeather Details (JSON Output):")
        print(json_output)

        # Append to a text file
        file_path = os.path.join(os.getcwd(), "weather_log.txt")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(json_output + "\n\n")

        print(f"\n✅ Weather details appended to: {file_path}")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("\nError: City not found. Please enter a valid city.")
        elif response.status_code == 401:
            print("\nError: Invalid API key. Please check your API key.")
        else:
            print(f"\nError: Unable to fetch data (HTTP {response.status_code}).")
    except requests.exceptions.RequestException:
        print("\nError: Network issue. Please check your internet connection.")
    except Exception as e:
        print(f"\nError: {e}")


# Run the function
get_weather_json()

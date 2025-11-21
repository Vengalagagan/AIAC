import requests
import json

def get_weather_data():
    # Ask user for city name first, then API key
    city = input("Enter city name: ").strip()
    api_key = input("Enter your OpenWeatherMap API key: ").strip()

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Parse the JSON response
        weather_data = response.json()
        
        # Extract specific fields
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        
        # Display the data in a user-friendly format
        print("\n--- Weather Report ---")
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    get_weather_data()

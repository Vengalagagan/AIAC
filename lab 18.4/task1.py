import argparse
import os
import requests
import json
import sys
def display_weather(city: str, api_key: str) -> int:
    """Fetch and print weather for `city` from OpenWeatherMap.
    Returns:
        int: Exit code 0 on success, non-zero on error."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()  # raise for HTTP errors (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Network / request error: {e}", file=sys.stderr)
        return 2
    try:
        data = resp.json()
    except ValueError:
        print("Failed to parse JSON response.", file=sys.stderr)
        return 3
    # If OpenWeatherMap returns a 200 but with an error payload (rare), show message
    if resp.status_code != 200 or data.get("cod") not in (200, "200"):
        message = data.get("message", resp.text)
        print(f"API error ({resp.status_code}): {message}", file=sys.stderr)
        return 4
    print(json.dumps(data, indent=2))
    return 0
def main(argv=None):
    parser = argparse.ArgumentParser(description="Show weather using OpenWeatherMap API.")
    parser.add_argument("city", nargs="?", help="City name (e.g. London)")
    parser.add_argument("api_key", nargs="?", help="OpenWeatherMap API key")
    args = parser.parse_args(argv)
    city = args.city or input("City: ").strip()
    api_key = args.api_key or os.environ.get("OPENWEATHER_API_KEY") or input("OpenWeatherMap API key: ").strip()
    if not city:
        print("City is required.", file=sys.stderr)
        return 1
    if not api_key:
        print("API key is required (pass as argument or set OPENWEATHER_API_KEY).", file=sys.stderr)
        return 1
    return display_weather(city, api_key)
if __name__ == "__main__":
    sys.exit(main())
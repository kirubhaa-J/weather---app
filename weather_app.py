import requests

# Your OpenWeather API Key (replace this with your key)
api_key = "f44e5936530cc1724e3463e9aeb13057"  # Use your own API key here!

# Get city name from the user
city = input("Enter city name: ")

# API URL with the city and API key
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Make the API request
response = requests.get(api_url)

# If the request is successful
if response.status_code == 200:
    data = response.json()
    
    # Get specific weather data from the API response
    city_name = data["name"]
    temperature = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    # Display the weather data to the user
    print(f"\nCity: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_desc}")
    print(f"Humidity: {humidity}%")
else:
    print("City not found, please try again.")
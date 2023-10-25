import requests

api_key = '899a03dc1228f7b8ccdeee9e3a4cb1c5'

def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def convert_kelvin_to_celsius(temp):
    return temp - 273.15


while True:
    print("Options:")
    print("1. Enter a city name")
    print("2. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        city = input("Enter the city name: ")
    elif choice == '2':
        print("Exiting the weather application.")
        break
    else:
        print("Invalid choice. Please enter 1or 2.")
        continue

    weather_data = fetch_weather(api_key, city)

    if 'weather' in weather_data:
        weather = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']
        temp = round(convert_kelvin_to_celsius(temp), 2)
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp}°C")
    else:
        print(f"Weather data for {city} not found.")

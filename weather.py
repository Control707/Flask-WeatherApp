from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city="London"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    pprint(weather)
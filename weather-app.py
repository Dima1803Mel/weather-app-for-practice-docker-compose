import requests

API_KEY = "7e7b169fa1aec31eb0da2b1399d30739"
CITY = "Vladimir"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Weather in {CITY}: {temp}°C, {desc}")
else:
    print(f"Error {response.status_code}: {response.text}")
import requests

API_KEY = "Your_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

responce = requests.get(requests_url)

if responce.status_code == 200:
    data = responce.json()
    weather = data['weather'][0]['description']
    temperarture = round(data['main']['temp'] - 273.15,2)
    print("Weather:",weather)
    print("Temperature:",temperarture,"celsius")
    
else:
    print("an error occured")
import requests

city = input("Enter city: ").title()

api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if "main" in data:
    print("\n📍 City:", city)
    print("🌡 Temperature:", data["main"]["temp"], "°C")
    print("💧 Humidity:", data["main"]["humidity"], "%")
    print("🌤 Weather:", data["weather"][0]["main"])
else:
    print("❌ City not found, try again")

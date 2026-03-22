import requests

api_key = "YOUR_API_KEY"

cities = input("Enter cities (comma separated): ").title()
city_list = cities.split(",")

for city in city_list:
    city = city.strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "main" in data:

        temp = data["main"]["temp"]

        if temp > 30:
            status = "🔥 Hot"
        elif temp < 15:
            status = "❄ Cold"
        else:
            status = "🙂 Normal"

        print("\n📍 City:", city)
        print("🌡 Temp:", temp, "°C |", status)

    else:
        print("❌ Error in", city)

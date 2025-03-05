from bs4 import BeautifulSoup


with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")[1:]
weather_data = []
temperatures = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))  
    condition = cols[2].text.strip()

    weather_data.append({"Day": day, "Temperature": temp, "Condition": condition})
    temperatures.append(temp)

print("\n 5-Day Weather Forecast:")
for data in weather_data:
    print(f"{data['Day']}: {data['Temperature']}°C - {data['Condition']}")


hottest_temp = max(temperatures)
hottest_days = [data["Day"] for data in weather_data if data["Temperature"] == hottest_temp]

print(f"\n Hottest Day(s): {', '.join(hottest_days)} ({hottest_temp}°C)")

sunny_days = [data["Day"] for data in weather_data if data["Condition"] == "Sunny"]

print(f"\n Sunny Days: {', '.join(sunny_days)}")

avg_temp = sum(temperatures) / len(temperatures)
print(f"\n Average Temperature for the Week: {avg_temp:.2f}°C")

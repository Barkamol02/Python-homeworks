import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.demoblaze.com")
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

laptops = []

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("div", class_="card-block")

    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})

    try:
        next_button = driver.find_element(By.ID, "next2")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
    except:
        break

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=2)

print(" Data saved to laptops.json")

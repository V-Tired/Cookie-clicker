from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""A cookie clicker web-driver. Runs for 5 minutes"""

url = 'https://orteil.dashnet.org/cookieclicker/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(3)
language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language.click()
time.sleep(3)
cookie = driver.find_element(By.ID, value="bigCookie")
time_end = time.time() + (60 * 5)
while time.time() < time_end:
    price_list = []
    time_check = time.time() + (10 * 1)
    while time.time() < time_check:
        cookie.click()

    unlocked = driver.find_elements(By.CLASS_NAME, value="unlocked")
    for item in unlocked:
        data = item.text.split("\n")[1].replace(",", "")
        price_list.append(data)

    cookie_counter = driver.find_element(By.ID, value="cookies").text
    cookie_counter = cookie_counter.split("\n")[0].split(" ")[0].replace(",", "")

    for each in range(len(price_list)-1, 0, -1):
        if int(cookie_counter) > int(price_list[each]):
            highest_index = price_list.index(price_list[each])
            driver.find_element(By.ID, value=f"product{highest_index}").click()
        else:
            continue

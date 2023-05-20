from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url=url)

cookie = driver.find_element(By.ID, "cookie")



# timeout = time.time() + 60*5
timeout = time.time() + 60
is_clickable = True
while is_clickable:
    time.sleep(0.01)
    cookie.click()
    if time.time() > timeout:
        is_clickable = False

available_cookie = driver.find_element(By.ID, "money").text.replace(",","")
# store_items[0].find_element(By.TAG_NAME, "b").click()


store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
for item in store_items[len(store_items)-2::-1]:
    cost = item.find_element(By.TAG_NAME, "b").text.split(" ")
    item_id = item.get_attribute("ID")
    print(item_id)
    print(cost)
    cost = cost[len(cost)-1]
    cost = int(cost.replace(",",""))
    print(cost)
    print(available_cookie)
    if cost > int(available_cookie):
        pass
    elif cost < int(available_cookie):
        while cost < int(available_cookie):
            driver.find_element(By.ID, item_id).click()

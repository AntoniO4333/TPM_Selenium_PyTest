from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get('https://www.python.org')
time.sleep(5)

download_link = driver.find_element(By.XPATH, '//a[@href="/downloads/"]')
download_link.click()
time.sleep(5)

keyword = "python 3.11"
input_search = driver.find_element(By.ID, 'id-search-field')
input_search.send_keys(keyword)

button_go = driver.find_element(By.ID, 'submit')
button_go.click()
time.sleep(5)

driver.quit()

# ВЫПОЛНИЛ: ЧЕРЕМУШКИН АНТОН

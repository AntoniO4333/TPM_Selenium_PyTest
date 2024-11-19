from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
h2_elements = driver.find_elements(By.CSS_SELECTOR, "h2")
print("\nТексты заголовков h2:")
for h2 in h2_elements: print(h2.text)

nav_menu_links = driver.find_elements(By.CSS_SELECTOR, "#mainnav a")
print("\nСсылки в Navigation Menu:")
for link in nav_menu_links: print(link.get_attribute("href"))

driver.quit()
#ЧЕРЕМУШКИН АНТОН

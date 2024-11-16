from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


driver.get('https://the-internet.herokuapp.com/context_menu')

context_menu_element = driver.find_element(By.ID, 'hot-spot')
ActionChains(driver).context_click(context_menu_element).perform()

time.sleep(20)

driver.get('https://the-internet.herokuapp.com/upload')

file_input = driver.find_element(By.ID, 'file-upload')
file_input.send_keys(r'C:\Users\anton\PycharmProjects\TPM_lab1\empty_file.txt')

submit_button = driver.find_element(By.ID, 'file-submit')
submit_button.click()

time.sleep(20)

driver.quit()
#ЧЕРЕМУШКИН АНТОН

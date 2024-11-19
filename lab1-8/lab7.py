import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.execute_script("window.open('https://www.base64encode.org/');")
driver.execute_script("window.open('https://en.wikipedia.org');")  # Вкладка английской Википедии
driver.execute_script("window.open('https://ru.wikipedia.org');")  # Вкладка русской Википедии
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[0])
driver.close()  # Закрываем вкладку конвертера
time.sleep(1)
tabs = driver.window_handles
time.sleep(2)
# Переход на русскую Википедию и открытие 5 случайных статей
driver.switch_to.window(tabs[2])
action = ActionChains(driver)

for _ in range(5):
    random_article_link = driver.find_element(By.XPATH, "//li[@id='n-randompage']/a")
    action.key_down(Keys.CONTROL).click(random_article_link).key_up(Keys.CONTROL).perform()
    time.sleep(1)

time.sleep(5)

# Переход на английскую Википедию
driver.switch_to.window(tabs[1])

# Открытие меню LeftNavBar один раз
menu_button = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")
menu_button.click()

# Открытие 5 случайных статей
for _ in range(5):
    menu_button.click()
    time.sleep(1)
    random_article_link = driver.find_element(By.XPATH, "//li[@id='n-randompage']/a")
    action.key_down(Keys.CONTROL).click(random_article_link).key_up(Keys.CONTROL).perform()
    time.sleep(1)

time.sleep(5)

# Получение заголовков со всех открытых статей
titles = []
for tab in driver.window_handles:
    driver.switch_to.window(tab)
    title = driver.title
    if title:
        titles.append(title)

# Закрываем все вкладки статей
for tab in driver.window_handles[3:]:
    driver.switch_to.window(tab)
    driver.close()

# Переход на вкладку конвертера Base64
driver.switch_to.window(tabs[0])

# Преобразование заголовков в Base64 через сайт и вывод в консоль
for title in titles[3:]:
    text_input = driver.find_element(By.ID, "input")
    # Очищаем поле ввода, если оно не пустое
    if text_input.text != "":
        text_input.clear()
    text_input.send_keys(title)

    submit_btn = driver.find_element(By.ID, "submit_text")
    submit_btn.click()
    time.sleep(2)  # Ждем обработки

    # Получаем закодированный текст
    output_text = driver.find_element(By.ID, "output")
    encoded_title = output_text.get_attribute("value")  # Получаем значение из поля output
    print(f"Заголовок: {title}")
    print(f"Base64: {encoded_title}\n")

driver.quit()
# ЧЕРЕМУКШИН АНТОН ЕВГЕНЬЕВИЧ

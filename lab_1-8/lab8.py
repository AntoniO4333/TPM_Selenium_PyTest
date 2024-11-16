from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://translate.google.com")

# Поиск и нажатие на нужную кнопку "английский" по ID
try:
    english_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'i16'))
    )
    english_button.click()
except:
    print("Не удалось найти нужную кнопку 'английский'.")

driver.execute_script("window.open('https://www.culture.ru/literature/poems/author-aleksandr-pushkin');")
tabs = driver.window_handles
driver.switch_to.window(tabs[1])

wait = WebDriverWait(driver, 10)
translated_poems = []

poem_links = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, ".Dx0ke a.ICocV[data-cy='next']")))[:8]

for index, link in enumerate(poem_links, start=1):

    link.send_keys(Keys.CONTROL + Keys.RETURN)
    driver.switch_to.window(driver.window_handles[-1])
    poem_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rrWFt"))).text
    poem_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".xZmPc div[data-content='text']"))).text
    driver.close()

    driver.switch_to.window(tabs[0])
    input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.er8xn")))
    input_box.clear()
    input_box.send_keys(poem_text)

    # Ожидание и получение переведенного текста
    translated_elements = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "span[jsname='W297wb']"))
    )
    translated_text = "\n".join([element.text for element in translated_elements])
    translated_poems.append((index, poem_title, poem_text, translated_text))

    button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Удалить исходный текст']")
    driver.execute_script("arguments[0].click();", button)

    driver.switch_to.window(tabs[1])

with open("translated_poems.txt", "w", encoding="utf-8") as file:
    for index, title, original, translated in translated_poems:
        file.write(f"Стихотворение {index}: {title}\n")
        file.write("Оригинал на русском:\n" + original + "\n\n")
        file.write("Перевод на английский:\n" + translated + "\n\n")
        file.write("=" * 50 + "\n\n")

driver.quit()
#ЧЕРЕМУШКИН АНТОН

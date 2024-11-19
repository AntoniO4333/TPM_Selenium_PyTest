from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('https://ci.nsu.ru/news')

wait = WebDriverWait(driver, 10)

# Нач дата
start_date = wait.until(EC.presence_of_element_located((By.ID,
                                        'arrFilter_DATE_ACTIVE_FROM_1')))
start_date.clear()
start_date.send_keys("01.10.2020")

# Конеч дата
end_date = driver.find_element(By.ID, 'arrFilter_DATE_ACTIVE_FROM_2')
end_date.clear()
end_date.send_keys("01.10.2024")

apply_filter_button = driver.find_element(By.XPATH, "//button[text()='Найти']")
apply_filter_button.click()

# Загрузка всех новостей циклом, пока кнопка Загрузить еще не исчезнет
while True:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                            "//a[@class='moreNewsList loadMoreButton']")))
        load_more_button.click()
        time.sleep(2)
    except:
        break

# Все новости в список
news_cards = driver.find_elements(By.CSS_SELECTOR, '.news-list-grid-item')

with open('result.txt', 'w', encoding='utf-8') as file:
    for card in news_cards:
        date = card.find_element(By.CSS_SELECTOR, '.date').text
        title = card.find_element(By.CSS_SELECTOR, 'a.name').text
        link = card.find_element(By.CSS_SELECTOR, 'a.name').get_attribute('href')
        image_url = card.find_element(By.CSS_SELECTOR, 'a.img-wrap img').get_attribute('src')

        file.write(f'{date} {title}\n"{link}"\n"{image_url}"\n\n')

# Закрыть браузер
driver.quit()

#ЧЕРЕМУШКИН АНТОН

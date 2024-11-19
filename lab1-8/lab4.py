from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Настройка драйвера и открытие страницы
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get('https://vk.com/video')

    # Ожидание элементов на странице
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/video-"]')))

    # Поиск видео в разделах "Для вас" и "Тренды"
    videos = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/video-"]')

    video_links = list(set(video.get_attribute('href') for video in videos))  # Убираем дубликаты
    print(f"Найдено {len(video_links)} уникальных ссылок на видео.")

    # Запись количества ссылок в файл
    with open('video_links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ссылка на видео'])
        for link in video_links:
            writer.writerow([link])

    # Создание файла для записи информации о видео
    with open('video_info.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Количество просмотров', 'Лайки', 'Дата создания', 'Название канала', 'Подписчики'])

        # Переход по каждой ссылке и сбор информации
        for link in video_links:
            driver.get(link)

            try:
                # Ожидание загрузки названия видео
                title = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="video_modal_title"]'))
                ).text

                # Количество просмотров и дата создания
                views_and_date = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.vkuiTypography--normalize.VideoModalInfoTitle-module__info--fJmkB'))
                ).text

                # Количество просмотров
                views = views_and_date.split("·")[0].strip()  # Берем часть с количеством просмотров

                # Дата создания
                date = views_and_date.split("·")[1].strip()  # Берем часть с датой

                # Количество лайков
                likes = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.PostFooterAction-module__label--qfx7o'))
                ).text

                # Название канала
                channel_name = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/video/"]'))
                ).text

                # Количество подписчиков на канале
                subscribers = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.vkuiSimpleCell__subtitle'))
                ).text

                # Запись в файл
                writer.writerow([title, views, likes, date, channel_name, subscribers])
                print(f"Обработано видео: {title}")

            except Exception as e:
                print(f"Ошибка при обработке видео {link}: {e}")

finally:
    driver.quit()
#ЧЕРЕМУШКИН АНТОН
















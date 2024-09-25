from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--headless") # Запускает Chrome в безголовом режиме, то есть без отображения графического интерфейса.
    chrome_options.add_argument("--disable-gpu") # Отключает аппаратное ускорение графики (GPU).
    chrome_options.add_argument("--no-sandbox") # Используется в окружениях вроде Docker или CI/CD, где пользователь, запускающий Chrome,
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

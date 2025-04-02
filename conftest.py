import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Helpers.generator import Generator


@pytest.fixture()
def driver():
    """Фикстура для инициализации и завершения работы драйвера Chrome

    Настройки включают:
    - Headless режим
    - Оптимизацию для CI/CD
    - Отключение проблемных графических интерфейсов
    - Автоматическую загрузку драйвера
    """
    options = Options()

    # Базовые настройки производительности
    options.page_load_strategy = 'eager'  # Не ждать полной загрузки страницы
    options.add_argument('--enable-javascript')

    # Настройки для headless-режима и CI/CD
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Исправление ошибки DirectComposition
    options.add_argument('--disable-direct-composition')
    options.add_argument('--disable-gpu')

    # Дополнительные оптимизации
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--log-level=3')  # Уменьшение уровня логов

    # Инициализация драйвера с автоматической загрузкой
    _driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Таймауты и размер окна
    _driver.implicitly_wait(10)
    _driver.set_window_size(1920, 1080)  # Более надежно, чем maximize_window() в headless

    # Переход на тестовую страницу
    _driver.get('https://globalsqa.com/angularJs-protractor/BankingProject/#/manager')

    yield _driver

    # Корректное завершение
    _driver.quit()


@pytest.fixture
def customer_data():
    """Фикстура для генерации тестовых данных клиента

    Возвращает:
        tuple: (first_name, last_name, post_code)
    """
    return Generator.generate_info()


@pytest.fixture
def setup(driver, customer_data):
    """Комбинированная фикстура для подготовки тестовой среды

    Возвращает:
        tuple: (driver, customer_data)
    """
    yield driver, customer_data

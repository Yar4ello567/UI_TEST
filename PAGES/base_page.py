"""Этот файл отвечает за нахождение элементов страницы."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import List


class BasePage:
    """Класс базовой страницы"""

    def __init__(self, driver, timeout=10):
        self.__driver = driver
        self.__timeout = int(timeout)
        self.__wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, value: str) -> WebElement:
        """
        Находит один элемент страницы по XPATH, id и тд.
        """
        return self.__wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        """
        Находит несколько элементов страницы.
        """
        return self.__wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

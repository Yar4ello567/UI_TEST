"""Этот файл отвечает за нахождение элементов страницы."""
from typing import List, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс базовой страницы"""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.__timeout = int(timeout)
        self.__wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, value: str) -> WebElement:
        """
        Находит один элемент страницы по XPATH, id и тд.
        """
        return self.__wait.until(EC.visibility_of_element_located((by, value)),
                                 message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        """
        Находит несколько элементов страницы.
        """
        return self.__wait.until(EC.visibility_of_all_elements_located((by, value)),
                                 message=f'Элементы {by, value} не найдены')

    def wait_and_click(self, by: By, value: str) -> None:
        """
        Ожидает кликабельности элемента по локатору и затем кликает по нему.
        """
        element = self.__wait.until(EC.element_to_be_clickable((by, value)),
                                    message=f'Элемент {by, value} не стал кликабельным')
        element.click()

    def click_element(self, element: WebElement) -> None:
        """
        Ожидает кликабельности уже найденного элемента и кликает по нему.
        """
        element = self.__wait.until(EC.element_to_be_clickable(element),
                                    message="Элемент не стал кликабельным")
        element.click()
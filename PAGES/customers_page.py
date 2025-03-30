"""Отвечает за страницу списка клиентов"""
import allure
from selenium.webdriver.common.by import By
from typing import List
from PAGES.base_page import BasePage


class CustomersPage(BasePage):
    """Класс страницы списка клиентов, наследуется из BasePage"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.__name_list = (By.XPATH, '//td[@class="ng-binding"][1]')
        self.__sort_names = (By.XPATH, '//a[normalize-space()="First Name"]')
        self.__delete_buttons = (By.XPATH, '//button[@ng-click="deleteCust(cust)"]')

    @allure.step("Нажать на кнопку имён два раза для сортировки по алфавиту.")
    def sort_alphabetically(self) -> None:
        """Кликает на кнопку(ссылку) имен в таблице для сортировки."""
        sort = self.find_element(*self.__sort_names)
        sort.click()
        sort.click()

    @allure.step("Получить список имён.")
    def get_names(self) -> List[str]:
        """
        Находит имена по элементам таблицы на странице.
        """
        names = self.find_elements(*self.__name_list)
        names = [name.text for name in names]
        return names

    @allure.step("Удалить клиента по имени.")
    def delete_customer(self, names: List[str], name: str) -> None:
        """
        Находит кнопку удаления клиента по имени из списка.
        """
        buttons = self.find_elements(*self.__delete_buttons)
        position = names.index(name)
        buttons[position].click()

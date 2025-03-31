"""Отвечает за страницу списка клиентов"""
from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Pages.base_page import BasePage


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
        assert sort.is_enabled(), "Кнопка сортировки не доступна"
        actions = ActionChains(self.driver)
        actions.double_click(sort).perform()

    @allure.step("Получить список имён.")
    def get_names(self) -> List[str]:
        """
        Находит имена по элементам таблицы на странице.
        """
        names = self.find_elements(*self.__name_list)
        names = [name.text for name in names]
        return names

    @allure.step("Удалить клиента по имени.")
    def delete_customer_by_name(self, name: str) -> None:
        """
        Удаляет клиента по имени.
        """
        names = self.get_names()
        if name in names:
            position = names.index(name)
            buttons = self.find_elements(*self.__delete_buttons)
            assert buttons[position].is_enabled(), "Кнопка удаления не доступна"
            buttons[position].click()

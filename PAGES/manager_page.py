"""Этот файл отвечает за переход по вкладкам/страницам добавления клиента, списков клиентов."""
import allure
from selenium.webdriver.common.by import By
from PAGES.base_page import BasePage


class ManagerPage(BasePage):
    """Класс страницы перехода по вкладкам, наследуется из BasePage."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.__add_cust_btn = (By.XPATH, '//button[normalize-space()="Add Customer"]')
        self.__cust_btn = (By.XPATH, '//button[normalize-space()="Customers"]')

    @allure.step("Перейти во вкладку добавления клиентов.")
    def to_add_cust(self) -> None:
        """Кликает на вкладку добавления клиентов."""
        self.find_element(*self.__add_cust_btn).click()

    @allure.step("Перейти во вкладку списка клиентов.")
    def to_cust(self) -> None:
        """Кликает на вкладку списка клиентов."""
        self.find_element(*self.__cust_btn).click()

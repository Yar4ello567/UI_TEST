"""Этот файл отвечает за переход по вкладкам/страницам добавления клиента, списков клиентов."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage


class ManagerPage(BasePage):
    """Класс страницы перехода по вкладкам, наследуется из BasePage."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.__add_cust_btn = (By.XPATH, '//button[normalize-space()="Add Customer"]')
        self.__cust_btn = (By.XPATH, '//button[normalize-space()="Customers"]')

    @allure.step("Проверить кликабельность кнопки добавления клиентов")
    def is_add_customer_button_clickable(self) -> bool:
        """Проверяет, кликабельна ли кнопка добавления клиентов"""
        try:
            return self.find_element(*self.__add_cust_btn).is_enabled()
        except:
            return False

    @allure.step("Проверить кликабельность кнопки списка клиентов")
    def is_customers_button_clickable(self) -> bool:
        """Проверяет, кликабельна ли кнопка списка клиентов"""
        try:
            return self.find_element(*self.__cust_btn).is_enabled()
        except:
            return False

    @allure.step("Перейти во вкладку добавления клиентов.")
    def to_add_cust(self) -> None:
        """Кликает на вкладку добавления клиентов."""
        if self.is_add_customer_button_clickable():
            self.find_element(*self.__add_cust_btn).click()
            self._BasePage__wait.until(EC.url_contains("addCust"))
        else:
            raise Exception("Кнопка добавления клиентов не кликабельна")

    @allure.step("Перейти во вкладку списка клиентов.")
    def to_cust(self) -> None:
        """Кликает на вкладку списка клиентов."""
        if self.is_customers_button_clickable():
            self.find_element(*self.__cust_btn).click()
            self._BasePage__wait.until(EC.url_contains("list"))
        else:
            raise Exception("Кнопка списка клиентов не кликабельна")
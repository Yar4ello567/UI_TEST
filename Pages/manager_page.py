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

    @allure.step("Перейти во вкладку добавления клиентов.")
    def to_add_cust(self) -> None:
        """Кликает на вкладку добавления клиентов."""
        try:
            btn = self.find_element(*self.__add_cust_btn)
            btn.click()
            self._BasePage__wait.until(EC.url_contains("addCust"))
        except Exception as e:
            raise Exception(f"Не удалось перейти во вкладку добавления клиентов: {str(e)}")

    @allure.step("Перейти во вкладку списка клиентов.")
    def to_cust(self) -> None:
        """Кликает на вкладку списка клиентов."""
        try:
            btn = self.find_element(*self.__cust_btn)
            btn.click()
            self._BasePage__wait.until(EC.url_contains("list"))
        except Exception as e:
            raise Exception(f"Не удалось перейти во вкладку списка клиентов: {str(e)}")

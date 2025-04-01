"""Этот файл отвечает за страницу добавления клиента."""
import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class AddCustomerPage(BasePage):
    """Класс страницы добавления клиента, наследуется из BasePage."""

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

        self.__first_name = (By.XPATH, '//input[@placeholder="First Name"]')
        self.__last_name = (By.XPATH, '//input[@placeholder="Last Name"]')
        self.__post_code = (By.XPATH, '//input[@placeholder="Post Code"]')
        self.__add_button = (By.XPATH, '//button[@type="submit"]')

    @allure.step("Ввести имя")
    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя клиента"""
        element = self.find_element(*self.__first_name)
        element.send_keys(first_name)

    @allure.step("Ввести фамилию")
    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию клиента"""
        element = self.find_element(*self.__last_name)
        element.send_keys(last_name)

    @allure.step("Ввести почтовый код")
    def enter_post_code(self, post_code: str) -> None:
        """Вводит почтовый код клиента"""
        element = self.find_element(*self.__post_code)
        element.send_keys(post_code)

    @allure.step("Нажать кнопку добавления")
    def click_add_button(self) -> None:
        """Кликает на кнопку добавления клиента"""
        element = self.find_element(*self.__add_button)
        element.click()

    @allure.step("Добавить клиента.")
    def add_customer(self, first_name: str, last_name: str, post_code: str) -> None:
        """
        Добавляет клиента с заданными данными из параметров.
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_post_code(post_code)
        self.click_add_button()

    @allure.step("Проверить вывод всплывающего окна и закрыть его.")
    def handle_alert(self) -> str:
        """
        Считывание текста из всплывающего окна и его закрытие.
        """
        self._BasePage__wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()
        return alert_text

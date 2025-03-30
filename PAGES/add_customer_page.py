"""Этот файл отвечает за страницу добавления клиента."""
import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from PAGES.base_page import BasePage


class AddCustomerPage(BasePage):
    """Класс страницы добавления клиента, наследуется из BasePage."""

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

        self.__driver = driver
        self.__first_name = (By.XPATH, '//input[@placeholder="First Name"]')
        self.__last_name = (By.XPATH, '//input[@placeholder="Last Name"]')
        self.__post_code = (By.XPATH, '//input[@placeholder="Post Code"]')
        self.__add_button = (By.XPATH, '//button[@type="submit"]')

    @allure.step("Добавить клиента.")
    def add_customer(self, first_name: str, last_name: str, post_code: str) -> None:
        """
        Добавляет клиента с заданными данными из параметров.
        """
        self.find_element(*self.__first_name).send_keys(first_name)
        self.find_element(*self.__last_name).send_keys(last_name)
        self.find_element(*self.__post_code).send_keys(post_code)
        self.find_element(*self.__add_button).click()

    @allure.step("Проверить вывод всплывающего окна и закрыть его.")
    def handle_alert(self) -> str:
        """
        Считывание текста из всплывающего окна и его закрытие.
        """
        alert = Alert(self.__driver)
        alert_text = alert.text
        alert.accept()
        return alert_text

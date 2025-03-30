import allure
from HELPERS.customers_handler import CustomerHandler
from HELPERS.generator import Generator
from PAGES.add_customer_page import AddCustomerPage
from PAGES.customers_page import CustomersPage
from PAGES.manager_page import ManagerPage


@allure.title('Проверить функциональность добавления клиента')
def test_1(driver) -> None:
    manager_page = ManagerPage(driver)
    manager_page.to_add_cust()

    # Добавляем пользователя с данными из генератора
    add_customer_page = AddCustomerPage(driver)
    customer = Generator.generate_info()
    add_customer_page.add_customer(*customer)
    success = add_customer_page.handle_alert()

    assert "Customer added successfully" in success, (
        f'Ошибка при добавлении клиента, "{success}".'
    )

    manager_page.to_cust()

    # Следует убедиться что он и вправду добавился
    customers_page = CustomersPage(driver)
    names = customers_page.get_names()

    assert customer[0] in names, (
        f'Клиент "{customer[0]}" не найден в списке.'
    )


@allure.title("Проверить функциональность сортировки имен в списке клиентов")
def test_2(driver) -> None:
    manager_page = ManagerPage(driver)
    manager_page.to_cust()

    # Сортируем список на странице, и смотрим если он отсортирован правильно
    customers_page = CustomersPage(driver)
    customers_page.sort_alphabetically()
    names = customers_page.get_names()

    assert names == sorted(names, key=str.lower), (
        'Список не отсортирован по алфавиту.'
    )


@allure.title("Проверить функциональность удаления клиентов в списке")
def test_3(driver) -> None:
    # Переходим в список клиентов
    manager_page = ManagerPage(driver)
    manager_page.to_cust()

    # Находим среднее арифметическое и клиента у которого имя по длине близко к нему
    customers_page = CustomersPage(driver)
    name_list = customers_page.get_names()
    average = CustomerHandler.get_avg_len(name_list)
    name = CustomerHandler.get_closest_avg(name_list, average)
    customers_page.delete_customer(name_list, name)

    assert not (name in customers_page.get_names()), (
        'Клиент не удалился из списка.'
    )

import allure

from Helpers.customers_handler import CustomerHandler
from Pages.add_customer_page import AddCustomerPage
from Pages.customers_page import CustomersPage
from Pages.manager_page import ManagerPage


@allure.title('Проверить функциональность добавления клиента')
def test_add_customer(driver, customer_data) -> None:
    manager_page = ManagerPage(driver)
    manager_page.to_add_cust()

    add_customer_page = AddCustomerPage(driver)
    add_customer_page.add_customer(*customer_data)
    success = add_customer_page.handle_alert()

    assert "Customer added successfully" in success, (
        f'Ошибка при добавлении клиента, "{success}".'
    )

    manager_page.to_cust()
    customers_page = CustomersPage(driver)
    names = customers_page.get_names()

    assert customer_data[0] in names, (
        f'Клиент "{customer_data[0]}" не найден в списке.'
    )


@allure.title("Проверить функциональность сортировки имен в списке клиентов")
def test_sort_customers(driver) -> None:
    manager_page = ManagerPage(driver)
    manager_page.to_cust()

    customers_page = CustomersPage(driver)
    # Получаем список до сортировки
    initial_names = customers_page.get_names()

    # Сортируем и получаем список после сортировки
    sorted_names = customers_page.sort_alphabetically()

    # Проверяем что список изменился (это подтвердит что сортировка сработала)
    assert initial_names != sorted_names, (
        'Список не изменился после сортировки.'
    )

    # Проверяем что список отсортирован либо по возрастанию, либо по убыванию
    is_ascending = sorted_names == sorted(initial_names, key=str.lower)
    is_descending = sorted_names == sorted(initial_names, key=str.lower, reverse=True)

    assert is_ascending or is_descending, (
        'Список не отсортирован ни по возрастанию, ни по убыванию.'
    )


@allure.title("Проверить функциональность удаления клиентов в списке")
def test_delete_customer(driver) -> None:
    manager_page = ManagerPage(driver)
    manager_page.to_cust()

    customers_page = CustomersPage(driver)
    name_list = customers_page.get_names()

    # Получаем имя для удаления из обработчика
    name_to_delete = CustomerHandler.get_name_to_delete(name_list)
    customers_page.delete_customer_by_name(name_to_delete)

    assert name_to_delete not in customers_page.get_names(), (
        'Клиент не удалился из списка.'
    )

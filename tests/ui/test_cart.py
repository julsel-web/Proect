import allure
import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


@allure.epic("UI")
@allure.feature("Корзина")
@pytest.mark.ui
@allure.title("Добавление товара в корзину со страницы Products")
def test_user_can_add_product_to_cart(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    products_page = ProductsPage(ui_page, ui_base_url)
    cart_page = CartPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()
    products_page.add_first_product_to_cart()
    products_page.open_cart_from_modal()

    cart_page.should_be_opened()
    cart_page.should_contain_product()


@allure.epic("UI")
@allure.feature("Корзина")
@pytest.mark.ui
@allure.title("Переход в корзину из шапки сайта")
def test_user_can_open_cart_from_header(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    cart_page = CartPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_cart()

    cart_page.should_be_opened()


@allure.epic("UI")
@allure.feature("Корзина")
@pytest.mark.ui
@allure.title("Повторное добавление товара не ломает отображение корзины")
def test_user_can_add_product_and_keep_browsing(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    products_page = ProductsPage(ui_page, ui_base_url)
    cart_page = CartPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()
    products_page.add_first_product_to_cart()
    products_page.continue_shopping()
    products_page.add_first_product_to_cart()
    products_page.open_cart_from_modal()

    cart_page.should_be_opened()
    cart_page.should_contain_product()

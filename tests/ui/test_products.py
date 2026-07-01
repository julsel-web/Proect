import allure
import pytest

from data.ui_data import SEARCH_QUERY
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


@allure.epic("UI")
@allure.feature("Каталог")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Открытие страницы Products")
def test_products_page_is_opened(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    products_page = ProductsPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()

    products_page.should_be_opened()


@allure.epic("UI")
@allure.feature("Каталог")
@pytest.mark.ui
@allure.title("Поиск товара по названию")
def test_user_can_search_product(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    products_page = ProductsPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()
    products_page.search_product(SEARCH_QUERY)

    products_page.should_show_search_results(SEARCH_QUERY)


@allure.epic("UI")
@allure.feature("Карточка товара")
@pytest.mark.ui
@allure.title("Открытие карточки товара из каталога")
def test_user_can_open_product_details(ui_page, ui_base_url):
    home_page = HomePage(ui_page, ui_base_url)
    products_page = ProductsPage(ui_page, ui_base_url)
    product_details_page = ProductDetailsPage(ui_page, ui_base_url)

    home_page.open_home_page()
    home_page.go_to_products()
    products_page.open_first_product()

    product_details_page.should_be_opened()
    product_details_page.should_have_default_quantity()

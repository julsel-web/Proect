import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_TITLE = ".breadcrumbs .active"
    CART_ROWS = "#cart_info_table tbody tr"
    CHECKOUT_BUTTON = ".check_out"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Проверить открытие корзины")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}/view_cart")
        expect(self.page.locator(self.CART_TITLE)).to_contain_text("Shopping Cart")

    @allure.step("Проверить, что в корзине есть товар")
    def should_contain_product(self):
        expect(self.page.locator(self.CART_ROWS).first).to_be_visible()

    @allure.step("Проверить количество товаров в корзине")
    def should_have_at_least_products(self, count: int):
        expect(self.page.locator(self.CART_ROWS)).to_have_count(count)

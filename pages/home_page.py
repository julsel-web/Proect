import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class HomePage(BasePage):
    FEATURES_ITEMS = ".features_items"
    FIRST_PRODUCT_CARD = ".features_items .product-image-wrapper"
    FIRST_ADD_TO_CART_BUTTON = ".features_items .product-image-wrapper a[data-product-id]"
    VIEW_FIRST_PRODUCT_LINK = ".choose a"
    SUBSCRIPTION_TITLE = "div.single-widget h2"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Открыть главную страницу")
    def open_home_page(self):
        self.open()

    @allure.step("Проверить, что главная страница открыта")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}/")
        self.expect_visible(self.FEATURES_ITEMS)

    @allure.step("Перейти в каталог товаров")
    def go_to_products(self):
        self.page.locator("a[href='/products']").filter(has_text="Products").first.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.page.locator("a[href='/view_cart']").filter(has_text="Cart").first.click()

    @allure.step("Перейти на страницу логина")
    def go_to_login(self):
        self.page.locator("a[href='/login']").filter(has_text="Signup / Login").first.click()

    @allure.step("Перейти на страницу Contact Us")
    def go_to_contact_us(self):
        self.page.locator("a[href='/contact_us']").filter(has_text="Contact us").first.click()

    @allure.step("Открыть карточку первого товара")
    def open_first_product(self):
        self.page.locator(self.FIRST_PRODUCT_CARD).first.hover()
        self.page.locator(self.VIEW_FIRST_PRODUCT_LINK).first.click()

    @allure.step("Добавить первый товар в корзину")
    def add_first_product_to_cart(self):
        self.page.locator(self.FIRST_PRODUCT_CARD).first.hover()
        self.page.locator(self.FIRST_ADD_TO_CART_BUTTON).first.click()

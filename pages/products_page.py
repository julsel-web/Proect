import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ProductsPage(BasePage):
    ALL_PRODUCTS_TITLE = "h2.title.text-center"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCH_RESULTS_TITLE = "h2.title.text-center"
    PRODUCT_CARDS = ".features_items .product-image-wrapper"
    FIRST_VIEW_PRODUCT = "a[href='/product_details/1']"
    FIRST_ADD_TO_CART = ".features_items a[data-product-id='1']"
    CONTINUE_SHOPPING_BUTTON = "button.btn.btn-success.close-modal"
    CART_MODAL = "#cartModal"
    VIEW_CART_LINK = "u"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Проверить открытие страницы Products")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}/products")
        expect(self.page.locator(self.ALL_PRODUCTS_TITLE)).to_contain_text("All Products")
        expect(self.page.locator(self.PRODUCT_CARDS).first).to_be_visible()

    @allure.step("Выполнить поиск товара")
    def search_product(self, query: str):
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    @allure.step("Проверить результаты поиска")
    def should_show_search_results(self, query: str):
        expect(self.page.locator(self.SEARCH_RESULTS_TITLE)).to_contain_text("Searched Products")
        expect(self.page.get_by_text(query).first).to_be_visible()

    @allure.step("Открыть первую карточку товара")
    def open_first_product(self):
        self.page.locator(self.FIRST_VIEW_PRODUCT).first.click()

    @allure.step("Добавить товар в корзину со страницы Products")
    def add_first_product_to_cart(self):
        self.page.locator(self.PRODUCT_CARDS).first.hover()
        self.page.locator(self.FIRST_ADD_TO_CART).first.click()
        expect(self.page.locator(self.CART_MODAL)).to_be_visible()

    @allure.step("Открыть корзину из модального окна")
    def open_cart_from_modal(self):
        self.page.get_by_role("link", name="View Cart").click()

    @allure.step("Закрыть модальное окно и продолжить покупки")
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

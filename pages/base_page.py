from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = ""):
        self.page.goto(f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str):
        self.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.locator(selector).fill(value)

    def text(self, selector: str) -> str:
        return self.locator(selector).inner_text().strip()

    def expect_visible(self, selector: str):
        expect(self.locator(selector)).to_be_visible()

    def expect_url_contains(self, path: str):
        expect(self.page).to_have_url(f"{self.base_url}{path}")

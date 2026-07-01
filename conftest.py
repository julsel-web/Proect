import json
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page

from clients.jsonplaceholder_client import JSONPlaceholderClient
from config.settings import settings


@pytest.fixture(scope="session")
def ui_base_url() -> str:
    return settings.ui_base_url


@pytest.fixture(scope="session")
def api_base_url() -> str:
    return settings.api_base_url


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {"width": 1440, "height": 900},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": settings.headless,
        "slow_mo": settings.slow_mo,
    }


@pytest.fixture
def ui_page(page: Page):
    page.set_default_timeout(settings.timeout)
    return page


@pytest.fixture
def api_client(api_base_url: str) -> JSONPlaceholderClient:
    return JSONPlaceholderClient(base_url=api_base_url)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

    if report.when != "call" or report.passed:
        return

    page = item.funcargs.get("page")
    if page:
        allure.attach(
            page.screenshot(full_page=True),
            name="failure-screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(page.url, name="page-url", attachment_type=allure.attachment_type.TEXT)


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default=settings.browser_name,
        choices=["chromium", "firefox", "webkit"],
        help="Браузер для UI-тестов.",
    )


@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser-name")


@pytest.fixture(scope="session", autouse=True)
def ensure_artifact_directories():
    for directory in ("allure-results", "artifacts/screenshots", "artifacts/api"):
        Path(directory).mkdir(parents=True, exist_ok=True)


def save_api_artifact(name: str, payload: dict | list):
    path = Path("artifacts/api") / f"{name}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path

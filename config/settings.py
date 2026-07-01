import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_bool_env(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    ui_base_url: str = os.getenv("UI_BASE_URL", "https://automationexercise.com").rstrip("/")
    api_base_url: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
    browser_name: str = os.getenv("BROWSER", "chromium")
    headless: bool = _get_bool_env("HEADLESS", True)
    timeout: int = int(os.getenv("TIMEOUT", "10000"))
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))


settings = Settings()

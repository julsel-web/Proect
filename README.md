# Frontend- и backend-автотесты для Automation Exercise и JSONPlaceholder

Проектная работа по курсу QA Python. В проекте собраны UI-тесты для сайта [Automation Exercise](https://automationexercise.com/) и API-тесты для сервиса [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Цель проекта

- показать практическое применение Pytest, Playwright, Requests и Allure
- реализовать проект по требованиям учебного ТЗ
- покрыть UI и API публичных ресурсов автотестами

## Стек

- Python
- Pytest
- Playwright
- Requests
- Allure
- Jenkins

## Что реализовано

- Page Object для UI-части
- API client с методами `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- вынесенные настройки через `.env`
- `headless`-режим браузера
- скриншот при падении UI-теста
- вложения request/response в Allure для API
- сценарий CI-запуска через `Jenkinsfile`

## Структура проекта

```text
.
├── clients
│   ├── base_client.py
│   └── jsonplaceholder_client.py
├── config
│   └── settings.py
├── data
│   ├── api_payloads.py
│   └── ui_data.py
├── pages
│   ├── base_page.py
│   ├── cart_page.py
│   ├── contact_us_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_details_page.py
│   └── products_page.py
├── tests
│   ├── api
│   └── ui
├── utils
│   └── assertions.py
├── conftest.py
├── Jenkinsfile
├── pytest.ini
├── requirements.txt
└── README.md
```

## Подготовка окружения

1. Создать виртуальное окружение:

```bash
python3 -m venv .venv
```

2. Активировать окружение:

```bash
source .venv/bin/activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Установить браузеры для Playwright:

```bash
playwright install chromium
```

## Настройки

Пример `.env`:

```env
UI_BASE_URL=https://automationexercise.com/
API_BASE_URL=https://jsonplaceholder.typicode.com/
HEADLESS=true
BROWSER=chromium
TIMEOUT=10000
SLOW_MO=0
```

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск только UI-тестов:

```bash
pytest -m ui --browser-name=chromium
```

Запуск только API-тестов:

```bash
pytest -m api
```

Запуск smoke-набора:

```bash
pytest -m smoke
```

Запуск с Allure:

```bash
pytest --alluredir=allure-results
```

Просмотр отчёта:

```bash
allure serve allure-results
```

## Покрытые UI-сценарии

- открытие главной страницы
- переходы в `Products`, `Cart`, `Signup / Login`, `Contact Us`
- поиск товара
- открытие карточки товара
- добавление товара в корзину
- проверка формы неуспешного логина
- проверка доступности формы регистрации
- отправка формы `Contact Us`

## Покрытые API-сценарии

- получение коллекций `posts`, `comments`, `albums`, `photos`, `todos`, `users`
- получение сущностей по `id`
- проверки на несуществующие `id`
- создание сущностей через `POST`
- обновление `PUT`
- частичное обновление `PATCH`
- удаление `DELETE`

Всего в проекте больше 20 API-проверок с учётом параметризации.

## Allure

В отчёт добавляются:

- `title`
- `epic` и `feature`
- `step`
- `request/response` для API
- скриншот и URL страницы при падении UI-теста

## Jenkins

В `Jenkinsfile` настроены этапы:

- установка зависимостей
- установка браузера Playwright
- запуск API-тестов
- запуск UI-тестов
- сохранение `allure-results` и артефактов

## Ограничения

- UI-сценарии завязаны на доступность публичного сайта и его актуальную вёрстку
- API-сценарии завязаны на поведение публичного демо-сервиса
- для локального запуска UI-тестов должен быть установлен браузер Playwright

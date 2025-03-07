
## SimbirSoft-SDET-TEST
Тестовое для практикума SDET
Использован паттерн проектирования Page Object Model

## Содержание

- [Описание](#описание)
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Запуск тестов](#запуск-тестов)
- [Генерация отчетов Allure](#генерация-отчетов-allure)



## Описание

Проект автоматизированного тестирования веб-приложения; содержит тесты на проверку полей и другие функциональные тесты.

## Требования

- Python 3.13
- Selenium
- Pytest
- Allure
- Google Chrome и ChromeDriver


## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/hany0n/SimbirSoft.git
    cd SimbirSoft
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

Для использования проекта вам необходимо иметь установленный Google Chrome и ChromeDriver.

## Запуск тестов

```bash
pytest --alluredir=results ./test

```

## Генерация отчетов Allure

```bash
allure serve ./results
```

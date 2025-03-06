from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.expected_conditions import alert_is_present
from conftest import driver
from pages.form_fields import FormFields
import allure


@allure.feature('Кейс. Работа с полями и формами')
@allure.story('Все шаги кейса')
def test_open_practice_automation(driver):
    with allure.step('Открытие страницы Form Fields'):
        form_fields = FormFields(driver)
        form_fields.open()
    with allure.step('Заполнить поле Name and Password'):
        form_fields.name_pass_input()
    with allure.step('Из списка What is your favorite drink? выбрать Milk и Coffee'):
        form_fields.checkbox_click()
    with allure.step('Из списка What is your favorite color? выбрать Yellow'):
        form_fields.radiobutton_click()
    with allure.step('В поле Do you like automation? выбрать любой вариант'):
        form_fields.slot_select()
    with allure.step('Поле Email заполнить строкой формата name@example.com'):
        form_fields.email_input()
    with allure.step('''В поле Message написать количество инструментов, описанных в пункте Automation tools
    *** дополнительный пункт повышенной сложности ***
    * В поле Message дополнительно написать инструмент из списка Automation tools, содержащий
    наибольшее количество символов
    '''):
        form_fields.automation_t_list()
    with allure.step('Нажать на кнопку Submit'):
        form_fields.submit_btn_click()
    #form_fields.alert_check("Message received!")
    with allure.step('Появился алерт с текстом Message received!'):
        form_fields.alert_click("Message received!")

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.expected_conditions import alert_is_present
from conftest import driver
from pages.form_fields import FormFields


def test_open_practice_automation(driver):
    form_fields = FormFields(driver)
    form_fields.open()
    form_fields.name_pass_input()
    form_fields.checkbox_click()
    form_fields.radiobutton_click()
    form_fields.slot_select()
    form_fields.email_input()
    form_fields.automation_t_list()
    form_fields.submit_btn_click()
    #form_fields.alert_check("Message received!")
    form_fields.alert_click("Message received!")

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormFields:


    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://practice-automation.com/form-fields/")

        assert "Form Fields" in self.driver.title


    def name_pass_input(self):
        name = self.driver.find_element(By.ID, "name-input")
        password = self.driver.find_element(By.XPATH, "//input[@type='password']")
        name.send_keys("Ivan")
        password.send_keys("qwerty")


    def checkbox_click(self):
        fav_drink_milk = self.driver.find_element(By.XPATH, "//input[@value='Milk']")
        fav_drink_milk.click()
        fav_drink_coffee = self.driver.find_element(By.XPATH, "//input[@value='Coffee']")
        fav_drink_coffee.click()


    def radiobutton_click(self):
        fav_color_yellow = self.driver.find_element(By.XPATH, "//input[@value='Yellow']")
        fav_color_yellow.click()
        res = fav_color_yellow.is_selected()


    def slot_select(self):

        automation_like = self.driver.find_element(By.XPATH, "//select[@name='automation']")
        ActionChains(self.driver) \
            .scroll_to_element(automation_like) \
            .perform()

        automation_like.click()
        automation_like_obj = self.driver.find_element(By.XPATH, "//option[@value='yes']")
        automation_like_obj.click()


    def email_input(self):
        email_elem = self.driver.find_element(By.XPATH, "//input[@id='email']")
        email_elem.send_keys("email_test@mail.ru")


    def automation_t_list(self):
        element = self.driver.find_element(By.XPATH, "//ul")
        elements = self.driver.find_elements(By.XPATH, ".//li")
        message_list = []
        for e in elements:
            message_list.append(e.text)


        def func_max_length_element(*args):
            element_max_length = ''
            for i in range(len(message_list)):
                element_cur_length = len(message_list[0])
                if len(message_list[i]) > element_cur_length:
                    element_max_length = message_list[i]

            return 'Наибольшее количество символов в: ' + element_max_length



        input_message = self.driver.find_element(By.XPATH, "//textarea[@id='message']")
        for i in message_list:
            input_message.send_keys(i)


        input_message.send_keys(func_max_length_element(message_list))


    def submit_btn_click(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit-btn']")
        ActionChains(self.driver) \
            .scroll_to_element(submit_button) \
            .perform()

        submit_button.click()


    # def alert_check(self, elem_alert_text):
    #     element = self.driver.find_element(By.LINK_TEXT, elem_alert_text)
    #     element.click()
    #
    #     wait = WebDriverWait(self.driver, timeout=2)
    #     alert = wait.until(lambda d: d.switch_to.alert)
    #     text = alert.text
    #     alert.accept()
    #
    #     assert element.text == elem_alert_text



    def alert_click(self, elem_alert1):
        elem_alert = self.driver.switch_to.alert
        #elem_alert.accept()

        assert elem_alert.text == elem_alert1
        elem_alert.accept()










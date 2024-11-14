from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    EMAIL = 'dapellome@gmail.com'
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    PASSWORD = 'Renderos13!'
    SECONDARY_BTN = (By.CSS_SELECTOR, "a[href='/secondary-listings']")


    def login(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)
        sleep(3)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)
        self.wait_to_be_clickable_click(*self.SIGN_IN_BTN)
        self.click(*self.SIGN_IN_BTN)
        self.wait_for_element_to_disappear(*self.SIGN_IN_BTN)






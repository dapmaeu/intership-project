from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_BTN = (By.XPATH, "//a[text()='Continue']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    EMAIL = 'dapellome@gmail.com'
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    PASSWORD = 'Renderos13!'


    def email_address(self, email):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)

    def input_password(self, password):
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def login(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)
        self.click(*self.SIGN_IN_BTN)



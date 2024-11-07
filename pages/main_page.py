from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    #URL = 'https://soft.reelly.io'
    SECONDARY_BTN = (By.XPATH, "//a[text()='Secondary']")


    def open_main_page(self):
        self.open('https://soft.reelly.io')

    def click_secondary_button(self):
        self.click(*self.SECONDARY_BTN)
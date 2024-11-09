from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class MainPage(Page):
    #URL = 'https://soft.reelly.io'
    SECONDARY_BTN = (By.CSS_SELECTOR, "a[href='/secondary-listings']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")

    def open_main_page(self):
        self.open('https://soft.reelly.io')
        sleep(3)

    def click_secondary_button(self):
        self.click(*self.SECONDARY_BTN)

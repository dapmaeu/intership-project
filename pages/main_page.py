from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class MainPage(Page):
    #URL = 'https://soft.reelly.io'
    SECONDARY_BTN = (By.CSS_SELECTOR, "a[href='/secondary-listings']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    CLOSE_BANNER = (By.XPATH, "//a[@class='button-grey w-inline-block']")

    def open_main_page(self):
        self.open('https://soft.reelly.io')
        sleep(3)

    def close_popup_banner(self):
        self.click(*self.CLOSE_BANNER)
        sleep(3)

    def click_secondary_button(self):
        self.wait_for_element_to_appear(*self.SECONDARY_BTN)
        self.click(*self.SECONDARY_BTN)

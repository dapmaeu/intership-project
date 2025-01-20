from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class LeftSideMenu(Page):

    OFF_PLAN = (By.XPATH, "//div[text()='Off-plan']")


    def click_on_off_plan(self):
        self.click(*self.OFF_PLAN)
        sleep(5)
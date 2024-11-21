from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class MainTopMenu(Page):

    SECONDARY_BUTTON = (By.XPATH, "//div[@class='grid-menu-leaderboard']//a[text()='Secondary']")

    def click_secondary_top_menu(self):
        self.click(*self.SECONDARY_BUTTON)
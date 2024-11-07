from pages.base_page import Page
from pages.secondary_page import SecondaryPage
from pages.sign_in_page import SignInPage
from pages.main_page import MainPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.secondary_page = SecondaryPage(driver)


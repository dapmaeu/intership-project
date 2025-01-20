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
    OFF_PLAN_PAGE = (By.XPATH, "//div[text()='Total projects']")
    FILTER_BTN = (By.XPATH, "//a[@class='filter-button w-inline-block']//div[text()='Filters']")
    UNIT_PRICE_FROM_FILTER= (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    UNIT_PRICE_TO_FILTER = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    STARTING_PRICE = ('1200000')
    MAX_PRICE = ('2000000')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[wized='applyFilterButton']")
    PRICE_VALUE = (By.CSS_SELECTOR, "[wized='projectMinimumPrice']")
    PROPERTY_CARD = (By.CSS_SELECTOR, ".name_object_block")
    SETTINGS_BTN = (By.XPATH, "//div[text()='Settings']")


    def open_main_page(self):
        self.open('https://soft.reelly.io')
        sleep(3)

    def close_popup_banner(self):
        self.click(*self.CLOSE_BANNER)
        sleep(3)

    def click_secondary_button(self):
        self.wait_for_element_to_appear(*self.SECONDARY_BTN)
        self.click(*self.SECONDARY_BTN)

    def click_on_settings_menu(self):
        self.click(*self.SETTINGS_BTN)

    def click_filter_button(self):
        self.click(*self.FILTER_BTN)
        self.input_text(self.STARTING_PRICE, *self.UNIT_PRICE_FROM_FILTER)
        self.input_text(self.MAX_PRICE, *self.UNIT_PRICE_TO_FILTER)
        self.click(*self.APPLY_FILTER_BTN)
        sleep(5)

    def verify_off_plan_page(self):
        expected_text = 'Total projects'
        actual_text = self.find_element(*self.OFF_PLAN_PAGE).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual!= {actual_text}'


    def verify_cards_price_in_range(self):
        self.verify_cards_price_in_range()
        # self.driver.execute_script("window.scrollBy(0, 3000)", "")
        # sleep(3)

        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.PROPERTY_CARD))
        for property in all_cards:
            property_price = property.find_element(*self.PRICE_VALUE)
            amount = property_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"


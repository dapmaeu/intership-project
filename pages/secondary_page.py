from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SecondaryPage(Page):
    FILTERS_BTN = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_SELL_BTN = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    #APPLY_FILTER_BTN = (By.XPATH, "a[text()='Apply filter' and @class='button-filter w-button']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')

    def verify_right_page(self):
        self.verify_partial_url('/secondary-listings')

    def click_filters_button(self):
        self.click(*self.FILTERS_BTN)

    def click_want_to_sell(self):
        self.click(*self.WANT_TO_SELL_BTN)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER_BTN)

    def verify_all_cards_label(self):
        self.verify_all_cards_label()


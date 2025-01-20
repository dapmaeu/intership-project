from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class SettingsPage(Page):

    VERIFICATION_BTN = (By.XPATH, "//div[text()='Verification']")
    UPLOAD_IMAGE = (By.CSS_SELECTOR, ".upload-button-2")
    NEXT_STEP_BTN = (By.CSS_SELECTOR, "[wized='nextButtonStep0']")


    def click_verification(self):
        self.driver.execute_script("window.scrollBy(0, 3000)", "")
        sleep(5)
        self.click(*self.VERIFICATION_BTN)


    def verify_verification_page_opened(self):
        self.verify_partial_url('verification/step-0')
        sleep(5)


    def verify_upload_image_and_next_step(self):
        self.wait_for_element_to_appear(*self.UPLOAD_IMAGE)
        self.wait_for_element_to_appear(*self.NEXT_STEP_BTN)

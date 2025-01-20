from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from time import sleep

@when('Click on the verification option')
def click_verification(context):
    context.app.settings_page.click_verification()

@when('Verify the verification page opens')
def verify_verification_page_opened(context):
    context.app.settings_page.verify_verification_page_opened()

@then('Verify “upload image” and “Next step” buttons are available')
def verify_upload_image_and_next_step(context):
    context.app.settings_page.verify_upload_image_and_next_step()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from time import sleep


@given('Open Reelly main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Close Popup banner')
def close_popup_banner(context):
    context.app.main_page.close_popup_banner()


@when('Click on “Secondary” button')
def click_on_secondary_button(context):
    context.app.main_page.click_secondary_button()


@when('Click on "settings" on left side menu')
def click_on_settings_menu(context):
    context.app.main_page.click_on_settings_menu()


@when('Filter the products by price range from 1200000 to 2000000 AED')
def click_filter_button(context):
    context.app.main_page.click_filter_button()


@when('Verify the off plan page opens')
def verify_off_plan_page(context):
    context.app.main_page.verify_off_plan_page()


@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_cards_price_in_range(context):
    context.app.main_page.verify_cards_price_in_range()




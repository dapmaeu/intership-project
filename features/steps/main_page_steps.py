from selenium import webdriver
from selenium.webdriver.common.by import By
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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on “Secondary” button on the top menu')
def click_secondary_top_menu(context):
    context.app.main_top_menu.click_secondary_top_menu()


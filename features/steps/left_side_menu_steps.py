from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on “off plan” at the left side menu')
def click_on_off_plan(context):
    context.app.left_side_menu.click_on_off_plan()
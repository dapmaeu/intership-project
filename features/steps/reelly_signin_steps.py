from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Log in to the page')
def log_in(context):
    context.app.sign_in_page.login()

@when('Click on Filters')
def click_on_filters(context):
    context.app.sign_in_page.click_on_filters()






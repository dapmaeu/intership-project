from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

FOR_SALE_BLOCK = (By.CSS_SELECTOR, ".for-sale-block")
ALL_CARDS = (By.CSS_SELECTOR, '[wized="listingCardMLS"]')

@when('Verify the right page opens')
def verify_right_page(context):
    sleep(5)
    context.app.secondary_page.verify_right_page()


@when('Click on Filters button')
def click_on_filters_button(context):
    context.app.secondary_page.click_filters_button()


@when('Filter the products by "Want to sell"')
def click_on_want_to_sell(context):
    context.app.secondary_page.click_want_to_sell()


@when('Click on Apply Filter')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()


@then('Verify all cards have "for sale" tag')
def verify_all_cards_label(context):
    context.driver.execute_script("window.scrollBy(0, 5000)","")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0, 5000)","")
    sleep(5)
    all_cards = context.driver.find_elements(*ALL_CARDS)

    for card in all_cards:
        context.wait.until(EC.visibility_of_element_located(FOR_SALE_BLOCK))
        label = card.find_element(*FOR_SALE_BLOCK)
        assert label, 'Product label not found'




from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep


#@given('Open Amazon page')
#def open_amazon(context):
 #context.driver = webdriver.Chrome(executable_path='/Users/raihanamin/Automation/python-selenium-automation/chromedriver')
 #context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_for__product(context, search_word):
 context.app.header.input_search(search_word)
 context.app.header.click_search()

@when('Click on first product')
def click_first_product(context):
 context.app.search_result_page.click_first_product()

@when('Click add to cart button')
def click_add_to_cart_button(context):
 context.app.product_page.click_add_to_cart()

 sleep(10)

@then('Verify cart has {expected_count} item')
def verify_cart_count(context,expected_count):
 context.app.header.verify_cart_count(expected_count)